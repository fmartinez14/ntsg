import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk, GLib, Gio


class FieldArea(Gtk.Box):

	data_list = list()

	def __init__(self):
		Gtk.Box.__init__(self,orientation=Gtk.Orientation.VERTICAL,spacing=0)

		TagLabel = Gtk.Label("Field Area")
		self.pack_start(TagLabel,False,False,0)

		FieldAreaFrame = Gtk.Frame()
		FieldAreaFrame.set_shadow_type(Gtk.ShadowType.IN)
		self.add(FieldAreaFrame)

		# self.set_border_width(10)

		#Setting up the self.grid to hold the data
		self.grid = Gtk.Grid()
		self.grid.set_column_homogeneous(True)
		self.grid.set_row_homogeneous(False)
		self.add(self.grid)

		#Creating the ListStore model
		self.data_liststore = Gtk.ListStore(str, str, int, int, str, str, int)

		self.current_filter_language = None

		#Creating the filter, feeding it with the liststore model
		self.language_filter = self.data_liststore.filter_new()
		#Setting the filter function
		self.language_filter.set_visible_func(self.language_filter_func)

		#Creating the treeview, making it use the filter as a model, and adding the columns
		self.treeview = Gtk.TreeView.new_with_model(self.language_filter)

		self.treeview.set_activate_on_single_click(True)
		#self.treeview.row_activated(Gtk.TreePath(), Gtk.TreeViewColumn(None))
		#self.treeview.set_cursor(Gtk.TreePath(row))

		#def NewSession_clicked(self, widget):
        #from newSessionsOverlay import ListBoxWindow
        #SessionWidget = ListBoxWindow()
        #SessionWidget.show_all()

		for i, column_title in enumerate(["Field Name", "Showname", "Size", "Position", "Value", "Entropy"]):
			renderer = Gtk.CellRendererText()
			column = Gtk.TreeViewColumn(column_title, renderer, text=i)
			column.set_resizable(True)
			self.treeview.append_column(column)

		self.treeview.connect("button_press_event", self.mouse_click)#****added this****



		#Creating buttons to filter by programming lang, and setting up their events
		# self.buttons = list()
		# for prog_language in ["Java", "C", "C++", "Python", "None"]:
		# 	button = Gtk.Button(prog_language)
		# 	self.buttons.append(button)
		# 	button.connect("clicked", self.on_selection_button_clicked)

		#Setting up the layout, putting the treeview in a scrollowindow, and the buttons in a row
		self.scrollable_treelist = Gtk.ScrolledWindow()
		self.scrollable_treelist.set_vexpand(True)
		self.scrollable_treelist.add(self.treeview)

		FieldBottomBox = Gtk.Box(spacing=10)
		SelectFieldsBox = Gtk.CheckButton(label="Select all fields")
		EditFieldsLabel = Gtk.Label("Field Name, showName, Value and Length are editable fields.")
		FieldBottomBox.pack_start(SelectFieldsBox, False, False, 0)
		FieldBottomBox.pack_start(EditFieldsLabel, False, False, 0)
		self.grid.attach(self.scrollable_treelist, 0, 0, 1, 1)
		self.grid.attach(FieldBottomBox, 0,1,1,1)
		# self.grid.attach_next_to(self.buttons[0], self.scrollable_treelist, Gtk.PositionType.BOTTOM, 1, 1)
		# for i, button in enumerate(self.buttons[1:]):
		# 	self.grid.attach_next_to(button, self.buttons[i], Gtk.PositionType.RIGHT, 1, 1)

		self.show_all()
	def mouse_click(self, tv, event):
		from tagOverlay import openPCAPwindow
		if event.button ==3:
			self.pthinfo = self.treeview.get_path_at_pos(event.x, event.y)
			if self.pthinfo != None:
				path,col,cellx,celly = self.pthinfo
				self.tree.grab_focus()
				self.tree.set_cursor(path,col,0)
		tagWindow = openPCAPwindow()
		tagWindow.show_all()

		print("you click me")

	def updateModel(self):
		for data_ref in self.data_list:
			self.data_liststore.append(list(data_ref))

			#Creating the filter, feeding it with the liststore model
		self.language_filter = self.data_liststore.filter_new()
		#Setting the filter function
		self.language_filter.set_visible_func(self.language_filter_func)
		#Creating the treeview, making it use the filter as a model, and adding the columns
		self.treeview = Gtk.TreeView.new_with_model(self.language_filter)

	""" This mignt need to change if the data_list is changed to a dictionary
		It would make finding and changing fields easy. But might mean over-
		hauling the functions in this class."""
	def addField(self, fieldName, showName, size, position, show, value, entropy):
		newField = (fieldName, showName, size, position, show, value, entropy)
		self.data_list.append(newField)
		self.updateModel()

	""" This mignt, no will, need to change if the data_list is changed to a dictionary
		It would make finding and changing fields easy. But might mean over-
		hauling the functions in this class.

		For now the row is needed to find the selected table row in the data_list
				the fieldToChange is needed to figure out which index in the tuple to change """
	def editField(self, row, fieldToChange, newValue):
		x = -1
		if fieldToChange == "Field Name":
			x = 0
		elif fieldToChange == "Showname":
			x = 1
		elif fieldToChange == "Value":
			x = 5
		elif fieldToChange == "Size":
			x = 2
		self.data_list[row][x] = newValue
		self.updateModel()

	""" This mignt, no will, need to change if the data_list is changed to a dictionary
		It would make finding and changing fields easy. But might mean over-
		hauling the functions in this class.

		For now the row is needed to find the selected table row in the data_list"""
	def remove(self, row):
		new_list = list()
		for i in self.data_list:
			if i == row:
				continue
			else:
				new_list.append(self.data_list[i])
		self.data_list = new_list
		updateModel()

	def language_filter_func(self, model, iter, data):
		"""Tests if the language in the row is the one in the filter"""
		if self.current_filter_language is None or self.current_filter_language == "None":
			return True
		else:
			return model[iter][2] == self.current_filter_language

	# def on_selection_button_clicked(self, widget):
	# 	"""Called on any of the button clicks"""
	# 	#We set the current language filter to the button's label
	# 	self.current_filter_language = widget.get_label()
	# 	# print("%s language selected!" % self.current_filter_language)
	# 	#We update the filter, which updates in turn the view
	# 	self.language_filter.refilter()
