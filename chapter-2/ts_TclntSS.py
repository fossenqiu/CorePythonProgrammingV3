#!/usr/bin/env python

from socket import *

HOST = '127.0.0.1' # or 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    tcpClickSock = socket(AF_INET, SOCK_STREAM)
    tcpClickSock.connect(ADDR)
    data = input(">>> ")
    if not data:
        break
    tcpClickSock.send(b"%s\r\n" % data.encode())
    data = tcpClickSock.recv(BUFSIZE)
    if not data:
        break
    print(data.strip())
    tcpClickSock.close()
