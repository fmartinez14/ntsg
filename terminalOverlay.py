import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class openTerminal(Gtk.ListBoxRow):
    def __init__(self, data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Label(data))

class openTerminalwindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Terminal")
        self.set_border_width(10)

        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        terminalDescription = Gtk.Label("Terminal Description")
        terminalDescription.set_text("[Destination Folder Path] > [Generated Files]")
        box_outer.pack_start(terminalDescription, False, False, 0)

if __name__ == '__main__':
    win = openTerminalwindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
