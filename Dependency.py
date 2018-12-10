class Dependency:
	dependency_type=""

	# these next two attributes satisfy SRS #94 & #98
	target=""
	source=""

	# satisfies SRS #91 & #95, creating a dependency
	def __init__(self, newSourceName, newTargetName, newDepType):
		self.source=newSourceName
		self.target=newTargetName
		self.dependency_type=newDepType