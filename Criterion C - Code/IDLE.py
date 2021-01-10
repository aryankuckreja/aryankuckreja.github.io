#importing necessary programs to allow certain parts to run  
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import webbrowser

#setting variables
root = Tk()
root.title("Awareness Design Project")
new = 1
url = "https://mail.google.com/mail/u/2/#inbox"

#open webbrowser
def openweb():
    webbrowser.open(url, new=new)

#setting background colour
root.configure(background='black')

#display text, buttons and areas to type
l = Label(root, text="Input the homework:")
l.pack()
e = Entry(root)
e.pack()
b = Button(root, text="√")
b.pack()

l = Label(root, text="Due Dates")
l.pack()
e = Entry(root)
e.pack()
b = Button(root, text="√")
b.pack()

l = Label(root, text="Concerns about the email?")
l.pack()
e = Entry(root)
e.pack()
b = Button(root, text="√")
b.pack()

l = Label(root, text="Concerns about the link")
l.pack()
e = Entry(root)
e.pack()
b = Button(root, text="√")
b.pack()

#button that open gmail in google chrome
b = Button(root, text="Link to the email", command=openweb)
b.pack()

#creates a Tkinter-compatible photo image, which can be used everywhere Tkinter 
path = "Awareness_1.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand= "yes")

#end of program
root.mainloop()
