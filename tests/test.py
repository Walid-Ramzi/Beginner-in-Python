import os
from tkinter import *
from tkinter import filedialog
def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\XPRISTO\\Downloads", title="Choose your file", filetypes = (("all files","*.*"),("all files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    print(filepath)
    file.close()
    def change():
        ffff = filepath.split(".")
        print(ffff)
        print(ffff[0])
        a = ffff[0]
        b = ffff[0]+".docx"
        print(b)
        save = filedialog.asksaveasfile(initialdir="C:\\Users\\XPRISTO\\Downloads", title="Choose your save file", filetypes=[("word files",".docx"),("pdf files",".pdf")])
    change()


window = Tk()
button = Button(text="open", command=openFile)
button.pack()
window.mainloop()
#os.startfile(r'D:')