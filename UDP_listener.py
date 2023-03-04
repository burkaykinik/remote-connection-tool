import os
import socket
import sys
import time
import dotenv

dotenv.load_dotenv("config.env")

# this function will listen to UDP Packets that are broadcasted
# and will return what it has received and the address of the sender
def listen_broadcast():
    while(True):
        UDP_PORT = int(os.getenv("UDP_PORT"))
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind(('',UDP_PORT))
        data = sock.recvfrom(1024)
        print(data)

listen_broadcast()
