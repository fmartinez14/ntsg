import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class stateMachineWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Network Traffic Based Software Generation - State Machine")

        img = Gtk.Image()
        img.set_from_file("index.png")
        self.add(img)


window = stateMachineWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
