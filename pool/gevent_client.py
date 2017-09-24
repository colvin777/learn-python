'''
Created on

@author: colvin
'''
import socket
 
HOST = 'localhost'    # The remote host
PORT = 8001           # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
count =0
while True:
#     msg = bytes(input(">>:"),encoding="utf8")
    count+=1
    msg = b'request %d'  % count
    s.sendall(msg)
#     s.sendall(None)
#     data = s.recv(1024)
    #print(data)
 
#     print('Received', repr(data))
s.close()