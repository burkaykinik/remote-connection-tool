import socket
from libs import command_split
from libs import execute_command

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
        command_list = command_split(command)
        
        if(command_list[0] == "shell"):
            stdout,stderr = execute_command(command_list[1:])
            conn.send(stdout)
            continue


s.close()

