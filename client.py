import socket
import sys
from libs import TCPConnection
import dotenv

dotenv.load_dotenv("config.env")
TCP_PORT = int(os.getenv("TCP_PORT"))
UDP_PORT = int(os.getenv("UDP_PORT"))

while(True):
    command = input("&>   ")
    

