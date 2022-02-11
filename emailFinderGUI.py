
import re
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.geometry("500x500")
root.title("Email Finder")
root.config(bg = "khaki3")


textField = tkinter.Text(root, height = 20, width = 40)
textField.place(x = 80, y = 80)

def finder():
    search = re.findall("([a-zA-Z][a-zA-Z0-9\._-]+@[a-zA-Z]+\.com)", textField.get("1.0","end").rstrip())
    print(search)
    messagebox.showinfo("EMAILS\n", search)

btn = tkinter.Button(root,bg = "khaki4", text = "Click To Find Emails",command = finder)
btn.place(x = 290, y = 420)


root.mainloop()

