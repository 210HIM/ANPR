from tkinter import * 
from tkinter import messagebox
import mysql
import mysql.connector


class new_memb:
    def _init_ (self):
        self.root = None
    

    def add_pass(self):
        try:
            file = open("Text/password.txt",'r')
            self.PWS = file.read()
            file.close()
        except:
            print("Password not get")


    def add_new_vhi(self):
        self.root = Tk()
        self.root.title("Registration of new vehicle")
        self.root.geometry("400x400")

        Datafreame1=Frame(self.root,bd=5,padx=20,relief=RIDGE,bg="#19232d")
        Datafreame1.place(x=0,y=0,width=400,height=370)

        note = Label(Datafreame1, text = "New vehicle registration ",font=("Young Serif",13,"bold"),relief=GROOVE,fg="black",bg="#00FFFF")
        note.grid(row=0,column=0,columnspan=2 ,pady = 15)

        name = Label(Datafreame1, text="Owner name :",font=("new time roman",10,"bold"),width=15)
        name.grid(row = 2, column = 0,padx = 10, pady = 15)

        vhi_num = Label(Datafreame1, text="Vehicle Number :",font=("new time roman",10,"bold"),width=15)
        vhi_num.grid(row = 3, column = 0,padx = 10, pady = 15)

        email_id = Label(Datafreame1, text="Email Id :",font=("new time roman",10,"bold"),width=15)
        email_id.grid(row = 4, column = 0,padx = 10, pady = 15)

        mobile_num = Label(Datafreame1, text="Mobile number :",font=("new time roman",10,"bold"),width=15)
        mobile_num.grid(row = 5, column = 0,padx = 10, pady = 15)
        
        address = Label(Datafreame1, text="Address :",font=("new time roman",10,"bold"),width=15)
        address.grid(row = 6, column = 0,padx = 10, pady = 15)

        #entry....
        self.Name_entry=Entry(Datafreame1,font=("arial",10,"bold"), bg='#81c3e5',width=22,fg='black')
        self.Name_entry.grid(row=2,column=1,padx=5)

        self.vhi_num_entry=Entry(Datafreame1,font=("arial",10,"bold"), bg='#81c3e5',width=22,fg='black')
        self.vhi_num_entry.grid(row=3,column=1,padx=5)

        self.email_id_entry=Entry(Datafreame1,font=("arial",10,"bold"), bg='#81c3e5',width=22,fg='black')
        self.email_id_entry.grid(row=4,column=1,padx=5)

        self.mobile_num_entry=Entry(Datafreame1,font=("arial",10,"bold"), bg='#81c3e5',width=22,fg='black')
        self.mobile_num_entry.grid(row=5,column=1,padx=5)
        
        self.address_entry=Entry(Datafreame1,font=("arial",10,"bold"), bg='#81c3e5',width=22,fg='black')
        self.address_entry.grid(row=6,column=1,padx=5)

        self.submit_button = Button(Datafreame1,text="Add Vehicle",fg="black",command=self.get_data,font=("Pixelify Sans",10,"bold"))
        self.submit_button.grid(row=7,column=1,pady=10,sticky=W+E)

        Datafreame2=Frame(self.root,bd=5,padx=20,bg='Black')
        Datafreame2.place(x=0,y=370,width=400,height=30)

        Exit=Button(Datafreame2,bd=3,text='Back',command=self.Exit,bg='black',fg='white')
        Exit.place(x=340,y=0)


    def Exit(self):
        self.root.destroy()


    def get_data(self):
        name = self.Name_entry.get()
        vhi_num = self.vhi_num_entry.get()
        vhi_num  = vhi_num.upper()
        email_id = self.email_id_entry.get()
        mobile_num = self.mobile_num_entry.get()
        addres = self.address_entry.get()

        ans = self.check_data(name, vhi_num, email_id, mobile_num, addres)

        if ans == 1:
            self.mobile_num_entry.delete(0,END)

        elif ans != 0:
            self.save_data([name, vhi_num, email_id, mobile_num, addres])

    def check_data(self,name, vhi_num, email_id, mobile_num, addres):
        if name == '' or vhi_num == '' or email_id == '' or mobile_num == '' or addres == '':
            messagebox.showwarning('Warning',"All informetion is necessary.")
            return 0
        elif len(mobile_num) != 10:
            messagebox.showwarning('Warning',"The mobile number provided is incorrect.")
            return 1

    def save_data(self,data):
        conn=mysql.connector.connect(host="localhost",username="root",password=self.PWS,database="anpr_final_db")
        my_cursor=conn.cursor()

        q2 = """INSERT INTO anpr_final_db.owner_data (Vehicle_number,owner_name,mobile_num,email_id,address) VALUES (%s, %s, %s, %s, %s);"""
        data = (str(data[1]),str(data[0]),str(data[3]),str(data[2]),str(data[4]))
        try:
            my_cursor.execute(q2,data)
            conn.commit()
            messagebox.showinfo('Information',"Rregistration process was successfully completed.")
            self.Exit()
        except:
            messagebox.showerror('Error',"Registration process has been halted.\nServer not responding")
        finally:
            conn.close()

        
# obj = new_memb()
# obj.add_new_vhi()
# mainloop()