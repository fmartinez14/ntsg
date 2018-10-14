import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class openPCAP(Gtk.ListBoxRow):
    def __init__(self, data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Label(data))

class openPCAPwindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="PCAP")
        self.set_border_width(10)

        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        pcapDescription = Gtk.Label("Launch Description")
        pcapDescription.set_text("Open a PCAP File")
        box_outer.pack_start(pcapDescription, False, False, 0)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        pcapLabel = Gtk.Label("PCAP Name", xalign=0)
        vbox.pack_start(pcapLabel, False, True, 0)

        pcapEntry = Gtk.Entry()
        pcapEntry.props.valign = Gtk.Align.CENTER
        pcapBrowse = Gtk.Button("Browse")
        hbox.pack_start(pcapEntry, False, True, 0)
        hbox.pack_start(pcapBrowse, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        dissectorlabel = Gtk.Label("Dissector     ", xalign=0)
        dissectorEntry = Gtk.Entry()
        dissectorButton = Gtk.Button("Browse")
        hbox.pack_start(dissectorlabel, False, True, 0)
        hbox.pack_start(dissectorEntry, False, True, 0)
        hbox.pack_start(dissectorButton, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 50)
        row.add(hbox)
        ConvertButton = Gtk.Button(label="Convert to PDML")
        CancelButton = Gtk.Button(label="Cancel")
        hbox.pack_start(ConvertButton, True, True, 0)
        hbox.pack_start(CancelButton, True, True, 0)

        listbox.add(row)


win = openPCAPwindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
