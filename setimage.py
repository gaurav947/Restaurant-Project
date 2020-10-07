from tkinter import *
import database
import f2
import f3
import f10
import f5
import f6
import f9
import f12
class Main:
    def __init__(self):
        self.tk=Tk()
        height = self.tk.winfo_screenheight()
        width = self.tk.winfo_screenwidth()
        y = (height-768)//2
        x = (width-1366)//2
        self.tk.geometry('1536x864+' + str(x) + '+' + str(y) + '')
        self.can = Canvas(self.tk, height=768, width=1366)
        self.can.pack()
        self.img = PhotoImage(file='./image/112233.png')
        self.can.create_image(0, 0, image=self.img, anchor=NW)
        self.can.create_text((640, 100), text='THE HUNGRY SITE !', fill='#FFD700', font=('chiller', 60))
        #400=where we from start,150=left line up and down,870=size of line,150=right= up and down
        self.can.create_line((380,150,910,150),fill='white')
        self.can.create_text((790, 140), text='For Admin ', fill='white', font=('Monaco', 20))
        self.can.create_text((550, 300), text='Username:', fill='white', font=('', 20))
        self.can.create_text((550, 350), text='Password:', fill='white', font=('', 20))
        self.ent1 = Entry(self.can)
        self.ent1.place(x=640, y=290)
        self.ent2 = Entry(self.can,show="*")
        self.ent2.place(x=640, y=340)
        self.btn = Button(self.can, text="Sign in", command=self.open, bg="black", fg="white")
        self.btn.place(x=600, y=400)
        self.tk.state("zoomed")
        self.tk.resizable(height=False, width=False)
        self.tk.mainloop()
    def signup(self):
        ob = database.Database()
        a = ob.checkadmin0()
        database.user = a
        i= f12.hey()
    def open(self):
        if self.ent1.get() != "" and self.ent2.get() != "":
            ob = database.Database()
            tup = (self.ent1.get(), self.ent2.get())
            a = ob.checkadmin(tup)
            if a is not None:
                database.user = a
                self.tk.destroy()
                self.star = Tk()
                self.star.title("THe HUNGRy SITe")
                height = self.star.winfo_screenheight()
                width = self.star.winfo_screenwidth()
                w = str(width)+'x'+str(height)
                self.star.geometry(w)
                '''menu'''
                self.menu_menu = Menu(self.star)
                self.menu_menu.add_command(label="ADD", command=self.switch)
                self.menu_menu.add_command(label="Manage Menu", command=self.switch2)
                '''worker'''
                self.menu1_menu1 = Menu(self.star)
                self.menu1_menu1.add_command(label="ADD", command=self.switch3)
                self.menu1_menu1.add_command(label="Manage", command=self.switch4)
                '''Account'''
                self.menu3_menu3 = Menu(self.star)
                self.menu3_menu3.add_command(label="Update Password", command=self.switch8)
                self.menu3_menu3.add_command(label="Logout", command=self.switch9)
                '''menubar'''
                self.menu = Menu(self.star)
                self.menu.add_cascade(label="Menu", menu=self.menu_menu)
                self.menu.add_cascade(label="Worker", menu=self.menu1_menu1)
                self.menu.add_cascade(label="Account", menu=self.menu3_menu3)
                self.can = Canvas(self.star, height=768, width=1366)
                self.can.pack()
                self.img = PhotoImage(file='./image/p9.png')
                self.can.create_image(0, 0, image=self.img, anchor=NW)
                self.can.create_text((700,500),text="WELCOME", fill="white")
                self.star.config(menu=self.menu)
                self.star.resizable(height=False,width=False)
                self.star.state("zoomed")
                self.star.mainloop()
            else:
                self.can.create_text((795, 410), text='*Please check Username or Password', fill='#FFD700', font=("bold"))
                self.btn = Button(self.can, text="Forget Anything ?", command=self.signup, bg="white", fg="blue")
                self.btn.place(x=640, y=370)
        else:
            self.can.create_text((830, 430), text='*Username or Password are not filled or incorrect', fill='#FFD700', font=("bold"))
            self.btn = Button(self.can, text="Forget Anything ?", command=self.signup, bg="white", fg="blue")
            self.btn.place(x=640, y=370)

    '''menud'''
    def switch(self):
        x= f2.hey()
    def switch2(self):
        y= f5.hey()
    '''worker'''
    def switch3(self):
        z= f3.hey()
    def switch4(self):
        a=f6.hey()
    '''Account'''
    def switch8(self):
        z= f10.hey()
    def switch9(self):
        a=f9.hey()
d=Main()
