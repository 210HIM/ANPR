import mysql 
import mysql.connector
from tkinter import *
from tkinter import messagebox
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
        print("not done")
    finally:
        conn.close()



class Admnin_data:

    def __init__(self):
        self.name = ''
        self.admin_id = ''
        self.mobile_num = ''
        self.email = ''
        self.password = ''


        self.conn=mysql.connector.connect(host="localhost",username="root",password="rakesh",database="admin_data")
        self.my_cursor=self.conn.cursor()
        sql='''SELECT * FROM admin_data.admin_info'''
        self.my_cursor.execute(sql)
        self.result=self.my_cursor.fetchall();
        #close connection here after completed programme @@@@@@

    #    print(self.result)

    def add_admin(self):
        #user_id creation 
        if len(self.result) > 0:
            temp=list(self.result[-1])
            x=temp[0]
            a,b=x.split('_')
            self.admin_id='admin_'+str(int(b)+1)
        else:
            self.admin_id = "admin_1"

        print(f"{self.admin_id},{self.password},{self.name},{self.mobile_num},{self.email}")

        q1 = """INSERT INTO admin_data.admin_info(admin_id,password,admin_name,email,mobile_num) VALUES(%s,%s,%s,%s,%s)"""
        data = (self.admin_id, self.password, self.name, self.email, self.mobile_num)
        try:
            self.my_cursor.execute(q1,data)
            self.conn.commit()
        except:
            print("not done")
        finally:
            self.conn.close()

    def print_msg(self,titel,msg):
        messagebox.showinfo(titel,msg)

    def check_data(self,name,password,mobilno,email):
        # check all data is fille or not 
        if len(name) == 0 or len(mobilno) == 0 or len(password) == 0 or len(email)==0:
            messagebox.showwarning('Warning','Fill all data')
            self.get_data()

        #chck name is coorect or not
        if name.isalpha() == False:
            self.print_msg('Information','Name contains o nly characters')
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
            messagebox.showwarning("Information","Mobile no. is invalid please try again")
            return 12


    
    def take_data(self):
        msg1=self.admin_id.get()
        msg2=self.email.get()
        msg3=self.mobile_num.get()
        msg4=self.password.get()

        val=self.check_data(name=msg1,password=msg2,mobilno=msg3,email=msg4)

        if val == 1:
            return True
            
        else:
            if val == 10:
                msg1=self.name.delete(0,END)
                self.get_data()
            # val=check_data(name=msg1,password=msg2,mobilno=msg3,email=msg4)


            elif val == 12:
                msg3=self.mobile_num.delete(0,END)
                self.get_data()
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

        self.admin_id=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.admin_id.grid(row=2,column=1,padx=5)

        #mobil_number
        Mobil_no=Label(Datafreame2,text="Mobil No:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=3,column=0,pady=15,sticky=W)

        self.mobile_num=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.mobile_num.grid(row=3,column=1,padx=5)

        #email
        emil=Label(Datafreame2,text="Email -Id:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=4,column=0,pady=15,sticky=W)

        self.email=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.email.grid(row=4,column=1,padx=5)

        #pass_word
        self.password=Label(Datafreame2,text="Password:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=5,column=0,pady=15,sticky=W)

        self.password=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
        self.password.grid(row=5,column=1,padx=5)
        
        Login_butt=Button(Datafreame2,text='Register',width=15,command=self.take_data)
        Login_butt.grid(row=7,column=1,pady=5)

        BACK=Button(Datafreame2,text='Login',width=15,command=self.Login_take_chek)
        BACK.grid(row=9,column=1,padx=5)

    def Register(self,root):
        Info = self.get_data(root)
        if Info == True: 
            self.add_admin()

    def Login(self,root):
        Datafreame2=Frame(root,background='#4caedb')
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

    def Login_take_chek(self):
        self.admin_id=self.admin_id.get()
        self.password=self.password.get()
        for item in self.result:
            if self.admin_id in item and self.password in item:
                print("sucefully login !")


            









