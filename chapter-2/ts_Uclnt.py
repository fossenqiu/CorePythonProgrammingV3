#!/usr/bin/env python

from socket import *

HOST = '127.0.0.1'   # or 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpClickSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("> ")
    if not data:
        break
    udpClickSock.sendto(data.encode(), ADDR)
    data, addr = udpClickSock.recvfrom(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))

udpClickSock.close()