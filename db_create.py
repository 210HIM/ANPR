import mysql 
import mysql.connector
from tkinter import *
from tkinter import messagebox
from Main_window import *
import smtplib
from email.message import EmailMessage
import random

def create_db():
    conn=mysql.connector.connect(host="localhost",username="root",password="rakesh",database="admin_data")
    my_cursur = conn.cursor()

    q1="""CREATE TABLE IF NOT EXISTS `admin_data`.`admin_info` (
    `admin_id` VARCHAR(45) NOT NULL,
    `password` VARCHAR(45) NOT NULL,
    `admin_name` VARCHAR(45) NOT NULL,
    `email` VARCHAR(45) NOT NULL,
    `mobile_num` VARCHAR(45) NOT NULL,
    PRIMARY KEY (`admin_id`));"""
    try:
        my_cursur.execute(q1)
        conn.commit()
    except:
        messagebox.showerror('showerror',"Server not responding! 1")
    finally:
        conn.close()



class Admnin_data:

    def __init__(self,root):
        self.name = None
        self.admin_id = None
        self.mobile_num = None
        self.email = None
        self.password = None

        self._password = None
        self._admin_id = None

        # Login_fream root
        self.root = root

        # Mainwindo _ obj
        self.obj = None


        self.conn=mysql.connector.connect(host="localhost",username="root",password="rakesh",database="admin_data")
        self.my_cursor=self.conn.cursor()
        sql='''SELECT * FROM admin_data.admin_info'''
        self.my_cursor.execute(sql)
        self.result=self.my_cursor.fetchall();
        #close connection here after completed programme @@@@@@

    #    print(self.result)

    def _result(self):
        self.conn=mysql.connector.connect(host="localhost",username="root",password="rakesh",database="admin_data")
        self.my_cursor=self.conn.cursor()
        sql='''SELECT * FROM admin_data.admin_info'''
        self.my_cursor.execute(sql)
        self.result=self.my_cursor.fetchall();
        self.conn.close()

        return self.result

    def add_admin(self):
        #user_id creation 
        if len(self.result) > 0:
            temp=list(self.result[-1])
            x=temp[0]
            a,b=x.split('_')
            self.admin_id='admin_'+str(int(b)+1)
        else:
            self.admin_id = "admin_1"

        print(f"{self.admin_id},{self.msg1},{self.msg4},{self.msg2},{self.msg3}")

        q1 = """INSERT INTO admin_data.admin_info(admin_id,password,admin_name,email,mobile_num) VALUES(%s,%s,%s,%s,%s)"""
        data = (self.admin_id, self.msg4, self.msg1, self.msg2, self.msg3)
        try:
            self.my_cursor.execute(q1,data)
            self.conn.commit()
            msg='Congratulations your account has been created \n admin_id:-  '+self.admin_id
            messagebox.showinfo('Upadet',msg)
            sql='''SELECT * FROM admin_data.admin_info'''
            self.my_cursor.execute(sql)
            self.result=self.my_cursor.fetchall();
        except:
            print("not done")
            messagebox.showerror('showerror',"server not responding ! 2")
        finally:
            self.conn.close()

        self.Login()

    def print_msg(self,titel,msg):
        messagebox.showinfo(titel,msg)

    def check_data(self,name,password,mobilno,email):
        # check all data is fille or not 
        if len(name) == 0 or len(mobilno) == 0 or len(password) == 0 or len(email)==0:
            messagebox.showwarning('Warning','Fill all data')
            self.get_data(self.root)

        #chck name is coorect or not
        if name.isalpha() == False:
            self.print_msg('showerror','Name contains only characters')
            return 10

        #Mobile nummber chcek
        if len(mobilno) == 10 :
            for i in range(len(self.result)):
                if mobilno in  list(self.result[i]):
                    #show erroe masege mobile number is incurect
                    messagebox.showwarning("Warning","Mobile no. is already registered please try again")
                    return 12
        else:
            #show erroe masege mobile number is incurect
            messagebox.showwarning("Warning","Mobile no. is invalid please try again")
            return 12

        return 1


    
    def take_data(self):
        self.msg1=self.name.get()
        self.msg2=self.email.get()
        self.msg3=self.mobile_num.get()
        self.msg4=self.password.get()

        val=self.check_data(name=self.msg1,password=self.msg2,mobilno=self.msg3,email=self.msg4)

        if val == 1:
            self.add_admin()
            
        else:
            if val == 10:
                self.msg1=self.name.delete(0,END)
                self.get_data(self.root)
            # val=check_data(name=msg1,password=msg2,mobilno=msg3,email=msg4)


            elif val == 12:
                self.msg3=self.mobile_num.delete(0,END)
                self.get_data(self.root  )
            # val=check_data(name=msg1,password=msg2,mobilno=msg3,email=msg4)
            
           
        


    def get_data(self,root):
        Datafreame2=Frame(root,background='#4caedb')
        Datafreame2.place(x=490,y=30,width=300,height=350)

        #title
        input_label=Label(Datafreame2,text='Registration',fg='white',bg='#013764',font=("times new roman",13,'bold'),relief=RAISED)
        input_label.grid(padx=0,pady=0)

        temp_lable=Label(Datafreame2,bg='#4caedb')
        temp_lable.grid(row=1,column=0,padx=10)

        #user_id
        Name=Label(Datafreame2,text="Name:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=2,column=0,pady=15,sticky=W)

        self.name=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.name.grid(row=2,column=1,padx=5)

        #mobil_number
        Mobil_no=Label(Datafreame2,text="Mobil No:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=3,column=0,pady=15,sticky=W)

        self.mobile_num=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.mobile_num.grid(row=3,column=1,padx=5)

        #email
        emil=Label(Datafreame2,text="Email -Id:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=4,column=0,pady=15,sticky=W)

        self.email=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.email.grid(row=4,column=1,padx=5)

        #pass_word
        password=Label(Datafreame2,text="Password:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=5,column=0,pady=15,sticky=W)

        self.password=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.password.grid(row=5,column=1,padx=5)
        
        Login_butt=Button(Datafreame2,text='Register',width=15,command=self.take_data)
        Login_butt.grid(row=7,column=1,pady=5)

        BACK=Button(Datafreame2,text='Login',width=15,command=self.Login)
        BACK.grid(row=9,column=1,padx=5)

    def Register(self):
         self.get_data(self.root)

    def Login(self):
        Datafreame2=Frame(self.root,background='#4caedb')
        Datafreame2.place(x=490,y=30,width=300,height=350)  
        #title
        input_label=Label(Datafreame2,text='Login',fg='white',bg='#013764',font=("times new roman",13,'bold'),relief=RAISED,padx=10)
        input_label.grid(padx=0,pady=0)

        temp_lable=Label(Datafreame2,bg='#4caedb')
        temp_lable.grid(row=1,column=0)

        #user_id
        user_id=Label(Datafreame2,text="USER -ID:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=2,column=0,pady=15,sticky=W)

        self.admin_id=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.admin_id.grid(row=2,column=1,padx=5)

        #pass_word
        Password=Label(Datafreame2,text="Password:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=3,column=0,pady=15,sticky=W)

        self.password=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.password.grid(row=3,column=1,padx=5)
        Login_butt=Button(Datafreame2,text='Sig in',width=15,command=self.Login_take_chek)
        Login_butt.grid(row=5,column=1)

        BACK=Button(Datafreame2,text='Register',width=15,command=self.Register)
        BACK.grid(row=7,column=1,pady=15)

        Forget_pass=Button(Datafreame2,text='Forget Password',width=20,command=self.reset_password)
        Forget_pass.grid(row=7,column=1,pady=15)

    def Login_take_chek(self):
        admin_id=self.admin_id.get()
        password=self.password.get()
        # new updated data from _result function 
        self.result = self._result() 
        for item in self.result:
            if admin_id in item and password in item:
                print("sucefully login !")
                messagebox.showinfo('Upadet',"sucefully login !")
                self.root.destroy()
                self.obj = Main_windows(admin_id=admin_id)
                break
        else: 
            print("not login !")
            messagebox.showwarning('showwarning',"User_id,Password not present !")

    def reset_password(self):
        Datafreame2=Frame(self.root,background='#4caedb')
        Datafreame2.place(x=490,y=30,width=300,height=350)

        #title
        input_label=Label(Datafreame2,text='Reset Password',fg='white',bg='#013764',font=("times new roman",13,'bold'),relief=RAISED)
        input_label.grid(padx=0,pady=0)

        temp_lable=Label(Datafreame2,bg='#4caedb')
        temp_lable.grid(row=1,column=0,padx=10)

        
        #email
        emil=Label(Datafreame2,text="Email -Id:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=2,column=0,pady=15,sticky=W)

        self.email=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.email.grid(row=2,column=1,padx=5)


        Login_butt=Button(Datafreame2,text='Send Otp',width=15,command=self.Otp_Eamil)
        Login_butt.grid(row=3,column=1,pady=5)

        
    def Otp_Eamil(self):
        self.OTP=random.randint(10000,99999)
        print(self.OTP)
        addreas = self.email.get()
        print(addreas)
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('rytcareer14@gmail.com','nqmmdsxvgfzyguxw')
        masg="""Dear user \nYour one time password:"""+str(self.OTP )+"""Please note that the one time password is valid for only one session.]nIf you did not request a one time password please connect with us immediately at rytcareer14@gmail.com.\nRegards,Automatic License/Number Plate Recognition (ANPR)"""

        email = EmailMessage()
        #email['From'] =
        email['To'] =addreas
        email['Subject'] = 'OTP'
        email.set_content(masg)
        server.send_message(email)

        self.temp()
        
    def temp(self):
        Datafreame2=Frame(self.root,background='#4caedb')
        Datafreame2.place(x=490,y=30,width=300,height=350)

        #title
        input_label=Label(Datafreame2,text='OTP Check',fg='white',bg='#013764',font=("times new roman",13,'bold'),relief=RAISED)
        input_label.grid(padx=0,pady=0)

        temp_lable=Label(Datafreame2,bg='#4caedb')
        temp_lable.grid(row=1,column=0,padx=10)

        
        #email
        otp=Label(Datafreame2,text="Enter OTP:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=2,column=0,pady=15,sticky=W)

        self.user_otp=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.user_otp.grid(row=2,column=1,padx=5)


        Login_butt=Button(Datafreame2,text='Set Password',width=15,command=self.chek_OTP)
        Login_butt.grid(row=3,column=1,pady=5)

    def chek_OTP(self):
        otp = self.user_otp.get()
        print(f"{otp}=={self.OTP}")

        if  str(otp) == str(self.OTP):
            Datafreame2=Frame(self.root,background='#4caedb')
            Datafreame2.place(x=490,y=30,width=300,height=350)

            #title
            input_label=Label(Datafreame2,text='Set Password',fg='white',bg='#013764',font=("times new roman",13,'bold'),relief=RAISED)
            input_label.grid(padx=0,pady=0)

            temp_lable=Label(Datafreame2,bg='#4caedb')
            temp_lable.grid(row=1,column=0,padx=10)

            #admin_id
            admin=Label(Datafreame2,text="Admin ID:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=2,column=0,pady=15,sticky=W)

            self.admin_id=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
            self.admin_id.grid(row=2,column=1,padx=5)

            #pass_word
            password=Label(Datafreame2,text="Password:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=3,column=0,pady=15,sticky=W)

            self.password=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
            self.password.grid(row=3,column=1,padx=5)
        

            Login_butt=Button(Datafreame2,text='Login',width=15,command=self.set_new_Password)
            Login_butt.grid(row=4,column=1,padx=5)
        
        else:
            self.temp()
            print("otp is wrong")

    def set_new_Password(self):
        Pass = str(self.password.get())
        admin_id = str(self.admin_id.get())
        self.conn=mysql.connector.connect(host="localhost",username="root",password="rakesh",database="admin_data")
        self.my_cursor=self.conn.cursor()
        sql = '''UPDATE `admin_data`.`admin_info` SET `password` = %s WHERE (`admin_id` = %s);'''
        data = (Pass , admin_id)
        print(admin_id)
        try:
            self.my_cursor.execute(sql,data)
            self.conn.commit()
            print("Password chnage and save")
            self.Login()
        except:
            print("New password is not change and save ")
        finally:
            self.conn.close()



                




                









