""" This class only stores the packet name and 
    the field name to store where this checksum
    belongs.  The checksum value is store as binary
    number with a field-value pair class
"""
class Checksum (Dependency):
	#satisfies SRS#98
	packetName=""
	fieldName=""

	def __init__(self, packetName, fieldName):

		self.packetName = packetName
		self.fieldName = fieldName