from Dependency import Dependency
from PDML import filterField

class Field_Length_Dependency (Dependency):

	def __init__(self, sourceFieldName, targetFieldName):
		Dependency.__init__(self, sourceFieldName, targetFieldName)

		rootField = PDML.filterField(sourceFieldName)
		childField = PDML.filterField(targetFieldName)

		# satisfies SRS#93
		if rootField.getSize() < childField.getSize():
			raise Exception("Field size not large enough for field")

		else:
			return self
