import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib
import os

textview = Gtk.TextView()
textview.set_name("TextView")
buf = Gtk.TextBuffer()
textview.set_buffer(buf)
seperator = "\n"
error = {"This is a public service announcement.", "This is only a test."}
errorDisplay = seperator.join(error)
#for i in error:
buf.set_text(errorDisplay)

style_provider = Gtk.CssProvider()



css = """
#TextView{
    background-color: white;
}
"""

style_provider.load_from_data(bytes(css.encode()))
Gtk.StyleContext.add_provider_for_screen(
	Gdk.Screen.get_default(), style_provider,
	Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

win = Gtk.Window()
win.connect('delete-event', Gtk.main_quit)
win.add(textview)
win.show_all()


Gtk.main()
