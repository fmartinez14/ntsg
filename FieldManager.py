"""
Class Name: FieldManager
Description: An interface class that interacts with all classes in the
Field Description Subsystem.
"""

#internal entities
import provideMessageInfo from MessageType
import provideFieldAttributes from Field
#external entities
import Message_Template from Message_Template
import StateMachine from StateMachine
import PayloadManager from PayloadManager

class FieldManager:

	def __init__(self, data):
		for attribute in data:
			#setattr(object, name, value)
			setattr(self, attribute, data[attribute])

#start of Contract Responsibilities
	def getInfoFromSubsystem(): #contract 21

	def provideInfo(): #contract 22


#start of Private Responsibilities

	def getMessageType():

	def getField():
