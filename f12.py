from tkinter import *
import database
from tkinter import messagebox
class hey:
    def __init__(self):
        self.star = Toplevel()
        self.can = Canvas(self.star, height=768, width=1366)
        self.can.pack()
        self.img = PhotoImage(file='./image/654.png')
        self.can.create_image(0, 0, image=self.img, anchor=NW)
        self.can.create_text((560, 250), text="ADD Username", fill='#000000', font=('monaco', 20, "bold"))
        self.ent0 = Entry(self.can)
        self.ent0.place(x=700, y=240)
        self.can.create_text((562, 280), text="ADD Password", fill='#000000', font=('monaco', 20, "bold"))
        self.ent2 = Entry(self.can,show="*")
        self.ent2.place(x=700, y=270)
        self.can.create_text((562, 310), text="confirm Password", fill='#000000', font=('monaco', 20, "bold"))
        self.ent3 = Entry(self.can,show="*")
        self.ent3.place(x=700, y=300)
        self.btn = Button(self.can, text="Submit", fg='white', bg='black', font=('monaco', 15, 'bold'),command=self.updatepassword)
        self.btn.place(x=690, y=340)
        self.btn = Button(self.can, text="<- Back", fg='white', bg='black', font=('monaco', 15, 'bold'),command=self.back)
        self.btn.place(x=500, y=340)
        self.star.resizable(height=False,width=False)
        self.star.state('zoomed')
        self.star.mainloop()
    def back(self):
        self.star.destroy()
    def updatepassword(self):
            obj = database.Database()
            if self .ent2.get() == self.ent3.get():
                obj.updatepassword1(self.ent0.get(),self.ent3.get())
                messagebox.showinfo("    WELCOME   ", "YOUR ACCOUNT HAS BEEN CREATED")
                self.star.destroy()
            else:
                messagebox.showinfo("Alert"," your Password are not same")