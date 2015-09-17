from twisted.internet import reactor, protocol

class EchoClient(protocol.Protocol): 
	def connectionMade(self):
		print "Connection made, now sending data to server"
		self.transport.write("1")

	def dataReceived(self, data):
		print "Server said:", data 
		self.transport.loseConnection()

class EchoFactory(protocol.ClientFactory): 
	def buildProtocol(self, addr):
		print "Building client protocol"
		return EchoClient()

	def clientConnectionFailed(self, connector, reason):
		print "Connection failed."
		reactor.stop()

	def clientConnectionLost(self, connector, reason):
		print "Connection lost."
		reactor.stop()

reactor.connectTCP("localhost", 8001, EchoFactory())
reactor.run()
