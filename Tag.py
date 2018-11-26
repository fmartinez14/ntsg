"""
Class Name: Tag
Description: A way for the analyst to notate certain field for later review
"""

import provideFieldAttributes from Field

class Tag:
	TagName = ""
	TaggedField
	TagAnnotation
	#tags = []

	def __init__(self, data):
		# self.TagName = data[0]
		# self.TaggedField = data[1]
		# self.TagAnnotation = data[2]

# start of Contract Responsibilities
	def provideTag(): #contract 18


#start of Private Responsibilities
	def saveTag():
		#Im putting this code in here in case we save info to files
		try:
			tagFile = open('tags.txt', r)
			for eachLine in tagFile:
			#add code
		data.close()
		except IOError:
			print('File not found')


	def createTag():


	def updateTag(data):
		#Im putting this code in here in case we save info to files
		try:
			data = open('tags.txt', w)
			for eachLine in data:
			#add code
		data.close()
		except IOError:
			print('File not found')
