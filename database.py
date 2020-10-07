import f5
import f6
import mysql.connector
user=None
class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            user="root",
            passwd="root",
            host="localhost",
            database="pizzadelivery")
        self.cursor = self.mydb.cursor()
    def checkadmin0(self):
        self.cursor.execute("SELECT  `email`, `password` FROM `admin`")
        return (self.cursor.fetchone())

    def checkadmin(self,tup):
        self.cursor.execute("SELECT * FROM `admin` where email=%s and `password`=%s ",tup)
        return(self.cursor.fetchone())

    def insertData(self, tup):
        self.cursor.execute("""
        INSERT INTO `menu`( `name`, `amount`,`photo`) VALUES
         (%s,%s,%s)
        """, tup)
        self.mydb.commit()
    def insertData2(self,tup):
        self.cursor.execute("""
        INSERT INTO `worker`( `name`, `gender` ,`email`, `password`, `contact`, `address`) VALUES
         (%s,%s,%s,%s,%s,%s)
        """, tup)
        self.mydb.commit()
    def insertData3(self,tup):
        self.cursor.execute("""
        INSERT INTO `admin`( `email`, `password`) VALUES
         (%s,%s)
        """, tup)
        self. mydb.commit()
    def getmenu(self):
        self.cursor.execute("SELECT * FROM `menu`")
        return(self.cursor.fetchall())
    def getmenu2(self):
        self.cursor.execute("SELECT *FROM `worker` ")
        return(self.cursor.fetchall())
    def getmenubyid(self,id_):
        self.cursor.execute("SELECT * FROM `menu` where id=%s", (id_,))
        return(self.cursor.fetchone())
    def getmenu2byid(self,id_):
        self.cursor.execute("SELECT * FROM `worker` where id=%s", (id_,))
        return(self.cursor.fetchone())
    def update1(self,tup):
        self.cursor.execute("""
         UPDATE `menu` SET `name`=%s,`amount`=%s where `id`=%s 
        """,tup)
        self.mydb.commit()
    def update2(self, tup):
        self.cursor.execute("""
         UPDATE `worker` SET `name`=%s,`gender`=%s,`email`=%s,`password`=%s,`contact`=%s,`address`=%s where `id`=%s
        """, tup)
        self.mydb.commit()
    def delete(self,id_):
        self.cursor.execute("DELETE FROM `menu` where `id`=%s", (id_,))
        self.mydb.commit()
        obj=f5.hey()
    def delete1(self,id_):
        self.cursor.execute("DELETE FROM `worker` where `id`=%s", (id_,))
        self.mydb.commit()
        obj = f6.hey()

    def updatepassword(self,admi, passw):
        self.cursor.execute("UPDATE `admin` set `email`=%s,`password`=%s where `id` = %s",(admi,passw,user[0]))
        self.mydb.commit()

    def updatepassword1(self, admi, passw):
        self.cursor.execute("UPDATE `admin` set `email`=%s,`password`=%s where `id` = %s", (admi, passw,228))
        self.mydb.commit()


