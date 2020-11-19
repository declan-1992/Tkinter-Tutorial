from tkinter import *

root = Tk()

#Drop Down Boxes
def show():
	myLabel = Label(root, text = clicked.get()).pack()


#Create list of options for dropdown menu
options = ["Monday", 
"Tuesday", 
"Wednesday", 
"Thursday", 
"Friday"
]

clicked = StringVar()
clicked.set(options[0])

#Create drop down menu widget
drop = OptionMenu(root, clicked, *options)
drop.pack()

#Add drop down option to screen
myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
