
from tkinter import *

window = Tk()
window.geometry("250x250")
window.title("Mouse Position GUI")

def click(e):
   x= e.x
   y= e.y
   label = Label( window, text= "Position of the mouse: %d, %d" %(x,y) ) 
   label.grid(row=1, column=3)   


window.bind('<Button-1>',click)
window.mainloop()