import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from Header import Header
from Session import Session
from TagArea import TagArea
from FieldArea import FieldArea


class LabelWindow(Gtk.Window):

	#screenWidth = 100
	#screenHeigth = 45

    def __init__(self):
        Gtk.Window.__init__(self, title="Network Traffic Based Software Generation")
        # screenWidth = Gdk.Screen.get_width(Gdk.Screen.get_default())
        # screenHeigth = Gdk.Screen.get_height(Gdk.Screen.get_default())
        # Gtk.Window.resize(self,screenWidth/10,screenHeigth/3)

        mainGrid = Gtk.Grid()
        mainGrid.set_column_spacing(4)
        mainGrid.set_row_spacing(4)
        mainGrid.set_row_homogeneous(False)
        mainGrid.set_hexpand(False)

        for x in range(4):
        	mainGrid.set_row_baseline_position(x,Gtk.BaselinePosition.CENTER)

   #Start of Header
    	HeaderBox = Header("Network Traffic Based Software Generation")

    	HeaderBox.addButton("Create Session")
    	HeaderBox.addButton("Open Session")
    	HeaderBox.addButton("Close Session")
    	HeaderBox.addButton("Open Session")
    	HeaderBox.addButton("Switch Workspace")
    	HeaderBox.addButton("Open PCAP")
    	HeaderBox.addButton("Terminal")
    	HeaderBox.showButtons()

    	mainGrid.attach(HeaderBox,0,0,4,1)
    #End of Header

    #Image Containing the status.
    	StatusIndicator = Gtk.Image.new_from_file ("statusIndicator.png")
        StatusFrame = Gtk.Frame()
        StatusBox = Gtk.Box(spacing=0)
        StatusBox.add(StatusFrame)
        mainGrid.attach(StatusBox,0,1,4,1)
        StatusBox.pack_start(StatusIndicator,False,True,0)
    #End of Image containing the Status.
    	
    #Start of Sessions View
        SessionsBox = Session()
        SessionsBox.addSession("Session A")
        SessionsBox.addSession("Session B")
        SessionsBox.addSession("Session C")
        SessionsBox.showSessions()

        mainGrid.attach(SessionsBox,0,2,1,1)
	#End of Sessions View
    	
    #Start of PDML View
        PDMLFrame = Gtk.Frame()
        PDMLBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=0)
        PDMLBox.add(PDMLFrame)
        PDMLLabel = Gtk.Label("PDML View")
        PDMLLabel.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse("light blue"))
        PDMLBox.pack_start(PDMLLabel,False,False,0)
        mainGrid.attach(PDMLBox,1,2,3,1)
    #End of PDML View

    #Start of Tagging View
        TagBox = TagArea()
        TagBox.addField("Saved Tag")
        TagBox.addField("Tag Name")
        TagBox.addField("Tagged Field")
        TagBox.addField("Tag Description")
        TagBox.showFields()

        TagBox.addButton("Update")
        TagBox.addButton("Cancel")
        TagBox.showButtons()

        mainGrid.attach(TagBox,0,3,1,1)
    #End of Tagging View

    #Start of field area View
        FieldAreaBox = FieldArea()
        mainGrid.attach(FieldAreaBox,1,3,1,1)

        FieldAreaBox.addField("icmp.type","Type 8 [Echo ping request]" , 1, 34, "8", "8", 2)
        FieldAreaBox.addField("icmp.code","Code 0" , 1, 35, "00", "0", 2)
        FieldAreaBox.addField("icmp.checksum","Checksum: 0x6861 [Correct]" , 0, 36, "0x6861", "6861", 0)
        FieldAreaBox.addField("icmp.Ident","Identifier: 0x809e" , 2, 38, "0x809e", "809e", 2)
        FieldAreaBox.addField("icmp.seq","Sequence number: 0x0f00" , 2, 40, "0x0f00", "0f00", 2)
        self.add(mainGrid)
 #        self.FieldAreaTable = Gtk.ListStore(str,str,int,int,str,str,int)


 #        FieldAreaFrame= Gtk.Frame()
 #        FieldAreaBox.add(FieldAreaFrame)

 #        TableBox = Gtk.Box(spacing=0)


 #        self.FieldAreaTable.append(["icmp.type","Type 8 [Echo ping request]" , 1, 34, "8", "8", 2])
 #        self.FieldAreaTable.append(["icmp.code","Code 0" , 1, 35, "00", "0", 2])
 #        self.FieldAreaTable.append(["icmp.checksum","Checksum: 0x6861 [Correct]" , 0, 36, "0x6861", "6861", 0])
 #        self.FieldAreaTable.append(["icmp.Ident","Identifier: 0x809e" , 2, 38, "0x809e", "809e", 2])
 #        self.FieldAreaTable.append(["icmp.seq","Sequence number: 0x0f00" , 2, 40, "0x0f00", "0f00", 2])

 #        Render_Name = Gtk.CellRendererText()
 #        Render_Name.set_property("editable",True)
 #        Render_Showname= Gtk.CellRendererText()
 #        Render_Showname.set_property("editable",True)
 #        Render_Size= Gtk.CellRendererText()
 #        Render_Size.set_property("editable",True)
 #        Render_Position= Gtk.CellRendererText()
 #        Render_Show = Gtk.CellRendererText()
 #        Render_Value = Gtk.CellRendererText()
 #        Render_Value.set_property("editable",True)
 #        Render_Entropy = Gtk.CellRendererText()

 #        TableView = Gtk.TreeView(self.FieldAreaTable)

 #        FirstColumn = Gtk.TreeViewColumn("Field Name",Render_Name,text=0)
 #        SecondColumn = Gtk.TreeViewColumn("Show Name",Render_Showname,text=1)
 #        ThirdColumn = Gtk.TreeViewColumn("Size",Render_Size,text=2)
 #        FourthColumn = Gtk.TreeViewColumn("Position",Render_Position,text=3)
 #        FifthColumn = Gtk.TreeViewColumn("Show",Render_Show,text=4)
 #        SixthColumn = Gtk.TreeViewColumn("Value",Render_Value,text=5)
 #        SeventhColumn = Gtk.TreeViewColumn("Entropy",Render_Entropy,text=6)

 #        TableView.append_column(FirstColumn)
 #        TableView.append_column(SecondColumn)
 #        TableView.append_column(ThirdColumn)
 #        TableView.append_column(FourthColumn)
 #        TableView.append_column(FifthColumn)
 #        TableView.append_column(SixthColumn)
 #        TableView.append_column(SeventhColumn)

        # Render_Name.connect("edited",self.name_edited)
        # Render_Showname.connect("edited",self.showName_edited)
        # Render_Size.connect("edited",self.size_edited)
        # Render_Value.connect("edited",self.value_edited)

 #        TableBox.pack_start(TableView,False,False,0)

 #        FieldAreaLabel = Gtk.Label("Field Area")
 #        FieldAreaLabel.set_text("Field Area")
    #     FieldAreaBox.pack_start(FieldAreaLabel,False,False,0)
    #     FieldBottomBox = Gtk.Box(spacing=10)
    #     SelectFieldBox = Gtk.CheckButton(label="Select all fields")
    #     EditFields = Gtk.Label("Field Name, Showname , Value and Length are editable fields.")
    #     FieldBottomBox.pack_start(SelectFieldBox,False,False,0)
    #     FieldBottomBox.pack_start(EditFields,False,False,0)
    #     FieldAreaBox.pack_start(TableBox,False,False,0)
    #     FieldAreaBox.pack_start(FieldBottomBox,False,False,0)
    # #End of Field area views.

    #Start of Message Type View
        MessageTypeBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=0)
        mainGrid.attach(MessageTypeBox,2,3,2,1)

        MessageTypeFrame = Gtk.Frame()
        MessageTypeBox.add(MessageTypeFrame)
        #
        #
        #
        #IMPORTANT: Notebook requires all views to be inside a box. This section is all the views until I find a way to have it set up more efficiently.
        #
        #Start of New/Modify
        MessageTypeTabs = Gtk.Notebook()
        NewModifyView = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=0)
        InstructionsLabel= Gtk.Label("To create a new message type, please enter a message type name and select message type field value pair(s). \n To Update/delete an existing message type, please select from the existing message type first \n and the previously selected name and field value pair(s) will be pre-populated.")
        InstructionsLabel.set_line_wrap(True)

        ExistingMessageTypeBox = Gtk.Box(spacing=1)
        ExistingMessageLabel = Gtk.Label("Existing Message Type")
        ExistingMessageTypeBox.pack_start(ExistingMessageLabel,False,False,0)
        ExistingMessageType = Gtk.Entry()
        ExistingMessageTypeBox.pack_start(ExistingMessageType,False,False,0)

        MessageTypeNameBox= Gtk.Box(spacing=2)
        MessageTypeLabel = Gtk.Label("Message Type Name")
        MessageTypeNameBox.pack_start(MessageTypeLabel, False,False,0)
        MessageTypeName= Gtk.Entry()
        MessageTypeNameBox.pack_start(MessageTypeName,False,False,0)

        MessageTypePairsBox = Gtk.Box(spacing=2)
        MessageTypePairsLabel = Gtk.Label("Message Type Field\n Value Pair(s)")
        MessageTypePairsBox.pack_start(MessageTypePairsLabel,False,False,0)
        ValuePairs = Gtk.Entry()
        MessageTypePairsBox.pack_start(ValuePairs,False,False,0)

        NewModifyView.pack_start(InstructionsLabel,False,False,0)
        NewModifyView.pack_start(ExistingMessageTypeBox,False,False,0)
        NewModifyView.pack_start(MessageTypeNameBox,False,False,0)
        NewModifyView.pack_start(MessageTypePairsBox,False,False,0)

        SelectBothField = Gtk.CheckButton(label="Select both field name and value")
        SelectFieldNameOnly = Gtk.CheckButton(label="Select field name only")

        NewModifyView.pack_start(SelectBothField,False,False,0)
        NewModifyView.pack_start(SelectFieldNameOnly,False,False,0)

        OperationButtons = Gtk.Box(spacing=2)
        SaveButtonMessageType = Gtk.Button(label="Save")
        DeleteButtonMessageType= Gtk.Button(label="Delete")
        ClearButtonMessageType= Gtk.Button(label="Clear")
        OperationButtons.pack_start(SaveButtonMessageType,False,False,0)
        OperationButtons.pack_start(DeleteButtonMessageType,False,False,0)
        OperationButtons.pack_start(ClearButtonMessageType,False,False,0)

        NewModifyView.pack_start(OperationButtons,False,False,0)

        MessageTypeTabs.append_page(NewModifyView)
        MessageTypeTabs.set_tab_label_text(NewModifyView,"New/Modify")

        #End of New/Modify
        #Start of Template
        TemplateBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=0)

        ExistingMessageTypebox = Gtk.Box(spacing=0)
        ExistingMessageTypeLabel = Gtk.Label("Existing Message Type")
        ExistingMessageType = Gtk.Entry()
        ExistingMessageTypebox.pack_start(ExistingMessageTypeLabel,False,False,0)
        ExistingMessageTypebox.pack_start(ExistingMessageType,False,False,0)
        TemplateBox.pack_start(ExistingMessageTypebox,False,False,0)


        CycleThroughPackets = Gtk.Button(label="Cycle Through Packets")
        TemplateBox.pack_start(CycleThroughPackets,False,False,0)

        MessageTypeTemplateBox = Gtk.Box(spacing=0)
        MessageTypeTemplateLabel = Gtk.Label("Message Type \n Template Field Value \n Pair(s)")
        PacketArea = Gtk.ListStore(str)
        PacketArea.append(["No packets"])

        PacketView = Gtk.TreeView(PacketArea)


        Render_Packet = Gtk.CellRendererText()
        PacketViewCol = Gtk.TreeViewColumn("Packets",Render_Packet,text=0)
        PacketView.append_column(PacketViewCol) 

        MessageTypeTemplateBox.pack_start(MessageTypeTemplateLabel,False,False,0)
        MessageTypeTemplateBox.pack_start(PacketView,False,False,0)
        TemplateBox.pack_start(MessageTypeTemplateBox,False,False,0)

        OperationButtonsTypeTemplate = Gtk.Box(spacing=2)
        SaveButtonTypeTemplate = Gtk.Button(label="Save")
        ClearButtonTypeTemplate= Gtk.Button(label="Clear")
        OperationButtonsTypeTemplate.pack_start(SaveButtonTypeTemplate,False,False,0)
        OperationButtonsTypeTemplate.pack_start(ClearButtonTypeTemplate,False,False,0)

        TemplateBox.pack_start(OperationButtonsTypeTemplate,False,False,0)

        MessageTypeTabs.append_page(TemplateBox)
        MessageTypeTabs.set_tab_label_text(TemplateBox,"Template")
        #End of Template

        #Start of Equivalency
        EquivalencyBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=0)
        FieldEquivalencyEqualBox = Gtk.Box(spacing=0)

        FieldEquivalencyLabel = Gtk.Label("Field Equivalency")
        FieldName = Gtk.Entry()
        FieldOR = Gtk.Label("OR")
        MessageType = Gtk.Entry()
        FieldEqual = Gtk.Label("=")
        FieldEquivalencyEqualBox.pack_start(FieldEquivalencyLabel,False,False,0)
        FieldEquivalencyEqualBox.pack_start(FieldName,False,False,0)
        FieldEquivalencyEqualBox.pack_start(FieldOR,False,False,0)
        FieldEquivalencyEqualBox.pack_start(MessageType,False,False,0)
        FieldEquivalencyEqualBox.pack_start(FieldEqual,False,False,0)
        EquivalencyBox.pack_start(FieldEquivalencyEqualBox,False,False,0)

        SecondFieldEquivalencyEqualBox= Gtk.Box(spacing=0)
        FieldName = Gtk.Entry()
        FieldOR = Gtk.Label("OR")
        IndentLabel = Gtk.Label("                           ")
        MessageType = Gtk.Entry()
        SecondFieldEquivalencyEqualBox.pack_start(IndentLabel,False,False,0)
        SecondFieldEquivalencyEqualBox.pack_start(FieldName,False,False,0)
        SecondFieldEquivalencyEqualBox.pack_start(FieldOR,False,False,0)
        SecondFieldEquivalencyEqualBox.pack_start(MessageType,False,False,0)
        FieldPLUS= Gtk.Label("+")
        SecondFieldEquivalencyEqualBox.pack_start(FieldPLUS,False,False,0)
        EquivalencyBox.pack_start(SecondFieldEquivalencyEqualBox,False,False,0)

        OperationButtonsEquivalency = Gtk.Box(spacing=2)
        SaveButtonEquivalency = Gtk.Button(label="Save")
        ClearButtonEquivalency= Gtk.Button(label="Clear")
        OperationButtonsEquivalency.pack_start(SaveButtonEquivalency,False,False,0)
        OperationButtonsEquivalency.pack_start(ClearButtonEquivalency,False,False,0)

        EquivalencyBox.pack_start(OperationButtonsEquivalency,False,False,0)

        MessageTypeTabs.append_page(EquivalencyBox)
        MessageTypeTabs.set_tab_label_text(EquivalencyBox,"Equivalency")

        #End of Equivalency

        #Start of Generation
        GenerationBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=0)
        ExistingMessageTypeInGeneration = Gtk.Box(spacing=0)
        ExistingMessageTypeLabel = Gtk.Label("Existing Message Type")
        ExistingMessageTypeInGeneration.pack_start(ExistingMessageTypeLabel,False,False,0)
        MessageTypeName= Gtk.Entry()
        ExistingMessageTypeInGeneration.pack_start(MessageTypeName,False,False,0)

        GenerationBox.pack_start(ExistingMessageTypeInGeneration,False,False,0)

        MessageTemplateFormatBox = Gtk.Box(spacing=0)
        MessageTemplateFormatLabel = Gtk.Label("Message Template \n Output Format")
        MessageTemplateFormat = Gtk.Entry()
        MessageTemplateFormatBox.pack_start(MessageTemplateFormatLabel,False,False,0)
        MessageTemplateFormatBox.pack_start(MessageTemplateFormat,False,False,0)
        GenerationBox.pack_start(MessageTemplateFormatBox,False,False,0)

        MessageTemplateNameBox = Gtk.Box(spacing=0)
        MessageTemplateNameLabel= Gtk.Label("Message Template \n Name")
        MessageTemplateName = Gtk.Entry()
        MessageTemplateNameBox.pack_start(MessageTemplateNameLabel,False,False,0)
        MessageTemplateNameBox.pack_start(MessageTemplateName,False,False,0)
        GenerationBox.pack_start(MessageTemplateNameBox,False,False,0)

        ButtonsMessageType = Gtk.Box(spacing=0)
        GenerateButton = Gtk.Button(label="Generate")
        ClearMessageType = Gtk.Button(label="Clear")
        ButtonsMessageType.pack_start(GenerateButton,False,False,0)
        ButtonsMessageType.pack_start(ClearMessageType,False,False,0)
        GenerationBox.pack_start(ButtonsMessageType,False,False,0)

        MessageTypeTabs.append_page(GenerationBox)
        MessageTypeTabs.set_tab_label_text(GenerationBox,"Generation")
        #End of Generation

        MessageTypeArea = Gtk.Label("Message Type Area")
        MessageTypeArea.set_text("Message Type")

        MessageTypeBox.pack_start(MessageTypeArea,False,False,0)
        MessageTypeBox.pack_start(MessageTypeTabs,False,False,0)
    #End of Message Type View

    # def name_edited(self, widget, path, text):
    #     self.FieldAreaTable[path][0] = text
    # def showName_edited(self, widget, path, text):
    #     self.FieldAreaTable[path][1] = text
    # def size_edited(self, widget, path, text):
    #     self.FieldAreaTable[path][2] = int(text)
    # def value_edited(self, widget, path, text):
    #     self.FieldAreaTable[path][5] = text


window = LabelWindow()
window.set_default_size(200, 300)
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
