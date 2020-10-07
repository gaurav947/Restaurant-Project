from tkinter import *
import database
class hey:
    def __init__(self):
        self.star=Toplevel()
        self.can = Canvas(self.star, height=768, width=1366)
        self.can.pack()
        self.img = PhotoImage(file='./image/roll.png')
        self.can.create_image(0, 0, image=self.img, anchor=NW)

        self.can.create_text((220, 250), text="Name -- ", fill='#000000', font=('monaco', 20, "bold"))
        self.ent1 = Entry(self.can)
        self.ent1.place(x=340, y=240)

        self.can.create_text((233, 280), text="Gender -- ", fill='#000000', font=('monaco', 20, "bold"))
        self.ent2 = Entry(self.can)
        self.ent2.place(x=340, y=270)

        self.can.create_text((227, 310), text="Email -- ", fill='#000000', font=('monaco', 20, "bold"))
        self.ent3 = Entry(self.can)
        self.ent3.place(x=340, y=300)

        self.can.create_text((250, 340), text="Password -- ", fill='#000000', font=('monaco', 20, "bold"))
        self.ent4 = Entry(self.can,show='*')
        self.ent4.place(x=340, y=330)

        self.can.create_text((239, 370), text="Contact -- ", fill='#000000', font=('monaco', 20, "bold"))
        self.ent5 = Entry(self.can)
        self.ent5.place(x=340, y=360)

        self.can.create_text((240, 400), text="Address -- ", fill='#000000', font=('monaco', 20, "bold"))
        self.ent6 = Entry(self.can)
        self.ent6.place(x=340, y=390)

        self.btn1 = Button(self.can, text="Submit", fg='white', bg='black', font=('monaco', 15, 'bold'),command=self.press)
        self.btn1.place(x=360, y=420)
        self.btn = Button(self.can, text="<- Back", fg='white', bg='black', font=('monaco', 14, 'bold'),command=self.back)
        self.btn.place(x=150, y=420)
        self.star.resizable(height=False, width=False)
        self.star.state("zoomed")
        self.star.mainloop()
    def press(self):
        if self.ent1.get()!="" and self.ent2.get()!=""and self.ent3.get()!="" and self.ent4.get()!="" and self.ent5.get()!="" and self.ent5.get()!="":
            ob = database.Database()
            tup = (self.ent1.get(), self.ent2.get(), self.ent3.get(), self.ent4.get(), self.ent5.get(), self.ent6.get())
            ob.insertData2(tup)
            self.star.destroy()
        else:
            self.can.create_text((730, 430), text="**Please fill all the blocks before submittion", fill='#FFD700',font=('monaco', 15, "bold"))
    def back(self):
        self.star.destroy()


