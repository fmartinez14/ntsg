import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class TagArea(Gtk.Box):

	TagBox = Gtk.Box()
	_fields = list()
	_buttons = list()
	
	def __init__(self,):
		TagBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=0)
		
		TagLabel = Gtk.Label("Tag Area")
		TagBox.pack_start(TagLabel,False,False,0)

	def addField(self, label):
		fieldBox = Gtk.Box(spacing=3)
		fieldTitle = Gtk.Label(label)
		fieldBox.pack_start(fieldTitle,False,False,0)
		fieldValue = Gtk.Entry()
		fieldBox.pack_start(fieldValue,False,False,0)
		self._fields.append(fieldBox)

	def showFields(self):
		fs = self._fields
		for x in range(len(fs)):
			self.TagBox.pack_start(fs[x],False,False,0)

	def addButton(self, name):
		newButton = Gtk.Button(label=name)
		self._buttons.append(newButton)

	def showButtons(self):
		buttonBox = Gtk.Box(spacing=10)
		for x in range(len(self._buttons)):
			buttonBox.pack_start(self._buttons[x],False,False,0)
