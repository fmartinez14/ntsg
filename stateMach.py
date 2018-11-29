import pydot

# this time, in graph_type we specify we want a DIrected GRAPH
graph = pydot.Dot(graph_type='digraph', rankdir = "LR")

graphlegend = pydot.Cluster(graph_name="NTSG", label="NTSG", rankdir="TB")

numNodes = 5

node = []

for i in range(numNodes):
	node.append(pydot.Node("Node %d" % i, rank="same"))
	graph.add_node(node[i])

for i in range(numNodes):
	if(i < (numNodes-1)):
		graph.add_edge(pydot.Edge(node[i], node[i+1]))
	else:
		graph.add_edge(pydot.Edge(node[i], node[0]))

graph.write_png('example3_graph.png')
