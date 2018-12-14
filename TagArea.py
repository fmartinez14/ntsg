import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class TagArea(Gtk.Box):

	_fields = list()
	_buttons = list()
	_tagFields = list()
	_tagDic = dict()


	def __init__(self):
		Gtk.Box.__init__(self,orientation=Gtk.Orientation.VERTICAL,spacing=0)

		TagLabel = Gtk.Label("Tag Area")
		self.pack_start(TagLabel,False,False,0)

		TagAreaFrame = Gtk.Frame()
		TagAreaFrame.set_shadow_type(Gtk.ShadowType.IN)
		self.add(TagAreaFrame)
		self.myFilter = ""

		with open("tags.txt") as file:
			for line in file:
				line = line.strip("\n")
				self._tagFields.append(line)

		#self.populateFields()

	def addField(self, label):
		# add the field key and value into the dictionay
		self._tagDic[label] = "testing"

		fieldBox = Gtk.Box(spacing=3)
		fieldTitle = Gtk.Label(label)
		fieldBox.pack_start(fieldTitle,False,False,0)
		fieldValue = Gtk.Entry()
		fieldBox.pack_end(fieldValue,False,False,0)
		self._fields.append(fieldBox)


	def addCombobox(self,label):
		comboBox = Gtk.Box(spacing=0)
		comboLabel = Gtk.Label(label)
		comboBox.pack_start(comboLabel, False, False,0)

		#Tag combobox
		self.tag_store = Gtk.ListStore(str)
		for f in self._tagFields:
			self.tag_store.append([f])

		self.tag_combo = Gtk.ComboBox.new_with_model(self.tag_store)
		self.tag_combo.connect("changed", self.on_name_combo_changed)
		self.tag_combo.set_active(0)

		renderer_text = Gtk.CellRendererText()
		self.tag_combo.pack_start(renderer_text, True)
		self.tag_combo.add_attribute(renderer_text, "text", 0)
		comboBox.pack_end(self.tag_combo , False, False, 0)
		self._fields.append(comboBox)

	 #Method for combobox in PDML View
	def on_name_combo_changed(self, combo):
		tree_iter = combo.get_active_iter()
		if tree_iter is not None:
		 	model = combo.get_model()
			self.myFilter = model[tree_iter][0]


	def addButton(self, name):
		newButton = Gtk.Button(label=name)
		self._buttons.append(newButton)



	def showFields(self):
		FieldGrid = Gtk.Grid()
		for x in range(len(self._fields)):
			FieldGrid.attach(self._fields[x],0,(x-1),2,1)
		self.pack_start(FieldGrid,False,False,0)



	def showButtons(self):
		buttonBox = Gtk.Box(spacing=10)
		for x in range(len(self._buttons)):
			buttonBox.pack_start(self._buttons[x],False,False,0)
		self.pack_end(buttonBox,False,False,36)

	def populateFields(self):
		#print (self._fields[0])
		for key in self._tagDic:
			print (key + ":" + self._tagDic[key])

