from tkinter import *
from tkinter import messagebox
w=Tk()
w.geometry("300x400")
w.title("purchasing")
w.config(bg="pink")
Label(text="product_name").grid(row=0,column=0)
product_name=Entry()
product_name.grid(row=0,column=1)
Label(text="product_quantity").grid(row=1,column=0)
product_quantity=Entry()
product_quantity.grid(row=1,column=1)
Label(text="product_price").grid(row=2,column=0)
product_price=Entry()
product_price.grid(row=2,column=1)
def search():
    pname=product_name.get()
    #pquantity=product_quantity.get()
    f=open("produc.txt","r")
    for i in f:
        if(i.split(" ")[0]==pname):
            messagebox.showinfo("search","product is available")
            pquantity=product_quantity.get()
            print(pquantity)
            pprice=product_price.get()
            print(pprice)
            if(i.split(" ")[2]>=pquantity):
                print("true")
                total_price=int(pquantity)*int(pprice)
                messagebox.showinfo("billing",total_price)
            else:
                messagebox.showinfo("search","out of stock")
        else:
            messagebox.showinfo("search", "product is not available")
    f.close()
Button(text="search",command=search).grid(row=3,column=0,columnspan=2)
w.mainloop()

