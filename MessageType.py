"""
Class Name: MessageType
Description: The information that will be passed through
the nodes of the state machine.
"""

#internal entities
import provideFieldValuePair from FieldValuePair
#external entities
import Message_Template from Message_Template #get method

class MessageType:
	MessageTypeName = ""
	Color = ""

	def __init__(self, data):
		for attribute in data:
            setattr(self, attribute, data[attribute])
        # self.MessageTypeName = data[0]
        # self.Color = data[1]

#start of Contract Responsibilities
	def provideMessageInfo(): #contract 20


#start of Private Responsibilities
	def createMessageType():
		#Im putting this code in here in case we save info to files
		try:
			data = open('messageType.txt', w)
			for eachLine in data:
				#add code
		data.close()
		except IOError:
	print('File not found')

	def updateMessageType():
		#Im putting this code in here in case we save info to files
		try:
			data = open('messageType.txt', w)
			for eachLine in data:
				#add code
		data.close()
		except IOError:
	print('File not found')

	def deleteMessageType():
