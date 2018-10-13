import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class LabelWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Network Traffic Based Software Generation")

        mainGrid = Gtk.Grid()
        self.add(mainGrid)

    #Start of Header
        HeaderBox = Gtk.Box(spacing=1)
        mainGrid.attach(HeaderBox,0,0,3,1)

        HeaderFrame = Gtk.Frame()
        HeaderBox.add(HeaderFrame)

        label = Gtk.Label("Network Traffic Based Software Generation")
        HeaderBox.pack_start(label,True,True,0)

        CreateSessionButton = Gtk.Button(label="Create Session")
        HeaderBox.pack_start(CreateSessionButton,True,True,0)

        OpenSessionButton = Gtk.Button(label="Open Session")
        HeaderBox.pack_start(OpenSessionButton,True,True,0)

        CloseSessionButton = Gtk.Button(label="Close Session")
        HeaderBox.pack_start(CloseSessionButton,True,True,0)

        SwitchWorkspaceButton = Gtk.Button(label="Switch Workspace")
        HeaderBox.pack_start(SwitchWorkspaceButton,True,True,0)

        OpenPCAPButton = Gtk.Button(label= "Open PCAP")
        HeaderBox.pack_start(OpenPCAPButton,True,True,0)

        OpenTerminalButton = Gtk.Button("Terminal")
        HeaderBox.pack_start(OpenTerminalButton,True,True,0)
    #End of Header

    #Image Containing the status.
        StatusIndicator = Gtk.Image.new_from_file ("statusIndicator.png")
        StatusFrame = Gtk.Frame()
        StatusBox = Gtk.Box(spacing=0)
        StatusBox.add(StatusFrame)
        mainGrid.attach(StatusBox,0,1,3,1)
        StatusBox.pack_start(StatusIndicator,False,True,0)
    #End of Image containing the Status.

    #Start of Sessions View
        SessionsBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        FolderImage = Gtk.Image.new_from_file ("folder.png")

        mainGrid.attach(SessionsBox,0,2,1,1)
        WorkspaceBox = Gtk.Box()

        # WorkspaceBox.pack_start(FolderImage,False,False,0)
        Workspace = Gtk.Label("Workspace Kobra")
        WorkspaceBox.pack_start(Workspace,False,False,0)

        SessionA = Gtk.Box(spacing=0)
        SessionA.pack_start(FolderImage,False,False,0)
        SessionALabel = Gtk.Label("Session A \n -State1 \n  -State 2")
        SessionA.pack_start(SessionALabel,False,False,0)

        FolderImage = Gtk.Image.new_from_file ("folder.png")
        SessionB = Gtk.Box(spacing=0)
        SessionB.pack_start(FolderImage,False,False,0)
        SessionBLabel = Gtk.Label("Session B")
        SessionB.pack_start(SessionBLabel,False,False,0)

        FolderImage = Gtk.Image.new_from_file ("folder.png")
        SessionC = Gtk.Box(spacing=0)
        SessionC.pack_start(FolderImage,False,False,0)
        SessionCLabel = Gtk.Label("Session C")
        SessionC.pack_start(SessionCLabel,False,False,0)

        SessionsFrame = Gtk.Frame()
        SessionsBox.add(SessionsFrame)

        SessionsViewLabel = Gtk.Label()
        SessionsViewLabel.set_text("Session View")
        SessionsBox.pack_start(SessionsViewLabel,False,False,0)
        SessionsBox.pack_start(WorkspaceBox,False,False,0)
        SessionsBox.pack_start(SessionA,False,False,0)
        SessionsBox.pack_start(SessionB,False,False,0)
        SessionsBox.pack_start(SessionC,False,False,0)
    #End of Sessions View

    #Start of PDML View
        PDMLFrame = Gtk.Frame()
        PDMLBox = Gtk.Box(spacing=0)
        mainGrid.attach(PDMLBox,1,2,2,1)
        PDMLBox.add(PDMLFrame)
        PDMLLabel = Gtk.Label("PDML View")
        PDMLLabel.set_text("PDML View")
        PDMLBox.pack_start(PDMLLabel,False,False,0)


    #End of PDML View

    #Start of Tagging View
        TagBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=0)
        mainGrid.attach(TagBox,0,3,1,1)

        TagFrame= Gtk.Frame()
        TagBox.add(TagFrame)

        TagLabel = Gtk.Label("Tag Area")
        TagLabel.set_text("Tag Area")
        TagBox.pack_start(TagLabel,False,False,0)


        #First text box of Tag area.
        SavedBox = Gtk.Box(spacing=3)
        SavedTag= Gtk.Label("Saved Tag")
        SavedTag.set_text("Saved Tag")
        SavedBox.pack_start(SavedTag,False,False,0)
        SavedTagArea = Gtk.Entry()
        SavedBox.pack_start(SavedTagArea,False,False,0)
        TagBox.pack_start(SavedBox,False,False,0)
        #End of first text box

        #Start of Second Text Box
        TagNameBox = Gtk.Box(spacing=3)
        TagNameLabel = Gtk.Label("Tag Name")
        TagNameLabel.set_text("Tag Name")
        TagNameBox.pack_start(TagNameLabel,False,False,0)
        TagNameInput = Gtk.Entry()
        TagNameBox.pack_start(TagNameInput,False,False,0)
        TagBox.pack_start(TagNameBox,False,False,0)
        #End of second text box

        #Start of Third Text Box
        TaggedFieldBox = Gtk.Box(spacing=3)
        TaggedFieldLabel = Gtk.Label("Tagged Field")
        TaggedFieldLabel.set_text("Tagged Field")
        TaggedFieldBox.pack_start(TaggedFieldLabel,False,False,0)
        TaggedFieldInput = Gtk.Entry()
        TaggedFieldBox.pack_start(TaggedFieldInput,False,False,0)
        TagBox.pack_start(TaggedFieldBox,False,False,0)
        #End of Third Text Box

        #Start of fourth and final box.
        TagDescriptionBox= Gtk.Box(spacing=3)
        TagDescriptionLabel= Gtk.Label("Tag Description")
        TagDescriptionLabel.set_text("Tag Description")
        TagDescriptionBox.pack_start(TagDescriptionLabel,False,False,0)
        TagDescriptionInput = Gtk.Entry()
        TagDescriptionBox.pack_start(TagDescriptionInput,False,False,0)
        TagBox.pack_start(TagDescriptionBox,False,False,0)
        #End of fourth box.

        #Buttons to submit or cancel.
        SubmitCancelBox = Gtk.Box(spacing=10)
        SubmitTagButton = Gtk.Button(label="Update")
        CancelTagButton = Gtk.Button(label="Cancel")
        SubmitCancelBox.pack_start(SubmitTagButton,False,False,0)
        SubmitCancelBox.pack_start(CancelTagButton,False,False,0)
        TagBox.pack_start(SubmitCancelBox,False,False,0)
        #End of Buttons to submit or cancel.
    #End of Tagging View

    #Start of field area View
        FieldAreaBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=1)
        mainGrid.attach(FieldAreaBox,1,3,1,1)
        self.FieldAreaTable = Gtk.ListStore(str,str,int,int,str,str,int)


        FieldAreaFrame= Gtk.Frame()
        FieldAreaBox.add(FieldAreaFrame)

        TableBox = Gtk.Box(spacing=0)


        self.FieldAreaTable.append(["icmp.type","Type 8 [Echo ping request]" , 1, 34, "8", "8", 2])
        self.FieldAreaTable.append(["icmp.code","Code 0" , 1, 35, "00", "0", 2])
        self.FieldAreaTable.append(["icmp.checksum","Checksum: 0x6861 [Correct]" , 0, 36, "0x6861", "6861", 0])
        self.FieldAreaTable.append(["icmp.Ident","Identifier: 0x809e" , 2, 38, "0x809e", "809e", 2])
        self.FieldAreaTable.append(["icmp.seq","Sequence number: 0x0f00" , 2, 40, "0x0f00", "0f00", 2])

        Render_Name = Gtk.CellRendererText()
        Render_Name.set_property("editable",True)
        Render_Showname= Gtk.CellRendererText()
        Render_Showname.set_property("editable",True)
        Render_Size= Gtk.CellRendererText()
        Render_Size.set_property("editable",True)
        Render_Position= Gtk.CellRendererText()
        Render_Show = Gtk.CellRendererText()
        Render_Value = Gtk.CellRendererText()
        Render_Value.set_property("editable",True)
        Render_Entropy = Gtk.CellRendererText()

        TableView = Gtk.TreeView(self.FieldAreaTable)

        FirstColumn = Gtk.TreeViewColumn("Field Name",Render_Name,text=0)
        SecondColumn = Gtk.TreeViewColumn("Show Name",Render_Showname,text=1)
        ThirdColumn = Gtk.TreeViewColumn("Size",Render_Size,text=2)
        FourthColumn = Gtk.TreeViewColumn("Position",Render_Position,text=3)
        FifthColumn = Gtk.TreeViewColumn("Show",Render_Show,text=4)
        SixthColumn = Gtk.TreeViewColumn("Value",Render_Value,text=5)
        SeventhColumn = Gtk.TreeViewColumn("Entropy",Render_Entropy,text=6)

        TableView.append_column(FirstColumn)
        TableView.append_column(SecondColumn)
        TableView.append_column(ThirdColumn)
        TableView.append_column(FourthColumn)
        TableView.append_column(FifthColumn)
        TableView.append_column(SixthColumn)
        TableView.append_column(SeventhColumn)

        Render_Name.connect("edited",self.name_edited)
        Render_Showname.connect("edited",self.showName_edited)
        Render_Size.connect("edited",self.size_edited)
        Render_Value.connect("edited",self.value_edited)

        TableBox.pack_start(TableView,False,False,0)

        FieldAreaLabel = Gtk.Label("Field Area")
        FieldAreaLabel.set_text("Field Area")
        FieldAreaBox.pack_start(FieldAreaLabel,False,False,0)
        FieldBottomBox = Gtk.Box(spacing=10)
        SelectFieldBox = Gtk.CheckButton(label="Select all fields")
        EditFields = Gtk.Label("Field Name, Showname , Value and Length are editable fields.")
        FieldBottomBox.pack_start(SelectFieldBox,False,False,0)
        FieldBottomBox.pack_start(EditFields,False,False,0)
        FieldAreaBox.pack_start(TableBox,False,False,0)
        FieldAreaBox.pack_start(FieldBottomBox,False,False,0)
    #End of Field area views.

    #Start of Message Type View
        MessageTypeBox = Gtk.Box(spacing=1)
        mainGrid.attach(MessageTypeBox,2,3,1,1)

        MessageTypeFrame = Gtk.Frame()
        MessageTypeBox.add(MessageTypeFrame)

        MessageTypeTabs = Gtk.Notebook()

        MessageTypeArea = Gtk.Label("Message Type Area")
        MessageTypeArea.set_text("Message Type")
        MessageTypeBox.pack_start(MessageTypeArea,False,True,0)
    #End of Message Type View

    def name_edited(self, widget, path, text):
        self.FieldAreaTable[path][0] = text
    def showName_edited(self, widget, path, text):
        self.FieldAreaTable[path][1] = text
    def size_edited(self, widget, path, text):
        self.FieldAreaTable[path][2] = int(text)
    def value_edited(self, widget, path, text):
        self.FieldAreaTable[path][5] = text


window = LabelWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
