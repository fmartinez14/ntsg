import pydot


class stateMachine:

	def __init(self):
		self.numNodes = 0

	def createMachine(self):
		graph = pydot.Dot(graph_type='digraph', rankdir = "LR")

		graphlegend = pydot.Cluster(graph_name="NTSG", label="NTSG", rankdir="TB")

		node = []

		for i in range(self.numNodes):
			node.append(pydot.Node("Node %d" % i, rank="same"))
			graph.add_node(node[i])

		for i in range(self.numNodes):
			if(i < (self.numNodes-1)):
				graph.add_edge(pydot.Edge(node[i], node[i+1]))
			else:
				graph.add_edge(pydot.Edge(node[i], node[0]))

		graph.del_edge(node[2], node[3])

		graph.write_png('example3_graph.png')

machine = stateMachine()
machine.numNodes = 6
machine.createMachine()
