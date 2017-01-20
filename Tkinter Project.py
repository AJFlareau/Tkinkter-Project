from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from PIL import Image, ImageTk

def openfileR():
    clearlist2()
    f = open("Readme.txt", "r")
    for line in f:
        name = line[0:-1]
        lisbox1.insert(END, name)
    f.close()
    findsize()
   
def openfileW():
    f = open("Readme.txt", 'w')
    names = listbox1.get(0, END)
    for i in names:
        f.write(i+"\n")


def buttonpress():
    #entrytext = entry1.get()
   # print entrytext
    tkMessageBox.showinfo("Error", "Add new contact")
    
def buttonpress1():
    #entrytext = entry1.get()
    #print entrytext
    tkMessageBox.showinfo("Error", "Select contact from list")
    
def buttonpress2():
    #entrytext = entry1.get()
    #print entrytext
    tkMessageBox.showinfo("Error", "Add new contact")  

def buttonpress3():
    #entrytext = entry1.get()
    #print entrytext
    tkMessageBox.showinfo("Error", "Delete contact")       


root = Tk() #gives us a blank canvas object to work with
root.title("The Book of Random Contacts")

button1 = Button(root, text="Add", bg="grey", command=buttonpress)
button1.grid(row=7, column=0)

button2 = Button(root, text="Select", bg="grey", command=buttonpress1)
button2.grid(row=7, column=2)

button3 = Button(root, text="Add", bg="grey", command=buttonpress2)
button3.grid(row=7, column=10)


button4 = Button(root, text="Delete", bg="grey", command=buttonpress3)
button4.grid(row=7, column=14)





label1 = Label(root, text="Contacts", bg="grey", anchor=W)
label1.grid(row=1, column=0, sticky=W)

image = Image.open("Logo.png")
image = image.resize((780,123))
photo = ImageTk.PhotoImage(image)

scrollbar = Scrollbar(root, orient=VERTICAL)
listbox1 = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox1.yview)
scrollbar.grid(row=2, column=5, rowspan=5, sticky=W)
listbox1.grid(row=2, column=0, columnspan=5, rowspan=5)
listbox1.insert(END, "Andrew Flareau", "Ian Pope")



menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfileR)
filemenu.add_separator()
filemenu.add_command(label="Save", command=openfileW)

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
 

#logo = Label(root, image=photo)
#logo.image = photo
#logo.grid(row=0, column=0, columnspan=8) 

mainloop() #causes the windows to display on the screen until program closes