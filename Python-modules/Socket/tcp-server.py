import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 1234
# Host a server
s.bind((socket.gethostname(), PORT))