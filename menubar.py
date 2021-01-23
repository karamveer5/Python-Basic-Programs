from tkinter import *
root=Tk()

menubar=Menu(root)
root.config(menu=menubar)

filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")




helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="view License")

helpmenu.add_command(label="About")

root.mainloop()