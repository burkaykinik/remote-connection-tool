import socket
from dotenv import load_dotenv
import os

load_dotenv("config.env")
UDP_PORT = int(os.getenv("UDP_PORT"))

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while(True):
    sock.sendto(bytes("thisisamachine","utf-8"),("255.255.255.255",UDP_PORT)) # maybe send machine information?
    
