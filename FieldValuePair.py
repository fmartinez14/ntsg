"""
Class Name: FieldValuePair
Description: A value that defines a pair of fields.
"""

import provideMessageInfo from MessageType
#import FieldManager from FieldManager

class FieldValuePair:
	FieldName = ""
	FieldValue = 0

	def __init__(self, data):
		for attribute in data:
            setattr(self, attribute, data[attribute])
        # self.FieldName = data[0]
        # self.Fieldvalue = data[1]

#start of Contract Responsibilities
	def provideFieldValuePair(): #contract 19


#start of Private Responsibilities

	def add():

	def remove():
