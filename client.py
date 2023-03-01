import socket
import sys


port = 19143

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.settimeout(10)

s.connect((sys.argv[1],port))

while(True):
    command = input("&>   ")
    