import socket

target_host = input('Enter host IP [127.0.0.1]: ')
target_port = input('Enter port [9997]: ')
target_port = int(target_port)

# Instantiating socket module as Socket object
Socket = socket

# Create a UDP Socket object
client = Socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def just_send(host, port):
    # Sending data as Bytes
    client.sendto(b'AAABBBCCC', (host, port))

    # Instantiating data, addr from received data chunk of 4096 bytes
    data, addr = client.recvfrom(4096)

    # Printing decoded ASCII Bytes UDP packet response as string
    print(data.decode())
    print(f'\n')
    print(f'addr:\n{addr}')

    # Close the socket
    client.close()

# Connecting to host using a tuple
try:
    just_send(target_host, target_port)

except OSError as e:
    print(f'Error...{e}')