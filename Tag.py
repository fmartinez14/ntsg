"""
Class Name: Tag
Description: A way for the analyst to notate certain field for later review
"""

from Field import Field

class Tag:
	#tags = []

	def __init__(self, TagName, TaggedField, TagAnnotation):
		self.TagName = TagName
		self.TaggedField = TaggedField
		self.TagAnnotation = TagAnnotation


# start of Contract Responsibilities
# 	def provideTag(): #contract 18
#
#
# 	#return tag
# #start of Private Responsibilities
	def saveTag(self, tagName, taggedField, tagAnnotation):
		#Im putting this code in here in case we save info to files
		try:
			tagFile = open('tags.txt', 'a')
			#text =
			tagFile.write(tagName+" "+ taggedField+" "+ tagAnnotation +"\n")
			print("Successfully saved")
			#for eachLine in tagFile:
			tagFile.close()
		except IOError:
			print('File not found')

#
# 	def createTag(self):
#
#
#
# 	def updateTag(data):
# 		#Im putting this code in here in case we save info to files
# 		try:
# 			data = open('tags.txt', w)
# 			for eachLine in data:
# 			#add code
# 		data.close()
# 		except IOError:
# 			print('File not found')

#mytag = Tag("name", "field", "desc")
#mytag.saveTag()
