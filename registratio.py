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
def reg():
    uname=username.get()
    pwd=password.get()
    f=open("admin.txt","a")
    #for i in f:
        #if (i.split(" ")[0]==uname):
            #messagebox.showinfo("Register","Already exist")
            #break
    #else:
    f.write(username)
    f.write(" ")
    f.write(password)
    f.write(" ")
    f.write("\n")
    messagebox.showinfo("Register","Registration succesfully")
    f.close()
Button(text="Register", command="reg",font=('gothic',20)).grid(row=2, column=0,columnspan=2)
w.mainloop()