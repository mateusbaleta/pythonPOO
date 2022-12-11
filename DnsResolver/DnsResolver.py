import socket
import sys

host = sys.argv[1]

print(f'{host} ---> {socket.gethostbyname(host)}')