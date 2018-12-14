import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Tag import Tag

class openPCAP(Gtk.ListBoxRow):
    def __init__(self, data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Label(data))

class openTagOverlaywindow(Gtk.Window):
    tag = {}
    def __init__(self):
        Gtk.Window.__init__(self, title="Tag")
        self.set_border_width(10)

        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        tagDescription = Gtk.Label("Launch Description")
        tagDescription.set_text("Tag Overlay")
        box_outer.pack_start(tagDescription, False, False, 0)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        tagLabel = Gtk.Label("Tag Name   ", xalign=0)
        vbox.pack_start(tagLabel, False, True, 0)

        self.tagEntry = Gtk.Entry()
        self.tagEntry.props.valign = Gtk.Align.CENTER
        hbox.pack_start(self.tagEntry, True, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        tagFieldlabel = Gtk.Label("Tag Field      ", xalign=0)
        self.tagFieldEntry = Gtk.Entry()
        hbox.pack_start(tagFieldlabel, False, True, 0)
        hbox.pack_start(self.tagFieldEntry, True, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        tagDescriptionlabel = Gtk.Label("Description", xalign=0)
        self.tagDescriptionEntry = Gtk.Entry()
        hbox.pack_start(tagDescriptionlabel, False, True, 0)
        hbox.pack_start(self.tagDescriptionEntry, True, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 50)
        row.add(hbox)
        SaveButton = Gtk.Button(label="Save")
        SaveButton.connect( "clicked", self.on_saveButton_click )
        CancelButton = Gtk.Button(label="Cancel")
        CancelButton.connect("clicked",self.on_exit_clicked)
        hbox.pack_start(SaveButton, True, True, 0)
        hbox.pack_start(CancelButton, True, True, 0)
        listbox.add(row)

    def on_saveButton_click(self, widget):
        tagName = self.tagEntry.get_text()
        tagField = self.tagFieldEntry.get_text()
        tagDescription = self.tagDescriptionEntry.get_text()

        myTag=Tag(tagName, tagField, tagDescription)
        print ("this is  my tag: ",myTag.TagName, myTag.TaggedField, myTag.TagAnnotation)
        myTag.saveTag(tagName, tagField, tagDescription)
        
        self.destroy()
    #def saveTag()
    def on_exit_clicked(self,widget):
        self.destroy()

if __name__ == '__main__':
    win = openTagOverlaywindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
