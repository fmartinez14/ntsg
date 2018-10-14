import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ListBoxRowWithData(Gtk.ListBoxRow):
    def __init__(self, data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Label(data))

class ListBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="New Session")
        self.set_border_width(10)

        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        LaunchDescription = Gtk.Label("Launch Description")
        LaunchDescription.set_text("Create a new session.")
        box_outer.pack_start(LaunchDescription, False, False, 0)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        label1 = Gtk.Label("Session Name", xalign=0)
        vbox.pack_start(label1, True, True, 0)

        sessionEntry = Gtk.Entry()
        sessionEntry.props.valign = Gtk.Align.CENTER
        hbox.pack_start(sessionEntry, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Description", xalign=0)
        descriptionField = Gtk.Entry()
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(descriptionField, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 50)
        row.add(hbox)
        CreateButton = Gtk.Button(label="Create")
        CancelButton = Gtk.Button(label="Cancel")
        hbox.pack_start(CreateButton, True, True, 0)
        hbox.pack_start(CancelButton, True, True, 0)

        listbox.add(row)


win = ListBoxWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
