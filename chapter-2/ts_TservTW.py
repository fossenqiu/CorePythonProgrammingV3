#!/usr/bin/env python

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print("... connected from:", clnt)

    def dataReceived(self, data):
        wr_data = '[%s] %s' % (ctime(), data)
        self.transport.write(wr_data.encode())


factory = protocol.Factory()
factory.protocol = TSServProtocol
print("waiting for connection...")
reactor.listenTCP(PORT, factory)
reactor.run()

