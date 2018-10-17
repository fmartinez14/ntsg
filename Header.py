import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Header(Gtk.Box):
	_buttons = list()
	PCAPWidget=""
	def __init__(self, labelString='New Header'):
		Gtk.Box.__init__(self,orientation=Gtk.Orientation.HORIZONTAL)

		HeaderFrame = Gtk.Frame()
		HeaderFrame.set_shadow_type(Gtk.ShadowType.IN)
		self.add(HeaderFrame)

		self.set_baseline_position(Gtk.BaselinePosition.CENTER)

		label = Gtk.Label(labelString)
		self.pack_start(label,True,True,3)

	def addButton(self, newLabel='New Button'):
		NewButton = Gtk.Button(label=newLabel)
		self._buttons.append(NewButton)

	def showButtons(self):
		for x in range(len(self._buttons)):
			self.pack_end(self._buttons[x],True,True,3)

	def PCAP_clicked(self, widget):
		   from openPCAPoverlay import openPCAPwindow
		   PCAPWidget = openPCAPwindow()
	   	   PCAPWidget.show_all()

   	def OpenSession_clicked(self, widget):
   		   from openSessionOverlay import openSessionwindow
   		   SessionWidget = openSessionwindow()
   	   	   SessionWidget.show_all()



   	def Workspace_clicked(self, widget):
   		   from launcherOverlay import launcherOverlayWindow
   		   LauncherWidget = launcherOverlayWindow()
   	   	   LauncherWidget.show_all()

   	def Terminal_clicked(self, widget):
   		   from terminalOverlay import openTerminalwindow
   		   TerminalWidget = openTerminalwindow()
   	   	   TerminalWidget.show_all()

  	# def PCAP_clicked(self, widget):
  	# 	   from openPCAPoverlay import openPCAPwindow
  	# 	   PCAPWidget = openPCAPwindow()
  	#    	   PCAPWidget.show_all()
