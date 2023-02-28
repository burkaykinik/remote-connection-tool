import socket

port = 19143
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.settimeout(10)

s.bind(('',port))
s.listen()


conn,addr = s.accept()
with conn:
    conn.send("Connected to the device.".encode())
    while(True):
        command = conn.recv(1024).decode()
        if(command == "exit"):
            conn.close()
            break
        #if(command == )

s.close()

