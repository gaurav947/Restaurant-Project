import mysql.connector
from mysql.connector import MySQLConnection
from mysql.connector import Error
import sys
from pytz import unicode
xyz = None

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="pizzadelivery"
)

cursor = con.cursor(buffered=True)

def insertData(tup,img):
    path = img
    image = convertToBinaryData(path)
    ls = list(tup)
    ls.append(image)
    conn = MySQLConnection(host="localhost",
                           user="root",
                           passwd="root",
                           database="pizzadelivery")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO `menu`( `name`, `amount`,`photo`,`image`) VALUES
     (%s,%s,%s,%s)
    """, ls)
    conn.commit()

def fetch_image():
    try:
        conn = MySQLConnection(host="localhost",
                               user="root",
                               passwd="root",
                               database="pizzadelivery")

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `menu` ")
        return cursor.fetchall()
        # for row in cursor.fetchall():
        #     write_file(row[4],row[3])

        # for row in rs:
        #     print(row[0])
        #write_file(file,'photo.png')
    except mysql.connector.Error as error:
        con.rollback()
        print("Failed to read BLOB data from MySQL table {}".format(error))

def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

# fetch_image()