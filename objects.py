from Tkinter import *
import os
root = Tk()
root.title("Localhost")

def start(event):
    os.system("python traffic.py")

def fun(event):
    os.system(" ")

def vdo1(event):
    os.system("python video.py")

def vdo2(event):
    os.system("python video2.py")

toolbar = Frame(root,bg="blue")

insertB = Button(toolbar,text="Theme:- Computer Vision")
insertB.bind('<Button>',fun)
insertB.pack(side=TOP,padx=2,pady=2)
#printB = Button(toolbar,text="More")
#printB.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)



text1 = Text(root, height=20, width=40)
photo=PhotoImage(file='images.png')
text1.insert(END,'\n')
text1.image_create(END, image=photo)
text1.pack(side=LEFT,fill=X)

text2 = Text(root, height=20, width=85)
scroll = Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 11, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 16, 'bold'))
text2.tag_configure('color', foreground='#476042',font=('Tempus Sans ITC', 12, 'bold'))

text2.insert(END,'\nObject Influx and Outflux Detection\n', 'big')
quote = """\nThis project will detect the objects in motion 
and count their number in real time. The open CV library is 
the main module used to built this project. \n\n\n\n
At present we have deployed this project on cars moving 
on road to count the no. cars passing through a road at 
particular time."""
text2.insert(END, quote, 'color')
text2.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

button1 = Button(root,fg='white',bg='red',text="Detect Objects")
button1.bind("<Button>",start)
button1.place(x=450,y=200)


button1 = Button(root,fg='white',bg='red',text="Input Video")
button1.bind("<Button>",vdo1)
button1.place(x=350,y=200)


button1 = Button(root,fg='white',bg='red',text="Output Video")
button1.bind("<Button>",vdo2)
button1.place(x=570,y=200)

root.mainloop()
