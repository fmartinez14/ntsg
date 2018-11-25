"""
	Author: Sergio Ponce De Leon
	Date of Last Edits: 11/25/2018

	This class creates a Message_Template instance that has
	a Field_length_Dependency, Packet_Length_Dependency,
	Checksum, Field_Equivalence, and a  Message_Type
"""

""" TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
	look into how Message_Type is used to "generate" a Message_Template
	TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
""" 
import Message_Type from Message_Type
import """Field_Length_Dependency contract 12""" from Field_Length_Dependency
import """Packet_Length_Dependency contract 13""" from Packet_Length_Dependency
import """Checksum contract 14""" from Checksum
import """Field_Equivalence contract 15""" from Field_Equivalence
import """State_Machine contract 8""" from State_Machine
import """Field_Manager contract 22""" from Field_Manager
import """Payload_Manager contract 4""" from Payload_Manager


class Message_Template:
	# class attributes
	# two underscores to initialize as private
	__messageTemplateName = "default_name"
	# why are folderName and FolderPath designed in
	# SRS class diagram to be stored in different variables?
	__destinationFolderName = "some_folder_name"
	__destinationFolderPath = "some_filepath"

	""" TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
		find out what the constructor needs to initialize
		TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
	""" 
	def __init__(self, data):
		for attribute in data:
			setattr(self,attribute,data[attribute])

	# Contract 10 on the Subsystems Baseline, aka, the last version submitted
	def provide_message_template:

		""" TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
			look into changing this into a dictionary
			TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
		""" 
		message_template = []
		message_template[0] = # Field_Length_Dependency contract 12
		message_template[1] = # Packet_Length_Dependency contract 13
		message_template[2] = # Checksum contract 14
		message_template[3] = # Field_Equivalence contract 15

	# Contract 11 on the Subsystems Baseline, aka, the last version submitted
	def provide_message_info:

		""" TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
			look into changing this into a dictionary
			TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
		""" 
		message_info = []
		message_info[0] = # State_Machine contract 8
		message_info[1] = # Field_Manager contract 22
		message_info[2] = # Payload_Manager contract 4

