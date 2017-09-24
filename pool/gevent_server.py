'''
Created on 

@author: colvin
'''
#http://www.cnblogs.com/wspblog/p/5941558.html#autoid-1-0-0
import sys
import socket
import time
import gevent
 
from gevent import socket,monkey
monkey.patch_all()
 
 
def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(1000)
    while True:
        cli, addr = s.accept()
        print(cli)
        gevent.spawn(handle_request, cli)
 
 
 
def handle_request(conn):
    try:
        while True:
            data = conn.recvfrom(1024)
            if  data[0] == b'':
                conn.shutdown(socket.SHUT_WR)
                break
            print("recv:", data[0])
#             conn.send(data)
            if not data[0]:
                conn.shutdown(socket.SHUT_WR)
 
    except Exception as  ex:
        print(ex)
    finally:
        conn.close()
if __name__ == '__main__':
    server(8001)