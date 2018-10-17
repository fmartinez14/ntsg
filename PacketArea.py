import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class PacketArea(Gtk.Box):

    def __init__(self):

        Gtk.Box.__init__(self,orientation=Gtk.Orientation.VERTICAL,spacing=0)
    #Start of Packet area
        PacketLabelBox = Gtk.Box(spacing=0)
        
        PacketAreaLabel = Gtk.Label("Packet Area")
        PacketLabelBox.pack_start(PacketAreaLabel,False,False,0)
        PDMLBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        PDMLBox.pack_start(PacketLabelBox,True,True,0)
        
        PacketBox = Gtk.Box(spacing=5)
        
        PacketLabel = Gtk.Label("Packet")
        PacketBox.pack_start(PacketLabel,True,True,0)

        FieldAreaBox = Gtk.Box()
        
        self.FieldAreaTable = Gtk.ListStore(Gtk.CheckButton,int)
        self.FieldAreaTable = Gtk.ListStore(bool,str,int)
        self.FieldAreaTable.append([False,"Frame 718:frame, eth, ip, tcp",1])
        self.FieldAreaTable.append([False,"Frame 767:frame, eth, ip, tcp",2])
        self.FieldAreaTable.append([False,"Frame 768:frame, eth, ip, tcp",3])

        TableView = Gtk.TreeView(self.FieldAreaTable)
        
        FieldAreaFrame= Gtk.Frame()
        FieldAreaBox.add(FieldAreaFrame)
        
        TableBox = Gtk.Box(spacing=5)
        
        renderer_toggle = Gtk.CellRendererToggle()
        renderer_toggle.connect("toggled", self.on_cell_toggled)
        column_toggle = Gtk.TreeViewColumn("", renderer_toggle, active=0)
        TableView.append_column(column_toggle)

        Render_Name = Gtk.CellRendererText()
        FirstColumn = Gtk.TreeViewColumn("Package Area",Render_Name,text=1)
        TableView.append_column(FirstColumn)
        
        Render_Showname= Gtk.CellRendererText()
        Render_Showname.set_property("editable",True)
        # Render_Showname.connect("edited",self.showName_edited)
        SecondColumn = Gtk.TreeViewColumn("Size",Render_Showname,text=2)
        TableView.append_column(SecondColumn)
        
        self.add(TableView)
        
        TableBox.pack_start(TableView,False,False,0)
        FieldAreaBox.pack_start(TableBox,False,False,0)
    
        
        RemoveButton = Gtk.Button(label="Remove")
        TableBox.pack_start(RemoveButton,True,True,0)
        
        ClearButton = Gtk.Button(label="Clear")
        TableBox.pack_start(ClearButton,True,True,0)
        
        PDMLBox.pack_start(FieldAreaBox,True,False,4)
    #End of Packet area 
    
    def on_cell_toggled(self, widget, path):
        self.FieldAreaTable[path][0] = not self.FieldAreaTable[path][0]
