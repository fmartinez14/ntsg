import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class stateMachineWindow(Gtk.Window):

    def __init__(self):
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

        sourceEntry = Gtk.Entry()
        sourceEntry.props.valign = Gtk.Align.CENTER
        hbox.pack_start(sourceEntry, True, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        destinationlabel = Gtk.Label("Destination", xalign=0)
        destinationEntry = Gtk.Entry()
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

        hbox.pack_start(createButton, True, True, 0)
        hbox.pack_start(deleteButton, True, True, 0)

        listbox.add(row)

window = stateMachineWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
