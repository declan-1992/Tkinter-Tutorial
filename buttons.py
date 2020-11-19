from tkinter import *
#Everything in tkinter is a widget

root = Tk()

#define what the button will do
def myClick():
	myLabel = Label(root, text="Look! I clicked a Button!!")
	myLabel.pack()

#set up button widget
myButton = Button(root, text = "Click Me!", command=myClick, fg="blue", bg="#000000")
myButton.pack()

root.mainloop()
