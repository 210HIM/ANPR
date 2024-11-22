from get_admin_data import *
from tkinter import *

class Admin:
    def __init__(self,admin_id):
        self.s_root = None
        self.admin_id = admin_id
        self.obj = Conecter(self.admin_id)
        self.result = None

    def Exit(self):
        self.info_root.destroy()

    def Admin__data(self):
        self.info_root = Tk()
        self.info_root.title("Admin Information")
        self.info_root.geometry("400x400")

        Datafreame1=Frame(self.info_root,bd=5,padx=20,bg='#ffeecd',relief=RIDGE,)
        Datafreame1.place(x=0,y=0,width=400,height=370)

        self. result = (self.obj.get_admin_data())


        #titille
        tile_lable=Label(Datafreame1,text='Admin Information',fg='Black',bg='#fff4cd',font=("times new roman",13,'bold'),relief=RAISED)
        tile_lable.grid(padx=0,pady=0)

        admin_id=Label(Datafreame1,text="Admin Id:",font=("arial",10,"bold"),padx=2,pady=4,fg='Black',bg='#f6f8fa')
        admin_id.grid(row=2,column=0,pady=15,sticky=W)

        Name=Label(Datafreame1,text="Name:",font=("arial",10,"bold"),padx=2,pady=4,fg='Black',bg='#f6f8fa')
        Name.grid(row=3,column=0,pady=15,sticky=W)

        email=Label(Datafreame1,text="Email Id:",font=("arial",10,"bold"),padx=2,pady=4,fg='Black',bg='#f6f8fa')
        email.grid(row=4,column=0,pady=15,sticky=W)

        mobile_num=Label(Datafreame1,text="Mobile No:",font=("arial",10,"bold"),padx=2,pady=4,fg='Black',bg='#f6f8fa')
        mobile_num.grid(row=5,column=0,pady=15,sticky=W)

        password=Label(Datafreame1,text="Password:",font=("arial",10,"bold"),padx=2,pady=4,fg='Black',bg='#f6f8fa')
        password.grid(row=6,column=0,pady=15,sticky=W)

        # value

        val_admin_id=Label(Datafreame1,text=self.result[0],font=("arial",10,"bold"),padx=2,pady=4,fg='Black',bg='#f6f8fa')
        val_admin_id.grid(row=2,column=1,pady=15,sticky=W)

        val_Name=Label(Datafreame1,text=self.result[1],font=("arial",10,"bold"),padx=2,pady=4,fg='Black',bg='#f6f8fa')
        val_Name.grid(row=3,column=1,pady=15,sticky=W)

        val_email=Label(Datafreame1,text=self.result[2],font=("arial",10,"bold"),padx=2,pady=4,fg='Black',bg='#f6f8fa')
        val_email.grid(row=4,column=1,pady=15,sticky=W)

        val_mobile_num=Label(Datafreame1,text=self.result[4],font=("arial",10,"bold"),padx=2,pady=4,fg='Black',bg='#f6f8fa')
        val_mobile_num.grid(row=5,column=1,pady=15,sticky=W)

        val_password=Label(Datafreame1,text=self.result[3],font=("arial",10,"bold"),padx=2,pady=4,fg='Black',bg='#f6f8fa')
        val_password.grid(row=6,column=1,pady=15,sticky=W)

        #lower/exit buutn
        Datafreame2=Frame(self.info_root,bd=5,padx=20,bg='Black')
        Datafreame2.place(x=0,y=370,width=400,height=30)

        Exit=Button(Datafreame2,text='Exit',command=self.Exit,bg='black',fg='white')
        Exit.place(x=335,y=0)









