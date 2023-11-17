from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql
import mysql.connector

class Find:
    def __init__ (self):
        self.root = None
        self.result = None
        file = open("Text/password.txt",'r')
        self.PWS = file.read()
        file.close()
        
    def add_pass(self):
        try:
            file = open("Text/password.txt",'r')
            self.PWS = file.read()
            file.close()
        except:
            print("Password not get")
        
    
    def find_vhi(self):
        self.root = Tk()
        self.root.wm_iconbitmap("Images/download.ico")
        self.root.title("Edit vehicle information")
        self.root.geometry("400x200")
        self.Datafreame1=Frame(self.root,bd=5,padx=20,relief=RIDGE,bg="#19232d")
        self.Datafreame1.place(x=0,y=0,width=400,height=170)

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        self.style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders


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


    def data(self):
        self.root = Tk()
        self.root.wm_iconbitmap("Images/download.ico")
        self.root.title("Vhical Entres")
        self.root.geometry("700x310")

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        self.style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        self.Datafreame1=Frame(self.root,padx=20,bg='#19232d',relief=RIDGE)
        self.Datafreame1.place(x = 0,y = 0,width= 700,height= 30)

        #--------------------
        self.type_of_sort = StringVar()
        comNameTable=ttk.Combobox(self.Datafreame1,textvariable=self.type_of_sort,font=("arial",10,"bold"),width=15)

        comNameTable["values"]=("Date","Time","Alphabet",)
        comNameTable.current(0)
        comNameTable.place(x = 0 ,y = 0)

        Admin_buttun = Button(self.Datafreame1,text ='Sort',font=("arial",8,"bold"),fg="#e0e1e3",bg="#4169e1",width=10)
        Admin_buttun.place(x = 150,y = 0 )
        #-----

        self.Datafreame2=Frame(self.root,bd=5,bg='#19232d',relief=RIDGE)
        self.Datafreame2.place(x = 0,y = 30,width= 700,height= 250)

        self.value_entry = Entry(self.root, font=("arial", 10, "bold"))
        self.value_entry.place(x=100, y=0)

        Admin_buttun = Button(self.Datafreame2, text='Please Delete me🙏👎🙏', command=self.get_type,
                              font=("arial", 8, "bold"),
                              fg="#e0e1e3", bg="#4169e1")
        Admin_buttun.place(x=340, y=0)

        self.Datafreame3=Frame(self.root,bd=2,bg='#19232d',relief=RIDGE)
        self.Datafreame3.place(x = 0,y = 280,width= 700,height= 30)

        exit=Button(self.Datafreame3,text='Back',command=self.Exit,bg='black',fg='white')
        exit.place(x=660,y=0)

        self.new_table(self.result)

    def db_conect(self):
        self.conn = mysql.connector.connect(username = 'root', host ='localhost', password = self.PWS,database = "anpr_final_db")
        self.my_curser = self.conn.cursor()
        sql = "select * from anpr_final_db.owner_data"
        self.my_curser.execute(sql)
        self.result = self.my_curser.fetchall()
        self.conn.close()
        self.new_table(self.result)

    def new_table(self,result):
        # Add a Treeview widget
        tree = ttk.Treeview(self.Datafreame2, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=10,selectmode = "extended" ,style="mystyle.Treeview")
        tree.column("# 1",width=10,anchor="nw")
        tree.heading("# 1", text="ID")

        tree.column("# 2",width=100, anchor="nw")
        tree.heading("# 2", text="Vehicle Number")

        tree.column("# 3",width=100, anchor="nw")
        tree.heading("# 3", text="Entry Date")

        tree.column("# 4",width=100, anchor="nw")
        tree.heading("# 4", text="Entry Time")

        tree.column("# 5",width=100, anchor="nw")
        tree.heading("# 5", text="Exit Date")

        tree.column("# 6",width=100, anchor="nw")
        tree.heading("# 6", text="Exit Time")

        for ind,val in enumerate(result):

            data_1 = val[2]
            # date_1, time_1 = data_1.split(' ')
            # time_1 = time_1[:8]

            date_1 = data_1.strftime("%d-%b-%Y")
            time_1 = data_1.strftime("%H:%M:%S")

            data_2 = val[3]
            # date_2, time_2 = data_2.split(' ')
            # time_2 = time_2[:8]

            date_2 = data_2.strftime("%d-%b-%Y")
            time_2 = data_2.strftime("%H:%M:%S")
            
            if ind % 2 != 0:
                tree.insert('', 'end', text=val[0], values=(ind+1,val[1],date_1,time_1,date_2,time_2),tags=('even',))
            else:
                tree.insert('', 'end', text=val[0], values=(ind+1,val[1],date_1,time_1,date_2,time_2),tags=('odd',))

        tree.tag_configure('odd', background='#E8E8E8')
        tree.tag_configure('even', background='#a3a3a3')
        self.y_scollbar = ttk.Scrollbar(self.Datafreame2,orient ="vertical",command = tree.yview)
        self.y_scollbar.place(x=670, y=0,height=240)
        tree['yscroll'] = self.y_scollbar.set
        tree.place(width=670,height=240)
            

obj = Find()
obj.find_vhi()
mainloop()