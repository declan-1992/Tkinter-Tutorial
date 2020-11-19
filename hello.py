from tkinter import *
#Everything in tkinter is a widget

root = Tk()

#Creating a label widget
myLabel = Label(root, text="Hello World!")


#Putting it onto the screen
myLabel.pack()

#Loop (refresh) page repeatedly 
root.mainloop()
