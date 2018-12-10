import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Session(Gtk.Box):

	WorkSpaceBox = Gtk.Box()
	_sessions = list()
	CurrSession=0
	# need to rewrite the class to have state objects
	_states = list()
	CurrState = 0


	def __init__(self):
		Gtk.Box.__init__(self,orientation=Gtk.Orientation.VERTICAL,spacing=10)
		self.set_border_width(3)
		SessionViewLabel = Gtk.Label("Session View")
		self.pack_start(SessionViewLabel, True, True, 0)
		self.WorkSpaceBox = Gtk.Box("Workspace Kobra",orientation=Gtk.Orientation.VERTICAL)

	def WorkSpaceBox(self, newName):
		label = Gtk.Label(newName)
		self.WorkSpaceBox.pack_start(label, False, False, 0)

	def addSession(self, name):
		FolderImage = Gtk.Image.new_from_file ("folder.png")

		Session = Gtk.Box(spacing=0)
		Session.pack_start(FolderImage,False, False,0)
		SessionName = Gtk.Label(name)
		Session.pack_start(SessionName,False,False,0)
		self._sessions.append(Session)
		self.CurrSession +=1

		self.WorkSpaceBox.pack_start(Session, False, False, 0)
		self.showSessions()

		print "session added "+ name

	def addState(self, stateName):
		#label = Gtk.label(name)
		SessionState = Gtk.Label(stateName)
		Session.pack_start(stateName, False, False, 0)
		self._state.append(SessionState)
		self.CurrState += 1

	def deleteSession(self,widget):
		getSessions = self._sessions
		if self.CurrSession > 1:
			self.CurrSession -= 1
			getSessions[self.CurrSession].set_child_visible(False)

	def showSession(self):
		getSessions = self._sessions
		if self.CurrSession <= 2:
			getSessions[self.CurrSession].set_child_visible(True)
			self.CurrSession+=1

	def showSessions(self):
		sns = self._sessions
		for x in range(len(sns)):
			self.WorkSpaceBox.pack_start(sns[x],False,False,0)
		self.pack_start(self.WorkSpaceBox,False,False,0)

		#SessionsFrame = Gtk.Frame()
		#self.add(SessionsFrame)
