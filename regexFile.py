
import re
import tkinter

f = open("C:/Users/Lenovo/Desktop/PythonPractices/textt.txt", 'r')

root = tkinter.Tk()
root.geometry('350x350')
root.title("Email Finder")
root.config(background = "pale turquoise")

def write():
    for line in f:
        x = re.findall('([a-zA-Z0-9\._-]+@\S+)', line)
        if x:
            lbl = tkinter.Label(root,bg="pale turquoise", text = x).pack()
            print(x)

btn = tkinter.Button(root,bg = "purple",text = "Click To See Emails", command = write).pack()

root.mainloop()

f.close()