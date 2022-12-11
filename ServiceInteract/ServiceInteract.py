import sys
import socket

ip = sys.argv[1]
port = int(sys.argv[2])

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((ip, port))

banner = mySocket.recv(1024)
print(f'{banner}\n')

print('Sending USER info...')
mySocket.send(b"USER baleta\r\n")
banner = mySocket.recv(1024)
print(f'{banner}\n')

print('Sending PASS info...')
mySocket.send(b"PASS baleta\r\n")
banner = mySocket.recv(1024)
print(f'{banner}\n')
