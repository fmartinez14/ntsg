import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class PDMLView(Gtk.Box):

    def __init__(self,main):

        Gtk.Box.__init__(self,orientation=Gtk.Orientation.VERTICAL,spacing=0)
        self.main = main
#Start of PDML View
        mainGrid = Gtk.Grid()
        PDMLFrame = Gtk.Frame()
        PDMLBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=0)
        mainGrid.attach(PDMLBox,1,2,4,1)
        PDMLBox.add(PDMLFrame)
        self.add(mainGrid)
        self.myFilter = ""
        self.Filter1=""
        self.Filter2=""
        self.Filter3=""

        self.FilterExpression = Gtk.Entry()
    #Title
        # PDMLLabel = Gtk.Label("PDML View")
        # PDMLBox.pack_start(PDMLLabel,True,True,0)

    #First row
        PDMLButtons = Gtk.Box(spacing=5)

        NewStateName = Gtk.Entry()
        NewStateName.set_text("New PDML State Name")
        PDMLButtons.pack_start(NewStateName,True,True,0)

        SaveAsNewButton = Gtk.Button(label="Save as New\n  PDML State")
        PDMLButtons.pack_start(SaveAsNewButton,True,True,0)

        SaveCurrentButton = Gtk.Button(label="Save Current\n  PDML State")
        PDMLButtons.pack_start(SaveCurrentButton,True,True,0)

        CloseCurrentButton = Gtk.Button(label="Close Current\n   PDML State")
        PDMLButtons.pack_start(CloseCurrentButton,True,True,0)

        DeleteCurrentButton = Gtk.Button(label="Delete Current\n    PDML State")
        PDMLButtons.pack_start(DeleteCurrentButton,True,True,0)

        RenameStateName = Gtk.Entry()
        RenameStateName.set_text("Rename Current PDML State Name")
        PDMLButtons.pack_start(RenameStateName,True,True,0)

        RenameCurrentButton = Gtk.Button(label= "Rename Current\n      PDML State")
        PDMLButtons.pack_start(RenameCurrentButton,True,True,0)


        RemoveButton = Gtk.Button(label="Remove")
        PDMLButtons.pack_start(RemoveButton,True,True,0)

        ClearButton = Gtk.Button(label="Clear")
        PDMLButtons.pack_start(ClearButton,True,True,0)

        PDMLBox.pack_start(PDMLButtons,False,False,0)
    #End of first row

    #Start of Filter Area
        FilterLabelBox = Gtk.Box(spacing=0)

        FilterAreaLabel = Gtk.Label("Filter Area")
        FilterLabelBox.pack_start(FilterAreaLabel,False,False,0)
        PDMLBox.pack_start(FilterLabelBox,True,True,0)

        FilterBox = Gtk.Box(spacing=5)

        FilterLabel = Gtk.Label("Filter")
        FilterBox.pack_start(FilterLabel,False,True,0)


        self.FilterExpression.set_text("Filter Expression")
        FilterBox.pack_start(self.FilterExpression,True,True,0)

        ApplyButton = Gtk.Button(label="Apply")
        FilterBox.pack_start(ApplyButton,True,True,0)

        ApplyButton.connect("clicked",self.filterApplied)

        ClearButton = Gtk.Button(label="Clear")
        FilterBox.pack_start(ClearButton,True,True,0)

        ClearButton.connect("clicked",self.clearFilter)

        SaveButton = Gtk.Button(label="Save")
        FilterBox.pack_start(SaveButton,True,True,0)

        SaveButton.connect("clicked",self.saveFilter)

        SaveButton.connect("clicked", self.saveFilter)

        SavedFilterLabel = Gtk.Label("Saved Filter")
        FilterBox.pack_start(SavedFilterLabel,True,True,0)

    #Filter combobox
        self.filter_store = Gtk.ListStore(str)
        self.filter_store.append(["Filter 1"])
        self.filter_store.append(["Filter 2"])
        self.filter_store.append(["Filter 3"])

        self.filter_combo = Gtk.ComboBox.new_with_model(self.filter_store)
        self.filter_combo.connect("changed", self.on_name_combo_changed)
        self.filter_combo.set_active(0)

        renderer_text = Gtk.CellRendererText()
        self.filter_combo.pack_start(renderer_text, True)
        self.filter_combo.add_attribute(renderer_text, "text", 0)
        FilterBox.pack_start(self.filter_combo , False, False, True)
    #End of filter combobox

        ApplyButton = Gtk.Button(label="Apply")
        FilterBox.pack_start(ApplyButton,True,True,0)
        ApplyButton.connect("clicked",self.applyFilter)

        PDMLBox.pack_start(FilterBox,True,True,0)
    #End of Filter Area

    #Method for combobox in PDML View
    def on_name_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            self.myFilter = model[tree_iter][0]

    def filterApplied(self,widget):
        filterText = self.FilterExpression.get_text()
        self.main.filterExpression = self.FilterExpression
        self.main.callFilter()

    def clearFilter(self,widget):
        self.FilterExpression.set_text("")

    def saveFilter(self,widget):
        filterText = self.FilterExpression.get_text()
        if(self.myFilter == "Filter 1" or self.myFilter == ""):
            self.Filter1 = filterText
        elif(self.myFilter == "Filter 2"):
            self.Filter2= filterText
        elif(self.myFilter == "Filter 3"):
            self.Filter3 = filterText

    def applyFilter(self,widget):
        if(self.myFilter == "Filter 1" or self.myFilter == ""):
            self.FilterExpression.set_text(self.Filter1)
        elif(self.myFilter == "Filter 2"):
            self.FilterExpression.set_text(self.Filter2)
        elif(self.myFilter == "Filter 3"):
            self.FilterExpression.set_text(self.Filter3)



    #End of PDML View
