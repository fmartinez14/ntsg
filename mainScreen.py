import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class LabelWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Label Example")


        mainGrid = Gtk.Grid()
        self.add(mainGrid)

    #Start of Header
        HeaderBox = Gtk.Box(spacing=1)
        mainGrid.attach(HeaderBox,0,0,1,1)

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
        StatusBox = Gtk.Box(spacing=1)
        mainGrid.attach(StatusBox,0,1,1,1)
        StatusBox.pack_start(StatusIndicator,True,True,0)
    #End of Image containing the Status.

    #Start of Sessions View
        SessionsBox = Gtk.Box(spacing=0)
        mainGrid.attach(SessionsBox,0,2,1,1)

        SessionsViewLabel = Gtk.Label()
        SessionsViewLabel.set_text("Sessions View")
        SessionsBox.pack_start(SessionsViewLabel,False,False,0)
    #End of Sessions View

    #Start of PDML View
        PDMLBox = Gtk.Box(spacing=0)
        mainGrid.attach(PDMLBox,1,2,1,1)

        PDMLLabel = Gtk.Label("PDML View")
        PDMLLabel.set_text("PDML View")
        PDMLBox.pack_start(PDMLLabel,False,False,0)
    #End of PDML View

    #Start of Tagging View
        TagBox = Gtk.Box(spacing=2)
        mainGrid.attach(TagBox,0,3,1,1)

        TagLabel = Gtk.Label("Tag Label")
        TagLabel.set_text("Tag Label")
        TagBox.pack_start(TagLabel,False,False,0)
    #End of Tagging View

    #Start of field area View
        FieldAreaBox = Gtk.Box(spacing=2)
        mainGrid.attach(FieldAreaBox,1,3,1,1)

        FieldAreaLabel = Gtk.Label("Field Area")
        FieldAreaLabel.set_text("Field Area")
        FieldAreaBox.pack_start(FieldAreaLabel,False,True,10)
    #End of Field area views.

    #Start of Message Type View
        MessageTypeBox = Gtk.Box(spacing=2)
        mainGrid.attach(MessageTypeBox,2,3,1,1)

        MessageTypeArea = Gtk.Label("Message Type Area")
        MessageTypeArea.set_text("Message Type")
        MessageTypeBox.pack_start(MessageTypeArea,False,True,0)
    #End of Message Type View


window = LabelWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
