import gi
import Protocol
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class PacketArea(Gtk.Box):

    def __init__(self,main):

        Gtk.Box.__init__(self,orientation=Gtk.Orientation.VERTICAL,spacing=0)
    #Start of Packet area
        PacketLabelBox = Gtk.Box(spacing=0)
        PacketAreaLabel = Gtk.Label("Packet Area")
        # PacketLabelBox.pack_start(PacketAreaLabel,False,False,0)
        self.main = main
        PDMLBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        PDMLBox.pack_start(PacketLabelBox,True,True,0)

        PacketBox = Gtk.Box(spacing=0)

        PacketLabel = Gtk.Label("Packet")
        PacketBox.pack_start(PacketLabel,True,True,0)

        FieldAreaBox = Gtk.Box()

        # self.FieldAreaTable = Gtk.ListStore(Gtk.CheckButton,int)
        self.FieldAreaTable = Gtk.TreeStore(str,int,int)

        ScrollBarPackets  = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        # ScrollBarPackets.set_border_width(10)
        ScrollBarPackets.set_policy(
            Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)



        # self.FieldAreaTable.append([False,"Frame 718:frame, eth, ip, tcp",1])
        # self.FieldAreaTable.append([False,"Frame 767:frame, eth, ip, tcp",2])
        # self.FieldAreaTable.append([False,"Frame 768:frame, eth, ip, tcp",3])

        self.TableView = Gtk.TreeView(self.FieldAreaTable)

        self.TableView.set_search_equal_func(self.getResults)
        self.TableView.set_search_column(1)

        FieldAreaFrame= Gtk.Frame()
        FieldAreaBox.add(FieldAreaFrame)

        TableBox = Gtk.Box(spacing=0)

        # renderer_toggle = Gtk.CellRendererToggle()
        # renderer_toggle.connect("toggled", self.on_cell_toggled)
        # column_toggle = Gtk.TreeViewColumn("", renderer_toggle, active=0)
        # self.TableView.append_column(column_toggle)

        Render_Name = Gtk.CellRendererText()
        FirstColumn = Gtk.TreeViewColumn("Package Name",Render_Name,text=0)
        self.TableView.append_column(FirstColumn)

        Render_Showname= Gtk.CellRendererText()
        Render_Showname.set_property("editable",True)
        # Render_Showname.connect("edited",self.showName_edited)
        SecondColumn = Gtk.TreeViewColumn("Size",Render_Showname,text=1)
        self.TableView.append_column(SecondColumn)

        ScrollBarPackets.add_with_viewport(self.TableView)

        # self.add(ScrollBarPackets)

        TableBox.pack_start(self.TableView,False,False,0)
        FieldAreaBox.pack_start(TableBox,False,False,0)


        RemoveButton = Gtk.Button(label="Remove")
        TableBox.pack_start(RemoveButton,True,True,0)

        ClearButton = Gtk.Button(label="Clear")
        TableBox.pack_start(ClearButton,True,True,0)

        PDMLBox.pack_start(ScrollBarPackets,True,True,0)
        # PDMLBox.pack_start(TableBox,True,False,4)
        self.add(PDMLBox)

        # PDMLBox.pack_start(TableBox,True,False,4)
    #End of Packet area

    def postPackets(self,DataList):
        PacketNumber = DataList[0]
        PacketsDisplay = DataList[1]
        packetNumber = 0
        ProtocolsDisplay = DataList[2]
        print("Posting packets..")

        for Packet in PacketNumber.values():
            PacketParent = self.FieldAreaTable.append(None,[self.getFrameProtocols(PacketsDisplay[Packet]),0,packetNumber])
            for Protocol in PacketsDisplay[Packet]:
                self.FieldAreaTable.append(PacketParent,[Protocol.showname,int(Protocol.size),packetNumber])
            packetNumber +=1


    # for ProtocolList in PacketsDisplay.values():
    #     PacketParent = self.FieldAreaTable.append(None,[self.getFrameProtocols(ProtocolList),0,packetNumber])
    #     for Protocol in ProtocolList.keys():
    #         self.FieldAreaTable.append(PacketParent,[Protocol.showname,int(Protocol.size),packetNumber])
    #     packetNumber +=1
        # for ProtocolList in PacketsDisplay.values():


        print("Packets Posted!")

    def getFrameProtocols(self,ProtocolList):
        FrameNumber=""
        protocolNames = ""
        for Proto in ProtocolList.keys():
            if(Proto.name == "frame"):
                FrameNumber = Proto.showname
                FrameNumber = FrameNumber.split(':')[0]
                FrameNumber += ":"
            else:
                protocolNames += Proto.name + ","
        protocolNames = protocolNames[:-1]
        return FrameNumber + protocolNames


    def filterResults(self,data):
        # print("ha" + data + " it actually works")
        self.TableView.set_search_entry(data)
        print('lol wut')

    def getResults(self, model, column, Data, Rows):
        row = model[Rows]
        if Data in list(row)[column-1].lower():
            return False
        for inner in row.iterchildren():
            if Data in list(inner)[column-1].lower():
                self.TableView.expand_to_path(row.path)
                break
        else:
             self.TableView.collapse_row(row.path)
        return True # Search does not match
    # def filterResults(self):
        # filterToApply =

    # def postPackets(self,DataList):
    #     PacketsDisplay = DataList[0]
    #     ProtocolsDisplay = DataList[1]
    #     print("Posting packets..")
    #     for ProtocolList in PacketsDisplay.values():
    #         for Protocol,Fields in ProtocolList.items():
    #             protocolParent = self.FieldAreaTable.append(None,[str(Protocol.showname),int(Protocol.size)])
    #             for Field in Fields:
    #                 self.FieldAreaTable.append(protocolParent,[Field.showname,int(Field.size)])
    #     print("Packets Posted!")

    def on_cell_toggled(self, widget, path):
        self.FieldAreaTable[path][0] = not self.FieldAreaTable[path][0]
