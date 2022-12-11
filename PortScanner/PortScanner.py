import sys
import socket

for port in range(1,65535):
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    if mySocket.connect_ex((sys.argv[1], port)) == 0:
        print(f'Port {port} [OPEN]')
        mySocket.close()
