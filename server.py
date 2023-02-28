import socket

port = 19143
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.settimeout(10)

s.bind(('',port))
s.listen()


conn,addr = s.accept()
with conn:
    

