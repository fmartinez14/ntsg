"""
Class Name: Field
Description: A location in a data structure that is used to store data.
"""

import provideEntropy from Entropy
import provideTag from Tag

class Field:
	FieldName = ""
	FieldShowName = false #not sure if its a boolean
	FieldPosition = 0
	FieldSize = 0
	FieldValue = 0
	FieldShow = false #same here

	def __init__(self,data):
        for attribute in data:
            setattr(self, attribute, data[attribute])
        # self.FieldName = data[0]
        # self.FieldShowName = data[1]
        # self.FieldPosition = data[2]
        # self.FieldSize = data[3]
        # self.FieldValue= data[4]
        # self.FieldShow = data[5]

#start of Contract Responsibilities
	def provideFieldAttributes(): #contract 16


#start of Private Responsibilities
	def edit():

