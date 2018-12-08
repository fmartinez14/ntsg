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
        saveButton = Gtk.Button(label="Save")

        createButton.connect("clicked", self.addClicked)
        deleteButton.connect("clicked", self.deleteClicked)
        saveButton.connect("clicked", self.saveClicked)

        hbox.pack_start(createButton, True, True, 0)
        hbox.pack_start(deleteButton, True, True, 0)
        hbox.pack_start(saveButton, True, True, 0)

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

    def saveClicked(self, widget):
        machine.sortMachine()
        for p in machine.messageTypes: print p

class transition():

    def __init__(self):
        self.source = 0
        self.destination = 0

    def setSource(self, source):
        self.source = source

    def setDest(self, destination):
        self.destination = destination

    def createTransition(self, source, destination):
        self.setSource(source)
        self.setDest(destination)
        return self


class stateMachine:

    def __init__(self):
        self.numNodes = 0
        self.graph = pydot.Dot(graph_type='digraph', rankdir = "LR")
        self.node = []
        self.messageTypes = ["A","B", "C", "D" , "E"]
        self.automata = []
        self.transitions = []


    #def calcNumNodes(self, messageTypes):
    def calcNumNodes(self):
        return len(self.messageTypes)
        #return 4

    def initializeMachine(self, messageType):
        self.MessageTypes = []
        self.numNodes = calcNumNodes(messageTypes)

        return self.automata

    def createMachine(self):
        self.graph = pydot.Dot(graph_type='digraph', rankdir = "LR")

        graphlegend = pydot.Cluster(graph_name="NTSG", label="NTSG", rankdir="TB")

        self.node = []

        for i in range(self.numNodes):
            #self.node.append(pydot.Node("Node %d" % (i) + " : " + messageTypes[i].name, rank="same"))
            self.node.append(pydot.Node("Node %d" % (i), rank="same"))
            self.graph.add_node(self.node[i])

        for i in range(self.numNodes):
            if(i < (self.numNodes-1)):
                #draw the initial edges
                self.graph.add_edge(pydot.Edge(self.node[i], self.node[i+1]))
                #create a transition and append it to the list
                
                self.transitions.append(transition().createTransition(i, (i+1)))


        self.graph.write_png('stateMachine.png')

    def deleteEdge(self, source, destination):
        edgeExists = False
        i = 0
        while i < len(self.transitions):
            if(self.transitions[i].source==source and self.transitions[i].destination==destination):
                edgeExists = True
                break
            i+=1
        if(edgeExists==True):
            self.graph.del_edge(self.node[source], self.node[destination])
            self.graph.write_png('stateMachine.png')
            del self.transitions[i]
        else:
            print("Edge from " + str(source) + " to " + str(destination) + " doesn't exists.")

    def addEdge(self, source, destination):
        i = 0  
        if(source==destination):
            print("Nodes can't connect to themselves")
            return
        while i < len(self.transitions):
            if(self.transitions[i].source==source and self.transitions[i].destination==destination):
                print("Edge from " + str(source) + " to " + str(destination) + " already exists.")
                return
            if(self.transitions[i].destination==destination):
                print("Node " + str(destination) + " already is reached by " + str(self.transitions[i].source) + ".")
                return
            if(self.transitions[i].source==source):
                print("Node " + str(source) + " cannot have multiple edges out.")
                return
            i+=1
        self.graph.add_edge(pydot.Edge(self.node[source], self.node[destination]))
        self.graph.write_png('stateMachine.png')
        self.transitions.append(transition().createTransition(source, destination))

    def sortMachine(self):
        i = 0
        lastSource = 0
        lastDest = 0
        temp = []
        temp.append(self.messageTypes[self.transitions[0].source])
        temp.append(self.messageTypes[self.transitions[0].destination])
        lastSource = self.transitions[0].source
        lastDest = self.transitions[0].destination
        while i < len(self.transitions):
            if(len(temp)==len(self.messageTypes)):
                self.messageTypes=temp
                return
            if(self.transitions[i].source==lastDest):
                temp.append(self.messageTypes[self.transitions[i].destination])
                lastDest = self.transitions[i].destination
                i=0
            if(self.transitions[i].destination==lastSource):
                temp.insert(0, self.messageTypes[self.transitions[i].source])
                lastSource = self.transitions[i].source
                i=0
            i+=1


            

machine = stateMachine()
machine.numNodes = machine.calcNumNodes()
machine.createMachine()
