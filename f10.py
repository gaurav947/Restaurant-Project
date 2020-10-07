from tkinter import *
import database
from tkinter import messagebox
class hey:
    def __init__(self):
        self.star = Toplevel()
        self.can = Canvas(self.star, height=768, width=1366)
        self.can.pack()
        self.img = PhotoImage(file='./image/p6.png')
        self.can.create_image(0, 0, image=self.img, anchor=NW)
        self.can.create_text((560, 220), text="Change Username", fill="white", font=('monaco', 20, "bold"))
        self.ent0 = Entry(self.can)
        self.ent0.place(x=700, y=210)
        self.can.create_text((560, 250), text="Old Password", fill='white', font=('monaco', 20, "bold"))
        self.ent1 = Entry(self.can,show="*")
        self.ent1.place(x=700, y=240)
        self.can.create_text((562, 280), text="New Password", fill='white', font=('monaco', 20, "bold"))
        self.ent2 = Entry(self.can,show="*")
        self.ent2.place(x=700, y=270)
        self.can.create_text((562, 310), text="confirm Password", fill='white', font=('monaco', 20, "bold"))
        self.ent3 = Entry(self.can,show="*")
        self.ent3.place(x=700, y=300)
        self.btn = Button(self.can, text="Submit", fg='white', bg='black', font=('monaco', 15, 'bold'),command=self.updatepassword)
        self.btn.place(x=690, y=340)
        self.btn = Button(self.can, text="<- Back", fg='white', bg='black', font=('monaco', 15, 'bold'),command=self.back)
        self.btn.place(x=500, y=340)
        self.star.resizable(height=False, width=False)
        self.star.state("zoomed")
        self.star.mainloop()
    def back(self):
        self.star.destroy()
    def updatepassword(self):
        if self.ent0.get()!="" and self.ent1.get()!="" and self.ent2.get()!="" and self.ent3.get()!="":
            if database.user[2] == self.ent1.get():
                obj = database.Database()
                if self .ent2.get() == self.ent3.get():
                    obj.updatepassword(self.ent0.get(),self.ent3.get())
                    messagebox.showinfo("Congrats","Your Password has been update.")
                    self.start.destroy()
                else:
                    self.can.create_text((950, 290), text="*Your New password are not Same ", fill="red",font="bold")

            else:
                self.can.create_text((930,250),text="*Your old Password is not Same", fill="red",font="bold")
        else:
            self.can.create_text((930,350),text="Please Fill all the Blanks for update", fill="red",font="bold")


