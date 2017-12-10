import socket
import sys
from _thread import * 

#client server activation with telnet

host = ''
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)

def threaded_client(conn):
    conn.send(str.encode('welcome, type your info\n'))
    reply = ""
    while True:
        data = conn.recv(2048)
        reply += data.decode('utf-8')

        if '\n' in data.decode('utf-8'):
            reply = "Server output: " + reply
            conn.sendall(str.encode(reply))
            reply = ""

        if not data:
            break

while True:

    conn, addr = s.accept()
    print('connected to: '+addr[0]+ ':' + str(addr[1]))

    start_new_thread(threaded_client, (conn,))