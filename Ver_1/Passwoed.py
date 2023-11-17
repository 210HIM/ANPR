from tkinter import *
import os

class PASS_WORD:
    def __init__(self):
        self.PSW = None
        self.root = None
        self.isExist = False

    def get_password(self):
        path = "Text\password.txt"
        self.isExist = os.path.exists(path)

        if self.isExist == False:
            self.root = Tk()
            self.root.geometry("400x150")
            self.root.title("ANPR/DataBase conection")
            self.root.wm_iconbitmap("Images/download.ico")
            

            moto = Label(self.root,text="This information only tekean one time for to conect Database",font=('arial' , 10 , 'bold'))
            moto.place(x = 2, y = 5)

            L=Label(self.root , text= "Enter password : ",font=('arial' , 8 , 'bold'))
            L.place(x = 10, y = 50)

            self.password = Entry(self.root , font=('arial' , 11 , 'bold'))
            self.password.place(x = 130 , y = 50)

            B_1=Button(self.root,text = "Process",command=self.Take_data,font=('arial' , 9 , 'bold'))
            B_1.place(x=210,y=90)

            B_2 = Button(self.root,text="Exit",font=('arial' , 9 , 'bold'),command=self.Exit)
            B_2.place(x=363,y = 120)

        if self.isExist == True:
            return 

    def Take_data(self):
        self.PSW = self.password.get()
        file = open("Text/password.txt",'w+')
        file.write(self.PSW)
        file.close()
        self.Exit()
        
                
    def Exit(self):
        self.root.destroy()
