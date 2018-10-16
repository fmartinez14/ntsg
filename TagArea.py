import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class TagArea(Gtk.Box):

	_fields = list()
	_buttons = list()
	
	def __init__(self):
		Gtk.Box.__init__(self,orientation=Gtk.Orientation.VERTICAL,spacing=0)

		TagLabel = Gtk.Label("Tag Area")
		self.pack_start(TagLabel,False,False,0)

		TagAreaFrame = Gtk.Frame()
		TagAreaFrame.set_shadow_type(Gtk.ShadowType.IN)
		self.add(TagAreaFrame)

	def addField(self, label):
		fieldBox = Gtk.Box(spacing=3)
		fieldTitle = Gtk.Label(label)
		fieldBox.pack_start(fieldTitle,False,False,0)
		fieldValue = Gtk.Entry()
		fieldBox.pack_end(fieldValue,False,False,0)
		self._fields.append(fieldBox)

	def showFields(self):
		FieldGrid = Gtk.Grid()
		for x in range(len(self._fields)):
			FieldGrid.attach(self._fields[x],0,(x-1),2,1)
		self.pack_start(FieldGrid,False,False,0)

	def addButton(self, name):
		newButton = Gtk.Button(label=name)
		self._buttons.append(newButton)

	def showButtons(self):
		buttonBox = Gtk.Box(spacing=10)
		for x in range(len(self._buttons)):
			buttonBox.pack_start(self._buttons[x],False,False,0)
		self.pack_end(buttonBox,False,False,36)
