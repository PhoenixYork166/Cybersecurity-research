import socket
import threading

# Accept connections from all Layer3 routed traffic ;)
IP = '0.0.0.0'

# Custom port
PORT = 9998

def main():
    Socket = socket
    server = Socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    
    # Listening to 5 Layer3 routed connections
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}: ')
    
    while True:
        # Instantiating client, address from server object
        client, address = server.accept()
        
        print(f'[*] Accetped connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        
        
        client_handler.start()


def handle_client(client_socket):
    with client_socket as sock:
        
        # Handling client Socket request using reliable chunk of 1024 bytes
        request = sock.recv(1024)
        
        print(f'[*] Received: {request.decode('utf-8')}')
        
        # Sending back Bytes ACK to clients
        sock.send(b'ACK')
        
if __name__ == '__main__':
    main()
    