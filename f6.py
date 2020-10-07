from tkinter import *
from tkinter.ttk import Treeview
import database,updatemenu2
class hey:
    def __init__(self):
        self.star1 = Toplevel()
        self.obj = database.Database()
        self.result = self.obj.getmenu2()
        self.star1.geometry('1366x768')
        self.can = Canvas(self.star1, height=768, width=1366)
        self.can.pack()
        self.img = PhotoImage(file='./image/roll.png')
        self.can.create_image(0, 0, image=self.img, anchor=NW)
        self.table = Treeview(self.can, columns=("#0", "#1", "#2", "#3", "#4", "#5", "#6","#7"))
        self.table.heading('#0', text="Sr no.")
        self.table.column('#0', width=10)
        self.table.heading('#1', text="Name")
        self.table.column('#1', width=100)
        self.table.heading('#2', text="Gender")
        self.table.column('#2', width=50)
        self.table.heading('#3', text="email")
        self.table.column('#3', width=100)
        self.table.heading('#4', text="password")
        self.table.column('#4', width=100)
        self.table.heading('#5', text="contact")
        self.table.column('#5', width=100)
        self.table.heading('#6', text="address")
        self.table.column('#6', width=100)
        self.table.heading('#7', text="edit")
        self.table.column('#7', width=100)
        self.table.heading('#8', text="delete")
        self.table.column('#8', width=100)
        for i in self.result:
            self.table.insert('','end',text=i[0], values=( i[1], i[2],i[3],i[4],i[5],i[6],"edit","Delete"))
        self.table.place(x=300, y=300)
        self.btn = Button(self.can, text="<- Back", fg='white', bg='black', font=('monaco', 15, 'bold'),command=self.back)
        self.btn.place(x=950, y=540)
        self.table.bind("<Double-Button-1>", self.trigger)
        self.star1.resizable(height=False, width=False)
        self.star1.state("zoomed")
        self.star1.mainloop()

    def back(self):
        self.star1.destroy()
    def trigger(self,e):
        f = self.table.focus()
        x = self.table.item(f)
        col = self.table.identify_column(e.x)
        if (col == "#7"):
            self.star1.destroy()
            obj=updatemenu2.UpdateMenu(x["text"])
        elif (col == "#8"):
            self.star1.destroy()
            d = database.Database()
            d.delete1(x["text"])


