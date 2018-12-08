import gi
import parsePDML
import os

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Header(Gtk.Box):
    _buttons = list()
    PCAPWidget = ""
    DataPCAP = []

    def __init__(self, main, labelString='New Header'):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.HORIZONTAL)
        self.main = main
        self.PDMLLocation = ""
        HeaderFrame = Gtk.Frame()
        HeaderFrame.set_shadow_type(Gtk.ShadowType.IN)
        self.add(HeaderFrame)

        self.set_baseline_position(Gtk.BaselinePosition.CENTER)

        label = Gtk.Label(labelString)
        self.pack_start(label, True, True, 3)

    def addButton(self, newLabel='New Button'):
        NewButton = Gtk.Button(label=newLabel)
        self._buttons.append(NewButton)

    def showButtons(self):
        for x in range(len(self._buttons)):
            self.pack_end(self._buttons[x], True, True, 3)

    def PCAP_clicked(self, widget):
        from openPCAPoverlay import openPCAPwindow
        PCAPWidget = openPCAPwindow(self)
        PCAPWidget.show_all()
        PCAPWidget.connect("destroy", self.parsePackets)

    def OpenSession_clicked(self, widget):
        from openSessionOverlay import openSessionwindow
        SessionWidget = openSessionwindow()
        SessionWidget.show_all()

    def NewSession_clicked(self, widget):
        from newSessionsOverlay import ListBoxWindow
        SessionWidget = ListBoxWindow()
        SessionWidget.show_all()

    def StateMachine_clicked(self, widget):
        from stateMachine import stateMachineWindow
        window = stateMachineWindow()
        window.show_all()

    def Workspace_clicked(self, widget):
        from launcherOverlay import launcherOverlayWindow
        LauncherWidget = launcherOverlayWindow()
        LauncherWidget.show_all()

    def Terminal_clicked(self, widget):
        from terminalOverlay import openTerminalwindow
        TerminalWidget = openTerminalwindow()
        TerminalWidget.show_all()

    def parsePackets(self, widget):
        # try:
        # if(self.PDMLLocation != ""):

        DataFile = parsePDML.makePackets(self.PDMLLocation)
        # parsePDML.printPackets(DataFile[0],DataFile[1])
        print("sending to main screen")
        self.main.recievePackets(DataFile)
# except:
# 	pass

# def PCAP_clicked(self, widget):
# 	   from openPCAPoverlay import openPCAPwindow
# 	   PCAPWidget = openPCAPwindow()
#    	   PCAPWidget.show_all()
