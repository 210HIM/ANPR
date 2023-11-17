from get_admin_data import *
from tkinter import *
from tkinter import messagebox

class Admin:
    def __init__(self,admin_id):
        self.root = None
        self.admin_id = admin_id
        self.obj = Conecter(self.admin_id)
        self.result = None

        file = open("Text/password.txt",'r')
        self.PWS = file.read()
        file.close()


    def Admin__data(self):
        self.root = Tk()
        self.root.wm_iconbitmap("Images/download.ico")
        self.root.title("Admin Information")
        self.root.geometry("400x400")

        Datafreame1=Frame(self.root,bd=5,padx=20,relief=RIDGE,bg="#19232d")
        Datafreame1.place(x=0,y=0,width=400,height=370)

        self.result = (self.obj.get_admin_data())

        #titille
        tile_lable=Label(Datafreame1,text='Admin Information',font=("times new roman",13,'bold'),relief=RAISED,fg="#e0e1e3",bg="#455364")
        tile_lable.grid(padx=0,pady=0)

        admin_id=Label(Datafreame1,text="Admin Id:",font=("arial",10,"bold"),padx=2,pady=4,fg="Black",bg="white",width=15)
        admin_id.grid(row=2,column=0,pady=5,padx=25,sticky=W)

        Name=Label(Datafreame1,text="Name:",font=("arial",10,"bold"),padx=2,pady=4,fg="Black",bg="white",relief=GROOVE,width=15)
        Name.grid(row=3,column=0,pady=5,padx=25,sticky=W)

        email=Label(Datafreame1,text="Email Id:",font=("arial",10,"bold"),padx=2,pady=4,fg="Black",bg="white",relief=GROOVE,width=15)
        email.grid(row=4,column=0,pady=15,padx=25,sticky=W)

        mobile_num=Label(Datafreame1,text="Mobile No:",font=("arial",10,"bold"),padx=2,pady=4,fg="Black",bg="white",relief=GROOVE,width=15)
        mobile_num.grid(row=5,column=0,pady=15,padx=25,sticky=W)

        password=Label(Datafreame1,text="Password:",font=("arial",10,"bold"),padx=2,pady=4,fg="Black",bg="white",relief=GROOVE,width=15)
        password.grid(row=6,column=0,pady=15,padx=25,sticky=W)

        # value

        val_admin_id=Label(Datafreame1,text=self.result[0],font=("arial",10,"bold"),padx=2,pady=4,fg="#e0e1e3",bg="#455364",relief=GROOVE,width=17)
        val_admin_id.grid(row=2,column=1,pady=15,sticky=W)

        val_Name=Label(Datafreame1,text=self.result[2],font=("arial",10,"bold"),padx=2,pady=4,fg="#e0e1e3",bg="#455364",relief=GROOVE,width=17)
        val_Name.grid(row=3,column=1,pady=15,sticky=W)

        val_email=Label(Datafreame1,text=self.result[3],font=("arial",10,"bold"),padx=2,pady=4,fg="#e0e1e3",bg="#455364",relief=GROOVE,width=17)
        val_email.grid(row=4,column=1,pady=15,sticky=W)

        val_mobile_num=Label(Datafreame1,text=self.result[4],font=("arial",10,"bold"),padx=2,pady=4,fg="#e0e1e3",bg="#455364",relief=GROOVE,width=17)
        val_mobile_num.grid(row=5,column=1,pady=15,sticky=W)

        val_password=Label(Datafreame1,text=self.result[1],font=("arial",10,"bold"),padx=2,pady=4,fg="#e0e1e3",bg="#455364",relief=GROOVE,width=17)
        val_password.grid(row=6,column=1,pady=15,sticky=W)

        #Button for LogOut 
        LogOut = Button(Datafreame1,command=quit,text = "LogOut",fg="black")
        LogOut.grid(row = 7, column = 2,sticky=W+E)

        #Button for Eite profile 
        Edit_butt = Button(Datafreame1,command=self.next_coll,text="Edit Profile",fg="black")
        Edit_butt.grid(row=7,column=0,sticky=W+E)

        #lower/exit buutn
        Datafreame2=Frame(self.root,bd=5,padx=20,bg='Black')
        Datafreame2.place(x=0,y=370,width=400,height=30)

        Exit=Button(Datafreame2,text='Back',command=self.Exit,bg='black',fg='white')
        Exit.place(x=335,y=0)


    def Exit(self):
        self.root.destroy()


    def next_coll(self):
        self.Exit()
        self.Edit_me()

    def Edit_me(self):
        self.root = Tk()
        self.root.wm_iconbitmap("Images/download.ico")
        self.root.title("AMPS/Admin Information")
        self.root.geometry("400x400")   

        Datafreame1=Frame(self.root,bd=5,padx=20,relief=RIDGE,bg="#19232d")
        Datafreame1.place(x=0,y=0,width=400,height=370)

        #titille
        tile_lable=Label(Datafreame1,text='Edit Profile',font=("times new roman",13,'bold'),relief=RAISED,fg="#e0e1e3",bg="#455364")
        tile_lable.grid(padx=0,pady=0)

        admin_id=Label(Datafreame1,text="Admin Id:",font=("arial",10,"bold"),padx=2,pady=4,fg="#e0e1e3",bg="#455364",relief=GROOVE,width=15)
        admin_id.grid(row=2,column=0,pady=15,padx=15,sticky=W)

        Name=Label(Datafreame1,text="Name:",font=("arial",10,"bold"),padx=2,pady=4,fg="#e0e1e3",bg="#455364",relief=GROOVE,width=15)
        Name.grid(row=3,column=0,pady=15,padx=15,sticky=W)

        email=Label(Datafreame1,text="Email Id:",font=("arial",10,"bold"),padx=2,pady=4,fg="#e0e1e3",bg="#455364",relief=GROOVE,width=15)
        email.grid(row=4,column=0,pady=15,padx=15,sticky=W)

        mobile_num=Label(Datafreame1,text="Mobile No:",font=("arial",10,"bold"),padx=2,pady=4,fg="#e0e1e3",bg="#455364",relief=GROOVE,width=15)
        mobile_num.grid(row=5,column=0,pady=15,padx=15,sticky=W)

        password=Label(Datafreame1,text="Password:",font=("arial",10,"bold"),padx=2,pady=4,fg="#e0e1e3",bg="#455364",relief=GROOVE,width=15)
        password.grid(row=6,column=0,pady=15,padx=15,sticky=W)

        #Entry
        self.admin_id_show=Label(Datafreame1,font=("arial",10,"bold"),text=self.admin_id,bg='#81c3e5',width=22,fg='black')
        self.admin_id_show.grid(row=2,column=1,padx=5)

        self.Name=Entry(Datafreame1,font=("arial",10,"bold"), bg='#81c3e5',width=22,fg='black')
        self.Name.grid(row=3,column=1,padx=5)

        self.email=Entry(Datafreame1,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.email.grid(row=4,column=1,padx=5)

        self.mobile_num=Entry(Datafreame1,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.mobile_num.grid(row=5,column=1,padx=5)

        self.password=Entry(Datafreame1,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.password.grid(row=6,column=1,padx=5)

        #Buttun for update
        Login_butt=Button(Datafreame1,text='Update',width=15,command=self.update)
        Login_butt.grid(row=9,column=1,pady=5)

        #lower/exit buutn
        Datafreame2=Frame(self.root,bd=5,padx=20,bg='Black')
        Datafreame2.place(x=0,y=370,width=400,height=30)

        Exit=Button(Datafreame2,text='Back',command=self.Exit,bg='black',fg='white')
        Exit.place(x=335,y=0)

    def set_data(self):
        self.Name_u = self.result[2]
        self.email_u = self.result[3]
        self.mobile_num_u = self.result[4]
        self.password_u = self.result[1]

    def update(self):
        self.set_data()
        Name = self.Name.get()
        Email = self.email.get()
        Password = self.password.get()
        Mobile_num = self.mobile_num.get()

        if Name != '':
            self.Name_u = Name
        if Email != '':
            self.email_u = Email
        if Mobile_num != '':
            self.mobile_num_u = Mobile_num
        if Password != '':
            self.password_u = Password

        self.conn=mysql.connector.connect(host="localhost",username="root",password=self.PWS,database="anpr_final_db")
        self.my_cursor=self.conn.cursor()
        
        sql = """UPDATE `anpr_final_db`.`admin_info` SET `password` = %s, `admin_name` = %s, `email` = %s, `mobile_num` = %s WHERE (`admin_id` = %s);"""
        data = (self.password_u,self.Name_u,self.email_u,self.mobile_num_u,self.admin_id)

        ans = messagebox.askquestion("Form","Do you wish to modify your profile?")
        if ans == 'yes':
            try:
                self.my_cursor.execute(sql, data)
                self.conn.commit()
                messagebox.showinfo('Upadet',"The profile has been updated.")
                self.root.destroy()
            except :
                messagebox.showwarning('showwarning',"The profile has not been updated., server problem !!")
            finally:
                self.conn.close()

        else:
            self.root.destroy()

# obj = Admin("admin_1")
# obj.Admin__data()
# mainloop()