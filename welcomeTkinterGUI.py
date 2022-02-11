
import tkinter
from tkinter import *
from tkinter import messagebox


root = tkinter.Tk()
root.geometry("300x200")
root.title("Welcome App")
root.config(background = "GREEN")

label = Label(root,text="Name& Surname:", justify='center') 
label.place(x=80,y=30) 
label.config(background = "GREEN")
 
nameSurname = Entry(root,justify='center')
nameSurname.place(x=80,y=60)

def login():
    messagebox.showinfo("Welcome Message Box", "Welcome "+ nameSurname.get() )
    
btn = Button(root,text="Login",command=login )
btn.place(x=80,y=90)
btn.config(background = "BROWN")


root.mainloop()


