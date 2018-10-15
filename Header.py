import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Header(Gtk.Box):
	_buttons = list()
	
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