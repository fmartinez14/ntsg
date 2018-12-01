import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pydot

class stateMachineWindow(Gtk.Window):

    def __init__(self):

    	ad = Gtk.Adjustment(0, 0, 100, 1, 0, 0)
    	bc = Gtk.Adjustment(0, 0, 100, 1, 0, 0)

        Gtk.Window.__init__(self, title="Network Traffic Based Software Generation - State Machine")


        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        machineDescription = Gtk.Label("Launch Description")
        machineDescription.set_text("State Machine")
        box_outer.pack_start(machineDescription, False, False, 0)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        img = Gtk.Image()
        img.set_from_file("stateMachine.png")
        self.add(img)

        vbox.pack_start(img, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, False, True, 0)

        sourceLabel = Gtk.Label("Source", xalign=0)
        vbox.pack_start(sourceLabel, False, True, 0)

        sourceEntry = Gtk.SpinButton(adjustment=ad, climb_rate=1, digits=0)
        sourceEntry.set_hexpand(True)
        self.source = sourceEntry.get_value_as_int()
        #sourceEntry.set_text(self.source)
        sourceEntry.props.valign = Gtk.Align.CENTER
        hbox.pack_start(sourceEntry, True, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        destinationlabel = Gtk.Label("Destination", xalign=0)
        destinationEntry = Gtk.SpinButton(adjustment=bc, climb_rate=1, digits=0)
        destinationEntry.set_hexpand(True)
       	self.destination = destinationEntry.get_value_as_int()
        #destinationEntry.set_text(self.destination)
        hbox.pack_start(destinationlabel, False, True, 0)
        hbox.pack_start(destinationEntry, True, True, 0)

        listbox.add(row)

        """row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        machineDescriptionlabel = Gtk.Label("Destination", xalign=0)
        machineDescriptionEntry = Gtk.Entry()
        hbox.pack_start(machineDescriptionlabel, False, True, 0)
        hbox.pack_start(machineDescriptionEntry, True, True, 0)

        listbox.add(row)"""

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 50)
        row.add(hbox)
        createButton = Gtk.Button(label="Create")
        deleteButton = Gtk.Button(label="Delete")

        createButton.connect("clicked", lambda: stateMachine.addEdge(machine, self.source, self.destination))
        deleteButton.connect("clicked", lambda: stateMachine.deleteEdge(machine, self.source, self.destination))

        hbox.pack_start(createButton, True, True, 0)
        hbox.pack_start(deleteButton, True, True, 0)

        listbox.add(row)


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
			self.node.append(pydot.Node("Node %d" % (i+1), rank="same"))
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

	def addEdge(self, x, y):
		self.graph.add_edge(pydot.Edge(self.node[x], self.node[y]))
		self.graph.write_png('stateMachine.png')

	"""def editEdge(self, x, y, z):
		x = int(float(x))
		y = int(float(y))
		z = int(float(z))
		self.graph.del_edge(self.node[x], self.node[y])
		self.graph.add_edge(pydot.Edge(self.node[x], self.node[z]))
		self.graph.write_png('stateMachine.png')"""

machine = stateMachine()
machine.numNodes = 4
machine.createMachine()

window = stateMachineWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
