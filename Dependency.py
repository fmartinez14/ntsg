class Dependency:
	dependency_type=""

	# these next two attributes satisfy SRS #94 & #98
	target=""
	source=""

	# satisfies SRS #91 & #95, creating a dependency
	def __init__(self, newSource, newTarget, newDepType):
		self.source=newSource
		self.target=newTarget
		self.dependency_type=newDepType