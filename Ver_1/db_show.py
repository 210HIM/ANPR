from tkinter import *
import mysql
import mysql.connector
class TBl:
    def __init__(self):
        self.root = None
        file = open("Text\password.txt",'r')
        self.PWS = file.read()
        file.close()

        self.conn=mysql.connector.connect(host="localhost",username="root",password=self.PWS,database="anpr_final_db")
        self.my_cursor=self.conn.cursor()
        sql='''SELECT * FROM anpr_final_db.admin_info'''
        self.my_cursor.execute(sql)
        self.result=self.my_cursor.fetchall();

    def tabel(self):
        self.root = Tk()
        self.root.wm_iconbitmap("Images/download.ico")
        # code for creating table
        for i in range(len(self.result)):
            for j in range(len(self.result[0])):
                 
                self.e = Entry(self.root, width=20, fg='blue',font=('Arial',16,'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, self.result[i][j])