from twisted.internet.protocol import Factory
from twisted.internet import reactor, protocol

class QuoteProtocol(protocol.Protocol):
	def __init__(self, factory):
		self.factory = factory

	def connectionMade(self):
		self.factory.numConnections += 1

	def dataReceived(self, data):
		print "Number of active connections: %d" % (self.factory.numConnections,)
		print "Received", self.getQuote()
		print "Sending", self.transport.write(self.getQuote())
		self.updateQuote(data)

	def connectionLost(self,reason):
		self.factory.numConnections -= 1

	def getQuote(self):
		self.factory.quote
	
	def updateQuote(self, quote):
		self.factory.quote = quote

class QuoteFactory(Factory):
	numConnections = 0

	def __init__(self, quote=None):
		print "Starting out here"
		self.quote= quote or "An apple a day keeps the doctor away"

	def buildProtocol(self, addr):
		return QuoteProtocol(self)

reactor.listenTCP(8002, QuoteFactory())
reactor.run()
