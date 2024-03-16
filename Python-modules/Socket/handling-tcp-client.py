import socket

def main():
    #target_host = "www.google.com"
    target_host = input('Enter target Url [www.google.com]: ')
    #target_port = 80
    target_port = input('Enter port [80]: ')
    #target_port = int(target_port)
    
    try:
        target_port = int(target_port)
        
    except ValueError as e:
        print(f'Port number must be an integer:\n{e}')
        return

    try:
        Socket = socket
        with Socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            
            client.connect((target_host, target_port))
            
            request = f'GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n'
            
            # encoded ASCII bytes sending to client
            client.send(request.encode())
            
            # Receiving ASCII bytes from client using a chunk of 4096 bytes
            response = client.recv(4096)
            
            print('f\n')
            # Printing decoded ASCII bytes in response
            print(f'Response:\n\n{response.decode()}')

    # Handling socket get address info (gai) error related to DNS resolution ;)
    except socket.gaierror as e:
        print(f'Hostname could not be resolved:\n{e}')

    # Handling socket error
    except socket.error as e:
        print(f'Socket error:\n{e}')

    # Handling Exception error
    except Exception as e:
        print(f'An unknown error occurred:\n{e}')
    
if __name__ == '__main__':
    main()


    
    