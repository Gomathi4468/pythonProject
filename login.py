from tkinter import *
from tkinter import messagebox
w=Tk()
w.geometry("400x300")
w.title("Registration")
w.config(bg="pink")
Label(text="username", font=('gothic',20)).grid(row=0, column=0)
username=Entry(font=('gothic',20))
username.grid(row=0,column=1)
Label(text="password", font=('gothic',20)).grid(row=1, column=0)
password=Entry(font=('gothic',20), show="*")
password.grid(row=1,column=1)
def login():
    uname=username.get()
    pwd=password.get()
    f=open("admin.txt","r")
    for i in f:
        if(i.split(" ")[0]==uname and i.split(" ")[1]==pwd):
            messagebox.showinfo("Login","Authorised user")
            break
    else:
        messagebox.showinfo("Login","Unauthorised user")
    f.close()
Button(text="login", command=login,font=('gothic',20)).grid(row=2, column=0,columnspan=2)
w.mainloop()