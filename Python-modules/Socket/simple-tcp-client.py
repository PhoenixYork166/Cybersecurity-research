import socket

target_host = input('Enter target Url [www.google.com]: ')
target_port = input('Enter port [80]: ')

# Creating a TCP Socket object
Socket = socket
client = Socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def handshake_and_send(host, port):

    # Handshake => connect to host using a tuple
    client.connect((host, port))

    # Sending data as Bytes
    client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')

    # Receieve data chunks using 4096 Bytes from host
    response = client.recv(4096)

    # Printing decoded ASCII Bytes response as string
    print(response.decode())

    # Close the socket
    client.close()


try:
    handshake_and_send(target_host, target_port)

except OSError as e:
    print(f'Error...{e}')