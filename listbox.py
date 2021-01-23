from tkinter import *
root =Tk()
root.geometry("500x450")
root.title("My Window")

Var1=StringVar()
S=Label(root,bg="green",fg="yellow",textvariable=Var1,width=10,font=("Arial",12,"bold"))
S.pack()

def print():
    V=K.get(K.curselection())
    ks.set(V)

ks=StringVar()
#ks.set((1,2,3,4))
K=Listbox(root,font=("times new roman",18,"bold"),relief=GROOVE,listvariable=ks)
K.pack()

K.insert("1","Doraemon")
K.insert("2","Schinchan")
K.insert("3","Pokemon")
K.insert("4","Perman")
K.insert("5","Death Note")
K.pack()

btn=Button(root,text="SHOW",font=("times new roman",18,"bold"),bg="lightblue",fg="green",command=print,height=1,width=10).pack()
root.mainloop()