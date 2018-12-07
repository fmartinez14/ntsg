class transition():

	def __init__(self):
		self.source = NULL
		self.destination = NULL

	def setSource(self, source):
		self.source = source

	def setDest(self, destination):
		self.destination = destination

	def createTranstition(self, source, destination):
		self.setSource(source)
		self.setDest(destination)
		return self
