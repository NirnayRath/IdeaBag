#Client socket here...

import socket

host= '127.0.0.1'
port= 5000
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    print("Waiting for connection form server!!")
    s.connect((host, port))
except :
    print("Exception ocured!!")

while True:
    print("Connection acquired!!")
    s.send(str("Hello Server!!").encode())

    data=s.recv(2048)
    result = data.decode('utf-8')
    if not data:
        break

    print("Server output->", result)
    s.send('Received data!!'.encode())
s.close()
print("socket closed!!")