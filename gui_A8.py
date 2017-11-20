##tkinter gui for database
import Tkinter
import tkMessageBox
from Tkinter import *

top = Tkinter.Tk()
# Code to add widgets will go here...
textBox = Text(top, height = 30, width = 90)
textBox.pack()

# definitions of button actions
# temp, will be replaced with query functions

def readCallBack():
    tkMessageBox.showinfo("READING TBD")

readButton = Tkinter.Button(top, text = "Read", command = readCallBack)
readButton.pack(side=LEFT)

def writeCallBack():
    tkMessageBox.showinfo("WRITING TBD")

writeButton = Tkinter.Button(top, text = "Write", command = writeCallBack)
writeButton.pack(side=LEFT)

def updateCallBack():
    tkMessageBox.showinfo("UPDATING TBD")

updateButton = Tkinter.Button(top, text = "Update", command = updateCallBack)
updateButton.pack(side=LEFT)

def deleteCallBack():
    tkMessageBox.showinfo("DELETING TBD")

deleteButton = Tkinter.Button(top, text = "Delete", command = deleteCallBack)
deleteButton.pack(side=LEFT)

top.mainloop()
