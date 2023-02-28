import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while(True):
    sock.sendto(bytes("thisisamachine","utf-8"),("255.255.255.255",19142)) # maybe send machine information?
    
