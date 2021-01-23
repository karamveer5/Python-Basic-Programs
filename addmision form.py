from tkinter import *
root=Tk()
root.geometry("600x500")
root.title("Admission Form 2020")
title=Label(root,text="Addmission Form 2020",font=("times new roman",30,"bold"),bg="yellow",fg="red",border="2",relief=GROOVE).place(x=0,y=0,relwidth=1)

lb1=Label(root,text="Full Name",font=("",22,"bold"),fg="blue").place(x=30,y=85)

e1=Entry(root,font=("times new roman",22,"bold"),fg="red",width=58,relief=SUNKEN).place(x=180,y=85)

lb2=Label(root,text="Father Name",font=("",22,"bold"),fg="blue").place(x=30,y=155)

e2=Entry(root,font=("times new roman",22,"bold"),fg="red",width=55,relief=SUNKEN).place(x=220,y=155)

lb3=Label(root,text="Mother Name",font=("",22,"bold"),fg="blue").place(x=30,y=225)

e3=Entry(root,font=("times new roman",22,"bold"),fg="red",width=55,relief=SUNKEN).place(x=220,y=225)

lb4=Label(root,text="Address",font=("",22,"bold"),fg="blue").place(x=30,y=295)

e4=Entry(root,font=("times new roman",22,"bold"),fg="red",width=60,relief=SUNKEN).place(x=150,y=295)

lb5=Label(root,text="Email ID",font=("",22,"bold"),fg="blue").place(x=30,y=365)

e5=Entry(root,font=("times new roman",22,"bold"),fg="red",width=60,relief=SUNKEN).place(x=150,y=365)



var=IntVar()
lb6=Label(root,text="Gender",font=("",22,"bold"),fg="blue").place(x=30,y=435)
r1=Radiobutton(root,text="Male",variable=var,value="male",font=("",22,"bold"),fg="blue").place(x=200,y=435)
r2=Radiobutton(root,text="Female",variable=var,value="female",font=("",22,"bold"),fg="blue").place(x=350,y=435)


var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
lb7=Label(root,text="Programming Language",font=("",22,"bold"),fg="blue").place(x=30,y=505)
c1=Checkbutton(root,text="C",variable=var1,fg="blue",font=("",22,"bold")).place(x=385,y=505)
c1=Checkbutton(root,text="JAvaScript",variable=var2,fg="blue",font=("",22,"bold")).place(x=555,y=505)
c1=Checkbutton(root,text="HTML",variable=var3,fg="blue",font=("",22,"bold")).place(x=385,y=555)
c1=Checkbutton(root,text="Python",variable=var4,fg="blue",font=("",22,"bold")).place(x=555,y=555)


Button(root,text="SUBMIT",font=("",22,"bold"),fg="blue",bg="yellow").place(x=500,y=630)

root.mainloop()