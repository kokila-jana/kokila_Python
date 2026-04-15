import tkinter as t
from tkinter import *
from tkinter.ttk import Combobox
from  tkinter import scrolledtext
a=t.Tk()
a.geometry("1600x900")
a.config(bg="#A9A9A9")
a.title("next Page")
cb=Combobox(a,font=("Arial Black",35),width=15)
cb["values"]=["select","Java","Python","Web designing","datascience"]
cb.current(0)
cb.place(x=100,y=20)
rb=Radiobutton(a,text="Male",fg="red",bg="#F5DEB3",font=("Arial Black",35),width=5,value=1)
rb.place(x=100,y=100)

rb1=Radiobutton(a,text="Female",fg="red",bg="#F5DEB3",font=("Arial Black",35),width=6,value=0)
rb1.place(x=350,y=100)
ck=Checkbutton(a,text="I am not Robot",fg="red",bg="#F5DEB3",font=("Arial Black",35))
ck.place(x=100,y=200)
sp=Spinbox(a,fg="red",bg="#F5DEB3",font=("Arial Black",35),width=3,from_=21,to=50)
sp.place(x=100,y=300)

sct=scrolledtext.ScrolledText(a,fg="red",bg="#F5DEB3",font=("Arial Black",35),width=10,height=5)
sct.place(x=100,y=400)
def demo():
    a.destroy()
    import loginPage
b=Button(a,text="Logout",fg="red",bg="#F5DEB3",font=("Arial Black",25),activeforeground="green",activebackground="red",command=demo)
b.place(x=972,y=420)



a.mainloop()
