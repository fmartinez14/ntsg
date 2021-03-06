import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class launcherOverlay(Gtk.ListBoxRow):
    def __init__(self, data):
        WorkspaceLocation = ""
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Label(data))

class launcherOverlayWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Workspace Launcher")
        self.set_border_width(10)

        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        LaunchDescription = Gtk.Label("Launch Description")
        LaunchDescription.set_text("Select a directory as workspace: NTBGSG uses the workspace\n directory to store sessions.")
        box_outer.pack_start(LaunchDescription, False, False, 0)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        #Start Workspace entry
        workspaceLabel = Gtk.Label("Workspace\n", xalign=0)
        vbox.pack_start(workspaceLabel, True, True, 0)

        WorkspaceEntry = Gtk.Entry()
        WorkspaceEntry.props.valign = Gtk.Align.CENTER
        hbox.pack_start(WorkspaceEntry, False, True, 0)

        WorkspaceBrowse = Gtk.Button(label="Browse")
        WorkspaceBrowse.props.valign = Gtk.Align.CENTER
        hbox.pack_start(WorkspaceBrowse, False, True, 0)
        WorkspaceBrowse.connect("clicked", self.openWorkspace)

        listbox.add(row)
        #End Workspace Entry, begin Destination Entry
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        destinationLabel = Gtk.Label("Destination \n Folder", xalign=0)
        destniationEntry = Gtk.Entry()
        hbox.pack_start(destinationLabel, False, True, 0)
        hbox.pack_start(destniationEntry, False, True, 0)

        listbox.add(row)
        #End Destination Entry, begin path entry
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        pathLabel = Gtk.Label("Destination \n Path", xalign=0)
        pathEntry = Gtk.Entry()
        pathBrowse = Gtk.Button(label="Browse")
        hbox.pack_start(pathLabel, False, True, 0)
        hbox.pack_start(pathEntry, False, True, 0)
        hbox.pack_start(pathBrowse, False, True, 0)


        listbox.add(row)   
        #end path entry, begin buttons     
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 50)
        row.add(hbox)
        LaunchButton = Gtk.Button(label="Launch")

        CancelButton = Gtk.Button(label="Cancel")
        CancelButton.connect("clicked", self.exitPrompt)


        hbox.pack_start(LaunchButton, True, True, 0)
        hbox.pack_start(CancelButton, True, True, 0)

        listbox.add(row)

    def exitPrompt(self, widget):
        self.destroy()

    def openWorkspace(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Browse clicked")
            print("Workspace File Path: " + dialog.get_filename())
            self.WorkspaceLocation = dialog.get_filename()
            WorkspaceLocation = self.WorkspaceLocation
            self.WorkspaceEntry.set_text(self.WorkspaceLocation)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

win = launcherOverlayWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
