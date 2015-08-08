from twisted.internet.protocol import Protocol

class Echo(Protocol):

	# factory is used to share state that exists beyond the lifetime of any object.
	def __init__(self, factory):
		self.factory = factory

	def connectionMade(self):
		self.factory.numProtocols = self.factory.numProtocols + 1
		self.transport.write(
		"Welcome! There are currently %d open connections.\n" %
		(self.factory.numProtocols,))
	# Count the number of protocols in a shared object, the factory	
	def connectionLost(self, reason):
		self.factory.numProtocols = self.factory.numProtocols - 1

	def dataReceived(self, data):
		self.transport.write(data)


class WelcomeMessage(Protocol):

	def connectionMade(self):
		self.transport.write("Hello server, I am the client!\r\n")
		self.transport.loseConnection()

class QOTD(Protocol):

	def connectionMade(self):
		self.transport.write("Hey, there. Connection made.")
		self.transport.loseConnection()
