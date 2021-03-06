#!/usr/bin/env python
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print("waiting for message...")
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(b'[%s] %s' % (bytes(ctime(), 'utf-8'), data), addr)
    print("...received from returned to: ", addr)

udpSerSock.close()
