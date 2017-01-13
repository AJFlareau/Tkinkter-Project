from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from PIL import Image, ImageTk


def buttonpress():
    entrytext = entry1.get()
    print entrytext
    tkMessageBox.showinfo("Error", "Add new contact")   


root = Tk() #gives us a blank canvas object to work with
root.title("The Book of Random Contacts")

button1 = Button(root, text="Enter", bg="white", command=buttonpress)
button1.grid(row=5, column=1)

entry1 = Entry(root)
entry1.grid(row=5, column=0)


label1 = Label(root, text="Contacts", bg="grey", anchor=W)
label1.grid(row=4, column=0, sticky=EW, columnspan=3)

image = Image.open("Logo.png")
image = image.resize((1560,346))
photo = ImageTk.PhotoImage(image)

logo = Label(root, image=photo)
logo.image = photo
logo.grid(row=0, column=0) 

mainloop() #causes the windows to display on the screen until program closes