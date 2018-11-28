import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import PCAP

class openPCAP(Gtk.ListBoxRow):
    def __init__(self, data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Label(data))

class openPCAPwindow(Gtk.Window):
    PCAPLocation = ""
    # tempVar = ""
    def __init__(self,main):
        Gtk.Window.__init__(self, title="PCAP")
        self.set_border_width(10)
        self.main = main
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

        self.pcapEntry = Gtk.Entry()
        self.pcapEntry.props.valign = Gtk.Align.CENTER

        pcapBrowse = Gtk.Button("Browse")

        pcapBrowse.connect("clicked",self.openPCAP)

        hbox.pack_start(self.pcapEntry, False, True, 0)
        hbox.pack_start(pcapBrowse, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        # dissectorlabel = Gtk.Label("Dissector     ", xalign=0)
        # dissectorEntry = Gtk.Entry()
        # dissectorButton = Gtk.Button("Browse")
        # hbox.pack_start(dissectorlabel, False, True, 0)
        # hbox.pack_start(dissectorEntry, False, True, 0)
        # hbox.pack_start(dissectorButton, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 50)
        row.add(hbox)
        self.ConvertButton = Gtk.Button(label="Convert to PDML")
        CancelButton = Gtk.Button(label="Cancel")
        self.ConvertButton.connect("clicked",self.exitProcess)
        CancelButton.connect("clicked",self.exitPrompt)
        hbox.pack_start(self.ConvertButton, True, True, 0)
        hbox.pack_start(CancelButton, True, True, 0)

        listbox.add(row)


    def openPCAP(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.fileFilters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("PCAP File Path: " + dialog.get_filename())
            self.PCAPLocation = dialog.get_filename()
            PCAPLocation = self.PCAPLocation
            self.pcapEntry.set_text(self.PCAPLocation)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()


    def exitPrompt(self,widget):
        self.destroy()


    def fileFilters(self, dialog):

        PCAPFilter = Gtk.FileFilter()
        PCAPFilter.set_name("PCAP File")
        PCAPFilter.add_mime_type("application/vnd.tcpdump.pcap")
        dialog.add_filter(PCAPFilter)

        allFiles = Gtk.FileFilter()
        allFiles.set_name("Any file")
        allFiles.add_pattern("*")
        dialog.add_filter(allFiles)

    def exitProcess(self,widget):
        # global PCAPLocation
        if(self.PCAPLocation == ""):
            win.destroy()
        myPCAP = PCAP.PCap(self.PCAPLocation)
        myPCAP.convertPCAP()
        self.main.PDMLLocation= myPCAP.obtainFilePath()
        print "Success!"
        self.destroy()

if __name__ == '__main__':
    win = openPCAPwindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
