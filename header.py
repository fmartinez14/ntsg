import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Header(Gtk.Box):

	HeaderBox = Gtk.Box()
	_buttons = list()

	def __init__(self, labelString='New Header'):
		self.HeaderBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		self.HeaderBox.set_baseline_position(Gtk.BaselinePosition.CENTER)
		self.HeaderBox.set_spacing(4)

	        label = Gtk.Label(labelString)
	        self.HeaderBox.pack_start(label,True,True,3)

		HeaderFrame = Gtk.Frame()
		HeaderFrame.set_shadow_type(Gtk.ShadowType.OUT)
		self.HeaderBox.add(HeaderFrame)

	def get_buttons(self):
		return self._buttons
	buttons = property(get_buttons)

	def addButton(self, newLabel='New Button'):
	        NewButton = Gtk.Button(label=newLabel)
		self._buttons.append(NewButton)

	def showButtons(self):
		btns = self._buttons
		for x in range(len(btns)):
			self.HeaderBox.pack_end(btns[x],False,False,3)

    
