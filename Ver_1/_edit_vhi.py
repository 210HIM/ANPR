from tkinter import *                   #GUI python Lib
from tkinter import messagebox          #GUI python Lib
import mysql                            #Python LIb for Databace
import mysql.connector                  #Python Lib for Databace connection


class Edit_vhi:
    def _init_ (self):
        self.root = None
        self.result = None
        self.msg = ''
        
    def add_pass(self):
        try:
            file = open("Text/password.txt",'r')
            self.PWS = file.read()
            file.close()
        except:
            print("Password not get")


    def find_vhi(self):
        self.root = Tk()
        self.root.title("Edit vehicle information")
        self.root.wm_iconbitmap("Images/download.ico")
        self.root.geometry("400x200")
        self.Datafreame1=Frame(self.root,bd=5,padx=20,relief=RIDGE,bg="#19232d")
        self.Datafreame1.place(x=0,y=0,width=400,height=170)

        note = Label(self.Datafreame1, text = "Find Vhical ",font=("new time roman",10),relief=GROOVE,fg="black",bg="#87ceeb",width=15).place(x=100,y=10)

        vehicle_id = Label(self.Datafreame1, text="Vehicle Num :",font=("new time roman",10,"bold"),width=15)
        vehicle_id.place(x = 15 , y = 60)

        self.vehicle_id_entry =Entry (self.Datafreame1,font=("arial",10,"bold"), bg='#81c3e5',width=22,fg='black')
        self.vehicle_id_entry.place(x = 160, y = 60)

        submit_button = Button(self.Datafreame1,text="Search",fg="black",width=10, command=self.get_data)
        submit_button.place(x = 190 , y = 110)

        Datafreame2=Frame(self.root,bd=5,padx=20,bg='Black')
        Datafreame2.place(x=0,y=170,width=400,height=30)

        Exit=Button(Datafreame2,text='Back',command=self.Exit,bg='black',fg='white')
        Exit.place(x=335,y=0) 


    def Exit(self):
        self.root.destroy()


    def get_data(self):
        self.msg = str(self.vehicle_id_entry.get()).upper()
        conn=mysql.connector.connect(host="localhost",username="root",password=self.PWS,database="anpr_final_db")
        my_cursor=conn.cursor()
        sql =f"SELECT * FROM anpr_final_db.owner_data where Vehicle_number = '{self.msg}';"
        try:
            my_cursor.execute(sql)
            self.result = my_cursor.fetchall()
        except: 
            conn.close()
            messagebox.showwarning('Warning',"Server not responding 🚬🔌")

        if len(self.result) == 0:
            messagebox.showwarning('Warning',"Vehicle is not present 🚬")
            self.root.destroy()
            self.Edit_vhi_data()
        else:
            self.result = list(self.result[0])

        if self.msg in self.result:
            messagebox.showinfo('Information',"The data should be filled with great care as it will not be returned.")
            self.root.destroy()
            self.Edit_vhi_data()
        else:
            messagebox.showwarning('Warning',"Vehicle is not present 🚬")
            self.root.destroy()


    def Edit_vhi_data(self):
        self.root = Tk()
        self.root.title("Edit vehicle information")
        self.root.geometry("400x420")

        self.Datafreame1=Frame(self.root,bd=5,padx=20,relief=RIDGE,bg="#19232d")
        self.Datafreame1.place(x=0,y=0,width=400,height=390)

        note = Label(self.Datafreame1, text = "Edit Details ",font=("new time roman",10,"bold"),relief=GROOVE,fg="black",bg="#87ceeb",width=25)
        note.grid(row=0,column=0,columnspan=2)

        vehicle_id = Label(self.Datafreame1, text="Vehicle Num :",font=("new time roman",10,"bold"),width=15)
        vehicle_id.grid(row = 1, column = 0,padx = 8, pady = 15)
        
        vehicle_id_show = Label(self.Datafreame1, text=self.msg,font=("new time roman",10,"bold"),width=15)
        vehicle_id_show.grid(row = 1, column = 1,padx = 10, pady = 15)

        name = Label(self.Datafreame1, text="Owner name :",font=("new time roman",10,"bold"),width=15)
        name.grid(row = 2, column = 0,padx = 8, pady = 15)

        email_id = Label(self.Datafreame1, text="Email Id :",font=("new time roman",10,"bold"),width=15)
        email_id.grid(row = 3, column = 0,padx = 8, pady = 15)

        mobile_num = Label(self.Datafreame1, text="Mobile number :",font=("new time roman",10,"bold"),width=15)
        mobile_num.grid(row = 4, column = 0,padx = 8, pady = 15)
        
        address = Label(self.Datafreame1, text="Address :",font=("new time roman",10,"bold"),width=15)
        address.grid(row = 5, column = 0,padx =8, pady = 15)

        #entry....
        self.Name_entry=Entry(self.Datafreame1,font=("arial",10,"bold"), bg='#81c3e5',width=22,fg='black')
        self.Name_entry.grid(row=2,column=1,padx=5)
        self.Name_entry.insert(0,self.result[1])

        self.email_id_entry=Entry(self.Datafreame1,font=("arial",10,"bold"), bg='#81c3e5',width=22,fg='black')
        self.email_id_entry.grid(row=3,column=1,padx=5)
        self.email_id_entry.insert(0,self.result[2])

        self.mobile_num_entry=Entry(self.Datafreame1,font=("arial",10,"bold"), bg='#81c3e5',width=22,fg='black')
        self.mobile_num_entry.grid(row=4,column=1,padx=5)
        self.mobile_num_entry.insert(0,self.result[3])
        
        self.address_entry=Entry(self.Datafreame1,font=("arial",10,"bold"), bg='#81c3e5',width=22,fg='black')
        self.address_entry.grid(row=5,column=1,padx=5)
        self.address_entry.insert(0,self.result[4])

        self.submit_button = Button(self.Datafreame1,text="Update",fg="black",command=self.Ed_get_data)
        self.submit_button.grid(row=6,column=1,pady=10,sticky=W+E)
        
        Datafreame2=Frame(self.root,bd=5,padx=20,bg='Black')
        Datafreame2.place(x=0,y=390,width=400,height=30)

        Exit=Button(Datafreame2,text='Back',command=self.Exit,bg='black',fg='white')
        Exit.place(x=335,y=0)
    
    def Ed_get_data(self):
        name = self.Name_entry.get()
        mobile_num = self.mobile_num_entry.get()
        address = self.address_entry.get()
        email_id = self.email_id_entry.get()

        if name == '':
            name = self.result[1]

        if mobile_num == '':
            mobile_num = self.result[2]

        if address == '':
            address = self.result[4]

        if email_id == '':
            email_id = self.result[3]

        conn=mysql.connector.connect(host="localhost",username="root",password="rakesh",database="anpr_final_db")
        my_cursor=conn.cursor()

        q2 =""" UPDATE `anpr_final_db`.`owner_data` SET `owner_name` = %s, `mobile_num` = %s, `email_id` = %s, `address` = %s WHERE (`Vehicle_number` = %s);"""

        data = (name, mobile_num, email_id, address,self.msg)

        ans = messagebox.askquestion("Informetion","Do you want to update profile.")
        if ans == "yes":
            try:
                my_cursor.execute(q2,data)
                conn.commit()
                messagebox.showinfo('information',"Your profile has been updated.")
                self.root.destroy()
            except: 
                messagebox.showwarning('Warning',"Server not responding")
            finally:
                conn.close()
        else:
            self.root.destroy()


# obj = Edit_vhi()
# obj.find_vhi()
# mainloop()