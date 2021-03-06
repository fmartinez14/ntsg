import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class openSession(Gtk.ListBoxRow):
    def __init__(self, data):
        SessionLocation = ""
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Label(data))

class openSessionwindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Open Session")
        self.set_border_width(10)

        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        openSessionDescription = Gtk.Label("Launch Description")
        openSessionDescription.set_text("Open an Existing Session")
        box_outer.pack_start(openSessionDescription, False, False, 0)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, False, True, 0)

        openSessionLabel = Gtk.Label("Session \n Name", xalign=0)
        vbox.pack_start(openSessionLabel, False, True, 0)

        openSessionEntry = Gtk.Entry()
        openSessionEntry.props.valign = Gtk.Align.CENTER
        hbox.pack_start(openSessionEntry, True, True, 0)

        openSessionBrowse = Gtk.Button("Browse")
        hbox.pack_start(openSessionBrowse, False, True, 0)
        openSessionBrowse.connect("clicked", self.openSession)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 50)
        row.add(hbox)
        OpenButton = Gtk.Button(label="Open")
        CancelButton = Gtk.Button(label="Cancel")
        CancelButton.connect("clicked", self.exitPrompt)

        hbox.pack_start(OpenButton, True, True, 0)
        hbox.pack_start(CancelButton, True, True, 0)

        listbox.add(row)

    def exitPrompt(self, widget):
        self.destroy()

    def openSession(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Browse clicked")
            print("Session File Path: " + dialog.get_filename())
            self.SessionLocation = dialog.get_filename()
            SessionLocation = self.SessionLocation
            self.openSessionEntry.set_text(self.SessionLocation)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

if __name__ == '__main__':
    win = openSessionwindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
