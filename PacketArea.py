import gi
import Protocol
import re
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class PacketArea(Gtk.Box):

    def __init__(self,main):

        Gtk.Box.__init__(self,orientation=Gtk.Orientation.VERTICAL,spacing=0)
    #Start of Packet area
        PacketLabelBox = Gtk.Box(spacing=0)
        PacketAreaLabel = Gtk.Label("Packet Area")
        self.pack_start(PacketAreaLabel, False, False, 0)
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

        self.PacketNumber = {}
        self.PacketsDisplay = {}
        self.ProtocolsDisplay = {}

        ScrollBarPackets  = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        # ScrollBarPackets.set_border_width(10)
        ScrollBarPackets.set_policy(
            Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)



        # self.FieldAreaTable.append(None,["Frame 1:eth,geninfo,icmpv6,ipv6",0,0])
        # self.FieldAreaTable.append([False,"Frame 767:frame, eth, ip, tcp",2])
        # self.FieldAreaTable.append([False,"Frame 768:frame, eth, ip, tcp",3])

        self.TableView = Gtk.TreeView(self.FieldAreaTable)

        # self.TableView.set_search_equal_func(self.getResults)
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

        buttonRow = Gtk.ListBoxRow()
        button = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        buttonRow.add(button)

        RemoveButton = Gtk.Button(label="Remove")
        #TableBox.pack_start(RemoveButton,True,True,0)

        ClearButton = Gtk.Button(label="Clear")
        #TableBox.pack_start(ClearButton,True,True,0)

        button.pack_start(RemoveButton, True, True, 0)
        button.pack_start(ClearButton, True, True, 0)

        PDMLBox.pack_start(ScrollBarPackets,True,True,0)
        # PDMLBox.pack_start(TableBox,True,False,4)
        self.add(PDMLBox)
        self.add(buttonRow)

        # PDMLBox.pack_start(TableBox,True,False,4)
    #End of Packet area

    def postPackets(self,DataList):
        self.PacketNumber = DataList[0]
        self.PacketsDisplay = DataList[1]
        packetNumber = 0
        self.ProtocolsDisplay = DataList[2]
        print("Posting packets..")

        for Packet in self.PacketNumber.values():
            PacketParent = self.FieldAreaTable.append(None,[self.getFrameProtocols(self.PacketsDisplay[Packet]),0,packetNumber])
            for Protocol in self.PacketsDisplay[Packet]:
                self.FieldAreaTable.append(PacketParent,[Protocol.showname,int(Protocol.size),packetNumber])
            packetNumber +=1


    # for ProtocolList in self.PacketsDisplay.values():
    #     PacketParent = self.FieldAreaTable.append(None,[self.getFrameProtocols(ProtocolList),0,packetNumber])
    #     for Protocol in ProtocolList.keys():
    #         self.FieldAreaTable.append(PacketParent,[Protocol.showname,int(Protocol.size),packetNumber])
    #     packetNumber +=1
        # for ProtocolList in self.PacketsDisplay.values():


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
        self.improvedSearch(data)


    def deletePacket(self):
        selectedPacket= self.TableView.get_selection()
        Packet,tupleVal = selectedPacket.get_selected_rows()
        treeVal = Packet.get_iter(tupleVal)
        PacketValue = Packet.get_value(treeVal,0)
        CheckPacket = PacketValue.split(':')[0]
        CheckFrame = PacketValue.split(" ")
        print(CheckFrame)
        if(CheckFrame[0] == "Frame"):
            self.FieldAreaTable.remove(treeVal)
            PacketDelNumber = PacketValue.split(':')[0]
            PacketDelNumber = PacketDelNumber.split(" ")[1]
            PacketDelNumber = int(PacketDelNumber)
            PacketToDelete = self.PacketNumber[PacketDelNumber]
            self.PacketNumber.pop(PacketDelNumber,None)
            self.PacketsDisplay.pop(PacketToDelete,None)
            self.ProtocolsDisplay.pop(PacketToDelete,None)


    def improvedSearch(self,filterValue):
        data = filterValue.get_text()
        self.FieldAreaTable.clear()
        packetAttached = False
        packetNumber = 0
        for Packet in self.PacketNumber.values():
            packetAttached = False
            for Protocol in self.PacketsDisplay[Packet]:
                for key,value in Protocol.__dict__.items():
                        if(packetAttached == False):
                            if(re.search(str(data),str(key)) or re.search(str(data),str(value))):
                                PacketParent = self.FieldAreaTable.append(None,[self.getFrameProtocols(self.PacketsDisplay[Packet]),0,packetNumber])
                                self.FieldAreaTable.append(PacketParent,[Protocol.showname,int(Protocol.size),packetNumber])
                                packetAttached = True
                                break
                        for Field in self.ProtocolsDisplay[Protocol]:
                            if(packetAttached == False):
                                for key,value in Field.__dict__.items():
                                    if(re.search(str(data),str(key)) or re.search(str(data),str(value))):
                                        print("Found a match")
                                        PacketParent = self.FieldAreaTable.append(None,[self.getFrameProtocols(self.PacketsDisplay[Packet]),0,packetNumber])
                                        self.FieldAreaTable.append(PacketParent,[Protocol.showname,int(Protocol.size),packetNumber])
                                        packetAttached = True
                                        break

            packetNumber +=1



    def clearPackets(self):
        self.FieldAreaTable.clear()

    def clearFilter(self):
        packetNumber=0
        self.FieldAreaTable.clear()
        for Packet in self.PacketNumber.values():
            PacketParent = self.FieldAreaTable.append(None,[self.getFrameProtocols(self.PacketsDisplay[Packet]),0,packetNumber])
            for Protocol in self.PacketsDisplay[Packet]:
                self.FieldAreaTable.append(PacketParent,[Protocol.showname,int(Protocol.size),packetNumber])
            packetNumber += 1



    def on_cell_toggled(self, widget, path):
        self.FieldAreaTable[path][0] = not self.FieldAreaTable[path][0]
