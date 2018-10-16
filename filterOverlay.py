import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

filters = [("IPX only","ipx"),
                    ("TCP only","tcp"), 
                    ("UDP only","upd"), 
                    ("Non-DNS", "!{udp.port==53||tcp.port==54}"),
                    ("Eternet Broadcast","Eth.addr == ff:ff:ff:ff:ff:ff")]


class filterOverlayWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Filter")
        self.set_border_width(10)

        mainGrid = Gtk.Grid()
        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)
#begin filterBox
        
        #convert filters to liststore
        filterList = Gtk.ListStore(str,str)
        for item in filters:
            filterList.append(list(item))

        #filterList will display in treeview
        filterTree = Gtk.TreeView(filterList)
        
        rendererCheck = Gtk.CellRendererToggle()
        columnCheck = Gtk.TreeViewColumn("", rendererCheck,text=0)
        filterTree.append_column(columnCheck)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Filter Name", renderer, text=0)
        filterTree.append_column(column)


        column = Gtk.TreeViewColumn("Filter Expression", renderer, text=1)
        filterTree.append_column(column)
        box_outer.pack_start(filterTree, True, True, 0)

        buttonBox = Gtk.ListBox()
        buttonBox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(buttonBox, True, True, 0)

        buttonRow = Gtk.ListBoxRow()
        hbutton = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        buttonRow.add(hbutton)
        vbutton = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbutton.pack_start(vbutton, True, True, 0)

        CreateButton = Gtk.Button(label="Create")
        UpdateButton = Gtk.Button(label="Update")
        DeleteButton = Gtk.Button(label="Delete")
        vbutton.pack_start(CreateButton, True, True, 0)
        hbutton.pack_start(UpdateButton, True, True, 0)
        hbutton.pack_start(DeleteButton, True, True, 0)

        buttonBox.add(buttonRow)

#end filterBox
        filterDescription = Gtk.Label("Filter Description")
        filterDescription.set_text("Create/Update a Filter")
        box_outer.pack_start(filterDescription, False, False, 0)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        filterNameLabel = Gtk.Label("Filter \nName", xalign=0)

        filterNameEntry = Gtk.Entry()
        filterNameEntry.props.valign = Gtk.Align.CENTER
        vbox.pack_start(filterNameLabel, False, True, 0)
        hbox.pack_start(filterNameEntry, True, True, 0)


        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        filterExplabel = Gtk.Label("Filter\nExpression", xalign=0)
        filterExpEntry = Gtk.Entry()
        hbox.pack_start(filterExplabel, False, True, 0)
        hbox.pack_start(filterExpEntry, True, True, 0)


        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 50)
        row.add(hbox)
        SaveButton = Gtk.Button(label="Save")
        CancelButton = Gtk.Button(label="Cancel")
        hbox.pack_start(SaveButton, True, True, 0)
        hbox.pack_start(CancelButton, True, True, 0)

        listbox.add(row)


win = filterOverlayWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
