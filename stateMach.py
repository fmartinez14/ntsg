import pydot


class stateMachine:

	def __init(self):
		self.numNodes = 0
		self.graph = pydot.Dot(graph_type='digraph', rankdir = "LR")
		self.node = []

	def createMachine(self):
		self.graph = pydot.Dot(graph_type='digraph', rankdir = "LR")

		graphlegend = pydot.Cluster(graph_name="NTSG", label="NTSG", rankdir="TB")

		self.node = []

		for i in range(self.numNodes):
			self.node.append(pydot.Node("Node %d" % i, rank="same"))
			self.graph.add_node(self.node[i])

		for i in range(self.numNodes):
			if(i < (self.numNodes-1)):
				self.graph.add_edge(pydot.Edge(self.node[i], self.node[i+1]))
			else:
				self.graph.add_edge(pydot.Edge(self.node[i], self.node[0]))


		self.graph.write_png('stateMachine.png')

	def deleteEdge(self, x, y):
		self.graph.del_edge(self.node[x], self.node[y])
		self.graph.write_png('stateMachine.png')


machine = stateMachine()
machine.numNodes = 3
machine.createMachine()
machine.deleteEdge(1,2)
