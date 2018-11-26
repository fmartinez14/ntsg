"""
Class Name: Entropy
Description: A numbering scheme that is calculated using the Entropy formula to
determine the number of occurrences of a specific string or character.
"""

class Entropy:
	NoOfUniqueValues = 0
	NoOfPackets = 0

	def __init__(self, data):
		for attribute in data:
			#setattr(object, name, value)
			setattr(self, attribute, data[attribute])
			# self.NoOfUniqueValues = data[0]
			# self.NoOfPackets = data[1]

#start of Contract Responsibilities
	def provideEntropy(): #contract 17


#start of Private Responsibilities


	def calculateEntropy(data):
  		return NoOfUniqueValues/NoOfPackets
