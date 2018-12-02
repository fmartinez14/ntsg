import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pydot

class stateMachineWindow(Gtk.Window):

    def __init__(self):

    	#set adjustment for spin buttons
    	ad = Gtk.Adjustment(0, 0, (machine.numNodes - 1), 1, 0, 0)
    	bc = Gtk.Adjustment(0, 0, (machine.numNodes - 1), 1, 0, 0)

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

        #start packing box with image
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        self.img = Gtk.Image()
        self.img.set_from_file("stateMachine.png")
        self.add(self.img)

        vbox.pack_start(self.img, False, True, 0)

        listbox.add(row)

        #start packing box with source spin button
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, False, True, 0)

        sourceLabel = Gtk.Label("Source", xalign=0)
        vbox.pack_start(sourceLabel, False, True, 0)
        self.sourceEntry = Gtk.SpinButton(adjustment=ad, climb_rate=1, digits=0)
        #sourceEntry.set_hexpand(True)
        self.sourceEntry.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.sourceEntry, True, True, 0)

        listbox.add(row)

        #start packing box with destination spin button
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        destinationlabel = Gtk.Label("Destination", xalign=0)
        self.destinationEntry = Gtk.SpinButton(adjustment=bc, climb_rate=1, digits=0)
        #destinationEntry.set_hexpand(True)
        hbox.pack_start(destinationlabel, False, True, 0)
        hbox.pack_start(self.destinationEntry, True, True, 0)

        listbox.add(row)

        #start packing box with create and delete buttons

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 50)
        row.add(hbox)
        createButton = Gtk.Button(label="Create")
        deleteButton = Gtk.Button(label="Delete")

        createButton.connect("clicked", self.addClicked)
        deleteButton.connect("clicked", self.deleteClicked)

        hbox.pack_start(createButton, True, True, 0)
        hbox.pack_start(deleteButton, True, True, 0)

        listbox.add(row)

    def addClicked(self, widget):
    	self.source = (self.sourceEntry.get_value_as_int())
    	self.destination = (self.destinationEntry.get_value_as_int())
     	machine.addEdge(self.source, self.destination)
     	self.img.clear()
     	self.img.set_from_file("stateMachine.png")

    def deleteClicked(self, widget):
    	self.source = (self.sourceEntry.get_value_as_int())
    	self.destination = (self.destinationEntry.get_value_as_int())
    	machine.deleteEdge(self.source, self.destination)
    	self.img.clear()
     	self.img.set_from_file("stateMachine.png")


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
			self.node.append(pydot.Node("Node %d" % (i), rank="same"))
			self.graph.add_node(self.node[i])

		for i in range(self.numNodes):
			if(i < (self.numNodes-1)):
				self.graph.add_edge(pydot.Edge(self.node[i], self.node[i+1]))
			else:
				self.graph.add_edge(pydot.Edge(self.node[i], self.node[0]))


		self.graph.write_png('stateMachine.png')

	def deleteEdge(self, source, destination):
		self.graph.del_edge(self.node[source], self.node[destination])
		self.graph.write_png('stateMachine.png')

	def addEdge(self, source, destination):	
		print(source, destination)	
		self.graph.add_edge(pydot.Edge(self.node[source], self.node[destination]))
		self.graph.write_png('stateMachine.png')

machine = stateMachine()
machine.numNodes = 4
machine.createMachine()

window = stateMachineWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
