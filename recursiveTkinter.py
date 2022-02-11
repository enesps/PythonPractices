
import tkinter

root = tkinter.Tk()
root.geometry("400x300")
root.title("Recursive")
root.configure(background='powder blue')

textLabel = tkinter.Label(root, text = "Enter a word", bg = "powder blue")
textLabel.place(x = 30 , y = 30)

# global list
list = []

def show(list):
    l = 50
    for x in list:
        label = tkinter.Label(root, text = x, bg = "powder blue")
        label.place (x = 180, y = l)
        l += 20
    
def tower(word):
    
    if len(word) == 0:
        show(list)        
    else:
        
        print(word[0:])
        list.append(word[0:])
        tower(word[len(word)-(len(word)-1):])
        
entry = tkinter.Entry(root)
entry.place(x = 30, y = 60)

btn = tkinter.Button(root,bg = "peach puff",text = "Click" , command = lambda: tower(entry.get() ))
btn.place(x = 30 , y= 90)

root.mainloop()