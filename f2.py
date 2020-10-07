from tkinter import *
import database
from tkinter import filedialog,messagebox
import shutil
import os
import filedatabase
class hey:
    def __init__(self):
        self.star=Toplevel()
        self.star.geometry('1366x768')
        self.can = Canvas(self.star, height=768, width=1366)
        self.can.pack()
        self.img = PhotoImage(file='./image/654.png')
        self.can.create_image(0, 0, image=self.img, anchor=NW)
        self.can.create_text((260, 250), text="Name --", fill='#000000', font=('monaco', 20, "bold"))
        self.ent1=Entry(self.can)
        self.ent1.place(x=340, y=240)
        self.can.create_text((272, 280),text="Amount --", fill='#000000', font=('monaco', 20, "bold"))
        self.ent2 = Entry(self.can)
        self.ent2.place(x=340, y=270)
        self.btn1 = Button(self.can, text="<- Back", fg='white', bg='black', font=('monaco', 15, 'bold'), command=self .back)
        self.btn1.place(x=200, y=400)
        self.btn=Button(self.can, text="Submit", fg='white', bg='black', font=('monaco', 15, 'bold'), command=self .printdata)
        self.btn.place(x=360, y=400)
        self.star.resizable(height=False,width=False)
        self.star.state("zoomed")
        self.star.mainloop()

    def image(self):
        s = filedialog.askopenfilename(filetypes=(("Images(PNG)", "*.png"),("Images(JPG)", "*.jpg")))
        self.dd = s
        target = './uploads/'
        cwd = os.getcwd()

        cwd = cwd + "\\uploads\\"

        target = os.path.join(target, os.path.dirname(s))

        # adding exception handling
        try:
            shutil.copy(s, cwd)
        except IOError as e:
            print("Unable to copy file. %s" % e)
        except:
            print("Unexpected error:", sys.exc_info())
        y = s.split('/')
        return(y[len(y)-1])

    def printdata(self):
        if self.ent1.get() != "" and self.ent2.get() != "":
            im = self.image()
            ob = database.Database()
            tup = (self.ent1.get(), self.ent2.get(), im)
            # ob.insertData(tup)
            try:
                filedatabase.insertData(tup,self.dd)
                messagebox.showinfo("Success", "Pizza has been added")
                self.star.destroy()
            except:
                messagebox.showinfo("Error","Image is curropted")

        elif self.ent1.get() == ""and self.ent2.get() != "":
            self.can.create_text((680, 250), text="Please Enter in the block first", fill='red', font=('monaco', 15, "bold"))
        elif self.ent1.get() != ""and self.ent2.get() == "":
            self.can.create_text((680, 280), text="Please Enter in the block first", fill='red', font=('monaco', 15, "bold"))
        else:
            self.can.create_text((680, 280), text="Please Enter in the block first", fill='red', font=('monaco', 15, "bold"))
            self.can.create_text((680, 250), text="Please Enter in the block first", fill='red', font=('monaco', 15, "bold"))
    def back(self):
        self.star.destroy()





