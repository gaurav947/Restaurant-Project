from tkinter import *
import database
import f5
class UpdateMenu:
    def __init__(self,id_):
        self.id =(id_)
        d=database.Database()
        self.tup = d.getmenubyid(id_)
        self.star=Toplevel()
        self.star.geometry('1366x768')
        self.can = Canvas(self.star, height=768, width=1366)
        self.can.pack()
        self.img = PhotoImage(file='./image/654.png')
        self.can.create_image(0, 0, image=self.img, anchor=NW)
        self.can.create_text((260,250),text="Name --",fill='#000000',font=('monaco',20,"bold"))

        self.name = StringVar(self.star)
        self.ammount=StringVar(self.star)
        self.name.set(self.tup[1])
        self.ammount.set(self.tup[2])
        self.ent1=Entry(self.can,textvariable=self.name)
        self.ent1.place(x=340,y=240)

        self.can.create_text((272,280),text="Amount --",fill='#000000',font=('monaco',20,"bold"))

        self.ent2 = Entry(self.can,textvariable=self.ammount)
        self.ent2.place(x=340,y=270)

        self.btn1 = Button(self.can, text="<- Back", fg='white', bg='black', font=('monaco', 15, 'bold'),command=self.back)
        self.btn1.place(x=200,y=300)
        self.btn=Button(self.can,text="Update",fg='white',bg='black',font=('monaco',15,'bold'),command=self.printdata)
        self.btn.place(x=360,y=300)
        self.star.state("zoomed")
        self.star.mainloop()
    def printdata(self):
        if self.ent1.get()!="" and self.ent2.get()!="":
            ob = database.Database()
            tup = (self.ent1.get(),self.ent2.get(),self.id)
            ob.update1(tup)
            self.star.destroy()
            obj = f5.hey()
        elif self.ent1.get()==""and self.ent2.get()!="":
            self.can.create_text((680, 250), text="Please Enter in the block first", fill='red',font=('monaco', 15, "bold"))
        elif self.ent1.get()!=""and self.ent2.get()=="":
            self.can.create_text((680, 280), text="Please Enter in the block first", fill='red',font=('monaco', 15, "bold"))
        else:
            self.can.create_text((680, 280), text="Please Enter in the block first", fill='red',font=('monaco', 15, "bold"))
            self.can.create_text((680, 250), text="Please Enter in the block first", fill='red',font=('monaco', 15, "bold"))
    def back(self):
        self.star.destroy()

