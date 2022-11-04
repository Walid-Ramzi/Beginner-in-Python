from random import choice, randint
from tkinter import *
import string

def generate_password():
    password_min=8
    password_max=10
    all_chars = string.ascii_letters + string.punctuation +string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min,password_max)))
    write.delete(0,END)
    write.insert(0,password)


win = Tk()
win.title("Walid_Ramzi")
win.geometry("720x640")
win.minsize(200, 120)
win.iconbitmap("logo.ico")
win.config(bg="#667CE9")

frame = Frame(win, bg="#667CE9", bd=1, relief=SUNKEN)
frame1 = Frame(win, bg="#667CE9")

inside_title = Label(frame, text="Hello User to",
                     font=("courrier", 40), bg="#667CE9")
inside_title.pack()
inside_subtitle = Label(frame, text="Password Generator",
                     font=("courrier", 28), bg="#667CE9", fg="green")
inside_subtitle.pack()
frame.pack()

inside_subtitle1 = Label(frame1, text="Password",
                     font=("courrier", 30), bg="#667CE9", fg="Purple")
inside_subtitle1.pack()
write = Entry(frame1, bg=("#FFFFFF"),font=("courrier",30))
write.pack()
KWR_button = Button(frame1, text="Generate",
                     font=("courrier", 28), bg="#E21C1C", fg="yellow",command=generate_password)
KWR_button.pack()

frame1.pack(expand=YES)

win.mainloop()
