
from Tkinter import *
MainScreen = Tk()
MainScreen.title('NTSG')

#Set height and width of main canvas.
canvas_height=10000
canvas_width=10000
#End height and width

#Main Canvas begin
w = Canvas(MainScreen)
w.grid(column=0,row=0)
#Main Canvas end.

#Start of header
M = Frame(w)
M.grid(column=0,row=0)
#Main header end

ButtonCanvas = Frame(M,bg="red")
ButtonCanvas.grid(column=1,row=0,sticky="e")

NTSGLabel =Label(M , text= "Network Traffic Based Software Generation" ,  fg="orange")
NTSGLabel.grid(column=0, row=0)

CreateSession = Button(ButtonCanvas, text='Create Session', command=MainScreen.destroy , fg="blue")
CreateSession.grid(column=1,row=0)

OpenSession = Button(ButtonCanvas, text='Open Session', command=MainScreen.destroy , fg="blue")
OpenSession.grid(column=2,row=0)

CloseSession = Button(ButtonCanvas, text='Close Session', command=MainScreen.destroy , fg="blue")
CloseSession.grid(column=3,row=0)

SwitchWorkspace = Button(ButtonCanvas, text='Switch Workspace', command=MainScreen.destroy , fg="blue")
SwitchWorkspace.grid(column=4,row=0)

OpenPCAP = Button(ButtonCanvas, text='Open PCAP', command=MainScreen.destroy , fg="blue")
OpenPCAP.grid(column=5,row=0)

Terminal = Button(ButtonCanvas, text='Terminal', command=MainScreen.destroy , fg="blue")
Terminal.grid(column=6,row=0)

#End of Header


#Start of Middle Frame
MiddleFrame = Frame(w)
MiddleFrame.grid(column=0,row=1)
#End Of Middle Frame

#Session View
SessionView = Frame(MiddleFrame)
SessionView.grid(column=0,row=1,sticky="w")

SessionLabel =Label(SessionView , text= "Sessions View" ,  fg="orange")
SessionLabel.grid(column=0,row=0, sticky="w")
#End of sessions views.


#Start of PDML View
PDMLView = Frame(MiddleFrame)
PDMLView.grid(column=1,row=1)

PDMLLabel =Label(PDMLView , text= "PDML View" ,fg="orange")
PDMLLabel.grid(column=0,row=0, sticky="e")

#End of PDML View



#Start of low frame
LowFrame = Frame(w)
LowFrame.grid(column=0,row=2)
#End of low frame

#Start of Tag Area
TagArea = Frame(LowFrame)
TagArea.grid(column=0,row=0,sticky="w")



TagLabel =Label(TagArea , text= "Tag Area" , fg="orange")
TagLabel.grid(column=0,row=0)

e1 = Entry(TagArea)
e2 = Entry(TagArea)
e3= Entry(TagArea)
e4= Entry(TagArea)

TagLabel =Label(TagArea , text= "Saved Tag" , fg="orange")
TagLabel.grid(row=1, sticky="w")

TagLabel =Label(TagArea , text= "Tag Name" , fg="orange")
TagLabel.grid(row=2,sticky="w")

TagLabel =Label(TagArea , text= "Tag Field" , fg="orange")
TagLabel.grid(row=3,sticky="w")

TagLabel =Label(TagArea , text= "Tag Description" , fg="orange")
TagLabel.grid(row=4,sticky="w")

e1.grid(row=1, column=2)
e2.grid(row=2, column=2)
e3.grid(row=3, column=2)
e4.grid(row=4, column=2)

UpdateLabel = Button(TagArea, text='Update', command=MainScreen.destroy , fg="blue")
UpdateLabel.grid(column=1,row=5,sticky="e")

CancelLabel = Button(TagArea, text='Cancel', command=MainScreen.destroy , fg="blue")
CancelLabel.grid(column=2,row=5,sticky="w")
#End of Tag Area


#Start of Field Area
FieldArea = Frame(LowFrame)
FieldArea.grid(column=2,row=0)

FieldLabel =Label(TagArea , text= "Field Area"  , fg="orange")
FieldLabel.grid(column=1,row=0)
#End of Field Area


#Start of Message Type area
MessageArea = Frame(LowFrame)
MessageArea.grid(column=3,row=0)


MessageLabel =Label(MessageArea , text= "Message Type Area" ,  fg="orange")
MessageLabel.grid(column=2,row=0)

NewMessageLabel = Button(MessageArea, text='New/Modify', command=MainScreen.destroy , fg="blue")
NewMessageLabel.grid(column=1,row=1)

NewDependency = Button(MessageArea, text='New Dependency', command=MainScreen.destroy , fg="blue")
NewDependency.grid(column=2,row=1)

NewTemplate = Button(MessageArea, text='Template', command=MainScreen.destroy , fg="blue")
NewTemplate.grid(column=3,row=1,sticky="w")

NewEquivalency = Button(MessageArea, text='Equivalency', command=MainScreen.destroy , fg="blue")
NewEquivalency.grid(column=4,row=1,sticky="w")

NewGeneration = Button(MessageArea, text='Generation', command=MainScreen.destroy , fg="blue")
NewGeneration.grid(column=5,row=1,sticky="w")
#
# InstructionsLabel =Label(MessageArea , text= "To create a new Message Type, " ,  fg="orange",width=20)
# InstructionsLabel.grid(column=2,row=2)
#
# InstructionsLabel3 =Label(MessageArea , text="please enter a message type name and select message type field value pair(s).", fg="orange")
# InstructionsLabel3.grid(column=2,row=3)
#
# InstructionsLabel2= Label(MessageArea , text="To update/delete to an existing message type, please select from the existing message type first and the previosuly selected name and field pair(s) will be pre pouplated." ,fg= "orange",width=20)
# InstructionsLabel2.grid(column=2,row=4,sticky="e")

#end of Message Type area



mainloop()
