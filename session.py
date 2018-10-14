import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Session(Gtk.Box):

	SessionsBox = Gtk.Box()
	WorkSpaceBox = Gtk.Box()
	_sessions = list()
	# need to rewrite the class to have state objects
	_states = list()

	FolderImage = Gtk.Image.new_from_file ("folder.png")

	def __init__(self):
		self.SessionsBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
		self.SessionsBox.set_border_width(3)
		SessionViewLabel = Gtk.Label("Session View")
		self.SessionsBox.pack_start(SessionViewLabel, True, True, 0)
		self.WorkSpaceBox = WorkSpaceBox("Workspace Kobra")

	def WorkSpaceBox(self, newName):
		label = Gtk.Label(newName)
		self.WorkSpaceBox.pack_start(label, False, False, 0)

	def addSession(self, name="New Session"):
		Session = Gtk.Box(spacing=0)
		Session.pack_start(FolderImage,False, False,0)
		SessionLabel = Gtk.Label(name + "\n  -State1")
		Session.pack_start(SessionLabel,False,False,0)
		self._sessions.append(Session)

	def showSessions():
		sns = self._sessions
		for x in range(len(sns)):
			self.WorkSpaceBox.pack_start(sns[x],False,False,0)
		self.SessionsBox.pack_start(self.WorkSapce,False,False,0)
