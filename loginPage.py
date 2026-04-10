import tkinter as t
from tkinter import *
from PIL import  Image,ImageTk
from tkinter import messagebox
a=t.Tk()
a.geometry("1600x900")
a.config(bg="#F5DEB3")
a.title("Login Page")
# img=Image.open("C:\\Users\\manojana\\OneDrive\\Pictures\\img1.png")
# x=ImageTk.PhotoImage(img)
# y=Label(a,image=x)
# y.place(relwidth=1,relheight=1)
l=Label(a,text="Login Page",fg="red",bg="#F5DEB3",font=("Arial Black",35))
l.place(x=622,y=120)
# l.pack()
l1=Label(a,text="UserName",fg="red",bg="#F5DEB3",font=("Arial Black",25))
l1.place(x=522,y=220)
t=Entry(a,fg="red",bg="#F5DEB3",font=("Arial Black",25),width=20)
t.place(x=750,y=220)
l2=Label(a,text="Password",fg="red",bg="#F5DEB3",font=("Arial Black",25))
l2.place(x=522,y=320)
t1=Entry(a,fg="red",bg="#F5DEB3",font=("Arial Black",25),width=20,show="*")
t1.place(x=750,y=320)

def demo():
    x=t.get()
    y=t1.get()
    if x=="" or y=="":
        messagebox.showwarning("Warning","Please enter all details...")
    elif x=="Python" and  y=="12345":
         messagebox.showinfo("Message","Login Success")
    else:
        messagebox.showerror("Error","Invalid username or password...l")

b=Button(a,text="Login",fg="red",bg="#F5DEB3",font=("Arial Black",25),activeforeground="green",activebackground="red",command=demo)
b.place(x=672,y=420)






a.mainloop()
