"""
	Author: Sergio Ponce De Leon
	Date of Last Edits: 11/25/2018

	This class is "an association between two
	attributes as equal values" -Subsystems Baseline
"""

import provide_message_info from Message_Template

class Field_Equivalence:
	# Probably need to give unique identifier to each field equivalence
	# ref self.add_field_eq
	__feqID = 0

	""" TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
		find out what the constructor needs to initialize
		TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
	""" 
	def __init__(self, data):
		for attribute in data:
			setattr(self,attribute,data[attribute])

	# Contract 15 on the Subsystems Baseline, aka, the last version submitted
	def provide_field_eq:

		""" TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
			look into changing this into a dictionary
			TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
		""" 
		field_eq_data = []
		field_eq_data[0] = # Message_Type attributes, supposed contract 11
		field_eq_data[1] = # Target attributes, supposed contract 11
		field_eq_data[2] = # Source attributes, supposed contract 11
		field_eq_data[3] = # Field Name attributes, supposed contract 11

	# private responsibility
	"""
		Thinking about implementing this "association" it would make sense
		to pair attribute 1 & 2 by declaring a field_eq dictionary in
		the Message_Template

		Bc of uniquie id need to thing about implementing as a @staticmethod
		ref: https://www.python-course.eu/python3_class_and_instance_attributes.php

		for now: creates a 3-element tuple to return
	"""
	def add_field_eq(attribute1, attribute2):
		# Probably need to give unique identifier to each field equivalence
		# ref self.__feqID based on:
		# https://www.python-course.eu/python3_class_and_instance_attributes.php
		type(self).__feqID += 13

		return (self.__feqID, attribute1, attribute2)

	# private responsibility
	"""
		Thinking about implementing by erasing a field_eq element in
		the field_eq dictionary within Message_Template

		Bc of uniquie id need to thing about implementing as a @staticmethod
		ref: https://www.python-course.eu/python3_class_and_instance_attributes.php

		for now: check if id exists in dict passed in, copies dict, deletes pair,
				 returns the copy with removed pair. Based on:
				 https://stackoverflow.com/questions/5844672/delete-an-element-from-
				 a-dictionary
	"""
	def remove_field_eq(id_dict, field_eq_id):
		if field_eq_id in id_dict:
			r = dict(id_dict)
			del r[field_eq_id]
			return r
