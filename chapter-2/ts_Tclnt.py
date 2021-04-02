#!/usr/bin/env python

from socket import *

HOST = '127.0.0.1' # or 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpClickSock = socket(AF_INET, SOCK_STREAM)
tcpClickSock.connect(ADDR)

while True:
    data = input("> ")
    if not data:
        break
    tcpClickSock.send(data.encode())
    data = tcpClickSock.recv(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))

tcpClickSock.close()
