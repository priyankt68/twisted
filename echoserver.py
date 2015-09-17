from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
	def dataReceived(self, data):
		print "Data received", data
		data = int(data)
		data += int(data)
        	self.transport.write(str(data))

class EchoFactory(protocol.Factory): 
	def buildProtocol(self, addr):
		print "Building Echo protocol"
		return Echo()

# Adding callbacks with the reactor's event driven loop and connecting it onto the 8001 port.
reactor.listenTCP(8001, EchoFactory())
reactor.run()
