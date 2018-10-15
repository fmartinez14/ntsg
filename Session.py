import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Session(Gtk.Box):

	WorkSpaceBox = Gtk.Box()
	_sessions = list()
	# need to rewrite the class to have state objects
	_states = list()

	def __init__(self):
		Gtk.Box.__init__(self,orientation=Gtk.Orientation.VERTICAL,spacing=10)
		self.set_border_width(3)
		SessionViewLabel = Gtk.Label("Session View")
		self.pack_start(SessionViewLabel, True, True, 0)
		self.WorkSpaceBox = Gtk.Box("Workspace Kobra",orientation=Gtk.Orientation.VERTICAL)

	def WorkSpaceBox(self, newName):
		label = Gtk.Label(newName)
		self.WorkSpaceBox.pack_start(label, False, False, 0)

	def addSession(self, name="New Session"):
		FolderImage = Gtk.Image.new_from_file ("folder.png")

		Session = Gtk.Box(spacing=0)
		Session.pack_start(FolderImage,False, False,0)
		SessionLabel = Gtk.Label(name + "\n  -State1")
		Session.pack_start(SessionLabel,False,False,0)
		self._sessions.append(Session)

	def showSessions(self):
		sns = self._sessions
		for x in range(len(sns)):
			self.WorkSpaceBox.pack_start(sns[x],False,False,0)
		self.pack_start(self.WorkSpaceBox,False,False,0)

		SessionsFrame = Gtk.Frame()
		self.add(SessionsFrame)
