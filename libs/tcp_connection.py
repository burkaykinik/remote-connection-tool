import socket
import sys
import os


class TCPConnection:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(10)
        self.s.connect((ip,port))
        self.s.send("Connected to the device.".encode())

    def send(self,command):

        self.s.send(command.encode())
    
    def recv(self):
        return self.s.recv(1024).decode()
    
    
    def send_and_recv(self,command):
        self.send(command)
        return self.recv()
    
    def close(self):
        self.s.close()
    