"""
Class Name: Entropy
Description: A numbering scheme that is calculated using the Entropy formula to
determine the number of occurrences of a specific string or character.
"""

class Entropy:

	def __init__(self, NoOfUniqueValues, NoOfPackets):
		self.NoOfUniqueValues = NoOfUniqueValues
		self.NoOfPackets = NoOfPackets

#start of Contract Responsibilities
	def provideEntropy(self): #contract 17
		entVal = self.__calculateEntropy()
		return(entVal)

#start of Private Responsibilities
	def __calculateEntropy(self):
		return(self.NoOfUniqueValues/self.NoOfPackets)

#testing my code
#entropy=Entropy(10,3)
#entVal1=entropy.provideEntropy()
#print(entVal1)
