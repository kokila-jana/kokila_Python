import tkinter as t
from tkinter import *
from PIL import  Image,ImageTk
from tkinter import messagebox
import pymysql as p
a=t.Tk()
a.geometry("1600x900")
a.config(bg="#BDB76B")
a.title("register Page")
# img=Image.open("C:\\Users\\manojana\\OneDrive\\Pictures\\img1.png")
# x=ImageTk.PhotoImage(img)
# y=Label(a,image=x)
# y.place(relwidth=1,relheight=1)
l=Label(a,text="Register Page",fg="blue",bg="#BDB76B",font=("Arial Black",35))
l.place(x=622,y=20)
# l.pack()
l1=Label(a,text="UserName",fg="blue",bg="#BDB76B",font=("Arial Black",25))
l1.place(x=522,y=120)
t=Entry(a,fg="blue",bg="#BDB76B",font=("Arial Black",25),width=20)
t.place(x=750,y=120)
l2=Label(a,text="Password",fg="blue",bg="#BDB76B",font=("Arial Black",25))
l2.place(x=522,y=220)
t1=Entry(a,fg="blue",bg="#BDB76B",font=("Arial Black",25),width=20,show="*")
t1.place(x=750,y=220)
l3=Label(a,text="Phone",fg="blue",bg="#BDB76B",font=("Arial Black",25))
l3.place(x=522,y=320)
t2=Entry(a,fg="blue",bg="#BDB76B",font=("Arial Black",25),width=20)
t2.place(x=750,y=320)
l4=Label(a,text="Gmail",fg="blue",bg="#BDB76B",font=("Arial Black",25))
l4.place(x=522,y=420)
t3=Entry(a,fg="blue",bg="#BDB76B",font=("Arial Black",25),width=20)
t3.place(x=750,y=420)
def fun():
    x = t.get()
    x1 = t1.get()
    x2 = t2.get()
    x3 = t3.get()
    if x=="" or  x1=="" or x2=="" or x3=="":
        messagebox.showwarning("Message","Fill all details...")
    else:
        con=p.connect(host="localhost",user="root",password="kokilajana",database="livewire1")
        cur=con.cursor()
        cur.execute("insert into info1 values('"+x+"','"+x1+"','"+x2+"','"+x3+"')")
        con.commit()
        messagebox.showinfo("Message","Register Success")
        a.destroy()
        import loginPage
b1=Button(a,text="Register",fg="blue",bg="#BDB76B",font=("Arial Black",25),activeforeground="green",activebackground="red",command=fun)
b1.place(x=700,y=520)

a.mainloop()
