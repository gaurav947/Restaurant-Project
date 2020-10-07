from tkinter import *
from tkinter.ttk import Treeview
import database
import updatemenu

class hey:
    def __init__(self):
        self.star1 = Toplevel()
        self.obj = database.Database()
        self.result = self.obj.getmenu()
        self.star1.geometry('1366x768')
        self.can = Canvas(self.star1, height=768, width=1366)
        self.can.pack()
        self.img = PhotoImage(file='./image/654.png')
        self.can.create_image(0, 0, image=self.img, anchor=NW)
        self.table = Treeview(self.can, columns=("#0", "#1", "#2", "#3","#4"))
        self.table.heading('#0', text="Sr no.")
        self.table.column('#0', width=40)
        self.table.heading('#1', text="Name")
        self.table.column('#1', width=100)
        self.table.heading('#2', text="Amount")
        self.table.column('#2', width=100)
        self.table.heading('#3', text="edit")
        self.table.column('#3', width=100)
        self.table.heading('#4', text="delete")
        self.table.column('#4', width=100)
        for i in self.result:
            self.table.insert('', 'end',text=i[0], values=(i[1], i[2],"edit","Delete"))
        self.table.place(x=300, y=300)
        self.btn = Button(self.can, text="<- Back", fg='white', bg='black', font=('monaco', 15, 'bold'),command=self.back)
        self.btn.place(x=810, y=540)
        self.table.bind("<Double-Button-1>",self.trigger)
        self.star1.resizable(height=False, width=False)
        self.star1.state("zoomed")
        self.star1.mainloop()
    def back(self):
        self.star1.destroy()
    def trigger(self,e):
        f=self.table.focus()
        x=self.table.item(f)
        col=self.table.identify_column(e.x)
        if(col=="#3"):
            self.star1.destroy()
            obj = updatemenu.UpdateMenu(x["text"])
        elif(col=="#4"):
            self.star1.destroy()
            d = database.Database()
            d.delete(x["text"])







