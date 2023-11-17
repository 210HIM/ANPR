from Passwoed import *
from Data_base import *
import mysql
import mysql.connector
from Main_window import *
import smtplib
from email.message import EmailMessage
import random


class Admnin_data:

    def __init__(self,root):
        P = PASS_WORD()
        P.get_password()
        
        D = db()
        D.create_data_base()

        self.name = None
        self.admin_id = None
        self.mobile_num = None
        self.email = None
        self.password = None
        self._password = None
        self._admin_id = None

        #Login_fream root
        self.root = root

        #Mainwindo _ obj
        self.obj = None

        file = open("Text\password.txt",'r')
        self.passw = file.read()
        file.close()

        self.conn=mysql.connector.connect(host="localhost",username="root",password=self.passw,database="anpr_final_db")
        self.my_cursor=self.conn.cursor()

        sql='''SELECT * FROM anpr_final_db.admin_info'''
        self.my_cursor.execute(sql)
        self.result=self.my_cursor.fetchall();
        self.conn.close()
        #close connection here after completed programme @@@@@@

    def _result(self):
        self.conn=mysql.connector.connect(host="localhost",username="root",password=self.passw,database="anpr_final_db")
        self.my_cursor=self.conn.cursor()
        sql='''SELECT * FROM anpr_final_db.admin_info'''
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

        q1 = """INSERT INTO anpr_final_db.admin_info(admin_id,password,admin_name,email,mobile_num) VALUES(%s,%s,%s,%s,%s)"""
        data = (self.admin_id, self.msg4, self.msg1, self.msg2, self.msg3)
        try:
            self.my_cursor.execute(q1,data)
            self.conn.commit()
            msg='Congratulations your account has been created \n admin_id:-  '+self.admin_id
            messagebox.showinfo('Upadet',msg)
            sql='''SELECT * FROM anpr_final_db.admin_info'''
            self.my_cursor.execute(sql)
            self.result=self.my_cursor.fetchall();
        except:
            messagebox.showerror('Warning ',"The server is currently not responding.")
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
            return
        #Mobile nummber chcek
        if len(mobilno) == 10 :
            for i in range(len(self.result)):
                if mobilno in  list(self.result[i]):
                    #show erroe masege mobile number is incurect
                    messagebox.showwarning("Warning","The mobile number has already been registered, so please try again.")
                    return 12

        if len(mobilno) != 10:
            #show erroe masege mobile number is incurect
            messagebox.showwarning("Warning","The mobile number provided is invalid, and it is requested to be tried again.")
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

            if val == 12:
                self.msg3=self.mobile_num.delete(0,END)
                self.get_data(self.root  )
            

    def get_data(self,root):
        Datafreame2=Frame(root,background='#4caedb')
        Datafreame2.place(x=490,y=30,width=300,height=350)

        #title
        input_label=Label(Datafreame2,text='New User Registration',fg='white',bg='#013764',font=("times new roman",13,'bold'),relief=RAISED)
        input_label.grid(padx=0,pady=0,columnspan=2)

        temp_lable=Label(Datafreame2,bg='#4caedb')
        temp_lable.grid(row=1,column=0)

        #user_id
        Name=Label(Datafreame2,text="Name: ",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=2,column=0,pady=10,sticky=W)

        self.name=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.name.grid(row=2,column=1)

        #mobil_number
        Mobil_no=Label(Datafreame2,text="Mobile No: ",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=3,column=0,pady=10,sticky=W)

        self.mobile_num=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.mobile_num.grid(row=3,column=1)

        #email
        emil=Label(Datafreame2,text="Email-Id: ",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=4,column=0,pady=10,sticky=W)

        self.email=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.email.grid(row=4,column=1)

        #pass_word
        password=Label(Datafreame2,text="Password: ",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=5,column=0,pady=10,sticky=W)

        self.password=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.password.grid(row=5,column=1,padx=5)
        
        Login_butt=Button(Datafreame2,text='Register',width=15,command=self.take_data)
        Login_butt.grid(row=7,column=1,pady=10)

        BACK=Button(Datafreame2,text='Login',width=15,command=self.Login)
        BACK.grid(row=9,column=1,padx=5)


    def Register(self):
         self.get_data(self.root)

    def Login(self):
        Datafreame2=Frame(self.root,background='#4caedb')
        Datafreame2.place(x=490,y=30,width=300,height=350)  
        #title
        input_label=Label(Datafreame2,text='Login',fg='white',bg='#013764',font=("times new roman",13,'bold'),relief=RAISED,padx=10)
        input_label.grid(padx=0,pady=0,columnspan=2)

        temp_lable=Label(Datafreame2,bg='#4caedb')
        temp_lable.grid(row=1,column=0)

        #user_id
        user_id=Label(Datafreame2,text="USER-ID:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=2,column=0,pady=15,sticky=W)

        self.admin_id=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.admin_id.grid(row=2,column=1,padx=5)

        #pass_word
        Password=Label(Datafreame2,text="Password:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=3,column=0,pady=15,sticky=W)

        self.password=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black',show = '*')
        self.password.grid(row=3,column=1,padx=5)

        Login_butt=Button(Datafreame2,text='Sign In',width=15,command=self.Login_take_chek)
        Login_butt.grid(row=5,column=1)

        Forget_pass=Button(Datafreame2,text='Forgot Password?',width=15,command=self.reset_password)
        Forget_pass.grid(row=7,column=1,pady=15)

        register_pass=Button(Datafreame2,text='New User',width=15,command=self.Register)
        register_pass.grid(row=8,column=1)

    def Login_take_chek(self):
        admin_id=self.admin_id.get()
        password=self.password.get()
        # new updated data from _result function 
        conn=mysql.connector.connect(host="localhost",username="root",password=self.passw,database="anpr_final_db")
        my_cursor=conn.cursor()

        sql=f"SELECT * FROM anpr_final_db.admin_info where admin_id = '{admin_id}';"

        try:
            my_cursor.execute(sql)
            result = my_cursor.fetchall()
        except:
            messagebox.showwarning("warning","The server is currently not responding.")
        finally:
            conn.close()

        if password == result[0][1]:
            print("sucefully login !")
            messagebox.showinfo('Upadet',"Successfully logged In.")
            self.root.destroy()
            self.obj = Main_windows(admin_id=admin_id)
        else: 

            messagebox.showwarning('showwarning',"The password provided is incorrect.")

    def reset_password(self):
        Datafreame2=Frame(self.root,background='#4caedb')
        Datafreame2.place(x=490,y=30,width=300,height=350)

        #title
        input_label=Label(Datafreame2,text='Reset Password',fg='white',bg='#013764',font=("times new roman",13,'bold'),relief=RAISED)
        input_label.grid(padx=0,pady=0,columnspan=2)

        temp_lable=Label(Datafreame2,bg='#4caedb')
        temp_lable.grid(row=1,column=0,padx=10) 
        
        #email
        emil=Label(Datafreame2,text="Email -Id:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=2,column=0,pady=15,sticky=W)

        self.email=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.email.grid(row=2,column=1,padx=5)

        Login_butt=Button(Datafreame2,text='Send Otp',width=15,command=self.check_Email_in_db)
        Login_butt.grid(row=3,column=1,pady=5)

    def check_Email_in_db(self):

        conn=mysql.connector.connect(host="localhost",username="root",password=self.passw,database="anpr_final_db")
        my_cursor=conn.cursor()

        sql = f"SELECT * FROM anpr_final_db.admin_info where email = '{self.email.get()}';"

        try:
            my_cursor.execute(sql)
            self.my_result = my_cursor.fetchall()
        except:
            messagebox.showerror('Error',"The server is currently not responding .")
        finally:
            conn.close()
    
        if self.email.get() == self.my_result[0][3]:
                self.Otp_Eamil()
        else:
            messagebox.showerror('Error',"The user is not registered in our system.")
            
    def Otp_Eamil(self):
        self.OTP=random.randint(10000,99999)
        print(self.OTP,"yes itis me to say you")
        addreas = self.email.get()
        print(addreas)
        try:
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login('rytcareer14@gmail.com','nqmmdsxvgfzyguxw')
            masg="""Dear user \nYour one time password:"""+str(self.OTP )+"""Please note that the one time password is valid for only one session.If you did not request a one time password please connect with us immediately at rytcareer14@gmail.com.\nRegards,Automatic License/Number Plate Recognition (ANPR)"""
            email = EmailMessage()
            #email['From'] =
            email['To'] =addreas
            email['Subject'] = 'OTP'
            email.set_content(masg)
            server.send_message(email)
        except:
            messagebox.showerror('Error',"The internet connection is not scalable.")
        
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

            self.admin_id=Label(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black',text = self.my_result[0][0])
            self.admin_id.grid(row=2,column=1,padx=5)

            #pass_word
            password=Label(Datafreame2,text="Password:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=3,column=0,pady=15,sticky=W)

            self.password=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
            self.password.grid(row=3,column=1,padx=5)
        
            Login_butt=Button(Datafreame2,text='Login',width=15,command=self.set_new_Password)
            Login_butt.grid(row=4,column=1,padx=5)
        
        else:
            self.temp()
            messagebox.showwarning("Warning","OTP is Incorrect")
            

    def set_new_Password(self):
        Pass = str(self.password.get())
        admin_id = self.my_result[0][0]
        self.conn=mysql.connector.connect(host="localhost",username="root",password=self.passw,database="anpr_final_db")
        self.my_cursor=self.conn.cursor()
        sql = '''UPDATE `anpr_final_db`.`admin_info` SET `password` = %s WHERE (`admin_id` = %s);'''
        data = (Pass , admin_id)
        try:
            self.my_cursor.execute(sql,data)
            self.conn.commit()
            messagebox.showinfo("Infornetion","The new password has been updated.")
            self.Login()
        except:
            messagebox.showwarning("Warning","The new password has not been updated.")
        finally:
            self.conn.close()


