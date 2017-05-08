from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from PIL import Image, ImageTk

alist=[]

def openfileR():
    global alist
    f = open("Addresses.txt", "r")
    for line in f:
        name = line[0:-1]
        alist.append(name)
    f.close()
    print alist
    for i in range(0, len(alist)):
        if i % 4 == 0:
            listbox1.insert (END, alist[i])
            
def openfileW():
    global alist
    f = open("Addresses.txt", 'w')
    for i in alist:
        f.write(i+"\n")
    f.close()    
 
def buttonpress1():
    clearlist2()
    x=listbox1.index(ACTIVE)
    idx=x*4
    entry1.insert(END,alist[idx])
    entry2.insert(END,alist[idx+1])
    entry3.insert(END,alist[idx+2])
    entry4.insert(END,alist[idx+3])
    
    
    
def buttonpress2():
    global alist
    x=listbox1.index(ACTIVE)
    idx=x*4
    alist[idx]=entry1.get()
    alist[idx+1]=entry2.get()
    alist[idx+2]=entry3.get()
    alist[idx+3]=entry4.get()
    openfileW()
    print alist
      

def buttonpress3():
    global alist
    x=listbox1.index(ACTIVE)
    listbox1.delete(x)
    clearlist2()
    idx=x*4
    alist.pop(idx) 
    alist.pop(idx) 
    alist.pop(idx) 
    alist.pop(idx) 
    print alist
    
           
def clearlist2():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)

def buttonpress4():
    listbox1.insert(END, entry1.get())
    alist.append(entry1.get())
    alist.append(entry2.get())
    alist.append(entry3.get())
    alist.append(entry4.get())

root = Tk() #gives us a blank canvas object to work with
root.title("The Book of Random Contacts")

button1 = Button(root, text="Add Contact", bg="grey", command=buttonpress4)
button1.grid(row=7, column=0)

button2 = Button(root, text="Select", bg="grey", command=buttonpress1)
button2.grid(row=7, column=1)

button3 = Button(root, text="Save", bg="grey", command=buttonpress2)
button3.grid(row=7, column=8)

button4 = Button(root, text="Delete", bg="grey", command=buttonpress3)
button4.grid(row=7, column=9)

label1 = Label(root, text="Contacts", bg="grey", anchor=W)
label1.grid(row=1, column=0, sticky=W)


scrollbar = Scrollbar(root, orient=VERTICAL)
listbox1 = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox1.yview)
scrollbar.grid(row=2, column=5, rowspan=5, sticky=W)
listbox1.grid(row=2, column=0, columnspan=5, rowspan=5)


label2 = Label(root, text="Name:")
label2.grid(row=2, column=7)

label3 = Label(root, text="Phone Number:")
label3.grid(row=3, column=7)

label4 = Label(root, text=" Email:")
label4.grid(row=4, column=7)

label5 = Label(root, text="Question:")
label5.grid(row=5, column=7)

label6 = Label(root, text="Answer:")
label6.grid(row=6, column=7)

label7 = Label(root, text="Whats your favorite food?")
label7.grid(row=5, column=9)

entry1 = Entry(root)
entry1.grid(row=2, column=9)

entry2 = Entry(root)
entry2.grid(row=3, column=9)

entry3 = Entry(root)
entry3.grid(row=4, column=9)

entry4 = Entry(root)
entry4.grid(row=6, column=9)



menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfileR)
filemenu.add_separator()
filemenu.add_command(label="Save", command=openfileW)

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
 











mainloop()