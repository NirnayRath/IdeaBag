# server socket that binds to the localhost..

import socket
from _thread import *

host= 'localhost'
port=5000

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)
print('Waiting for connection!!!')
def threaded_client(conn):
    data= conn.recv(2048)
    print('->', data.decode('utf8'))
    conn.send('Got it!!'.encode())
    data= conn.recv(2048)
    print('->', data.decode('utf8'))
    conn.close()
while True:
    conn, addr=s.accept()
    print('connected to :', addr[0], ':', str(addr[1]))

    start_new_thread(threaded_client, (conn, ))