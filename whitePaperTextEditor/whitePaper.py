import Tkinter
from Tkinter import *
import tkFileDialog
import tkMessageBox
#because tkinter text area does not provide scrolling
from ScrolledText import *


root = Tkinter.Tk(className="WhitePaper")
textPad = ScrolledText(root, width=100, height = 80)
#text editor+scrollable

def open_command():
	file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
	if file !=None:
		contents=file.read()
		textPad.insert('1.0',contents)
		file.close()

def save_command(self):
	file = tkFileDialog.asksaveasfile(mode='w')
	if file!=None:
		#slice off last character from get as an extra return is added
		data = self.textPad.get('1.0',END+'-1c')
		file.write(data)
		file.close()

def exit_command():
	if tkMessageBox.askokcancel("Quit","Do you really want to quit?"):
		root.destroy()

def about_command():
	label=tkMessageBox.showinfo("About","WhitePaper created by Charlson So\nInspired by knowpapa.com\nCopyright\nNo rights left to reserve")

def dummy():
	print "I am a Dummy Command"

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)


menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New", command=dummy)
filemenu.add_command(label="Open...",command=open_command)
filemenu.add_command(label="Save",command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=exit_command)

helpmenu=Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)
#unable to use select all (command+a)?
#menu appears on the mac menubar! 

textPad.pack()
root.mainloop()