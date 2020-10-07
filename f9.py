from tkinter import *
class hey:
    def __init__(self):
        self.star1 = Toplevel()
        self.can = Canvas(self.star1, height=768, width=1366)
        self.can.pack()
        self.img = PhotoImage(file='./image/p8.png')
        self.can.create_image(0, 0, image=self.img, anchor=NW)
        self.can.create_text((600,200),text="Do You want to Logout Your Account?",font=('',30,'bold'))
        self.btn1=Button(self.can,text="Yes",command=self.yes, fg='white',bg='black',font=('', 15, 'bold'))
        self.btn1.place(x=520,y=250)
        self.btn2=Button(self.can,text="No",command=self.no, fg='white',bg='black',font=('', 15, 'bold'))
        self.btn2.place(x=620,y=250)
        self.star1.resizable(height=False, width=False)
        self.star1.state("zoomed")
        self.star1.mainloop()
    def yes(self):
        exit()
    def no(self):
        self.star1.destroy()





