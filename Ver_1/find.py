from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql
import mysql.connector


class Find:
    def __init__(self):
        self.root = None
        self.result = None
        file = open("Text/password.txt", 'r')
        self.PWS = file.read()
        file.close()

    def add_pass(self):
        try:
            file = open("Text/password.txt", 'r')
            self.PWS = file.read()
            file.close()
        except:
            print("Password not get")



    def data(self):
        self.root = Tk()
        self.root.wm_iconbitmap("Images/download.ico")
        self.root.title("Vhical Entres")
        self.root.geometry("700x310")

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                             font=('Calibri', 11))  # Modify the font of the body
        self.style.configure("mystyle.Treeview.Heading",
                             font=('Calibri', 13, 'bold'))  # Modify the font of the headings
        self.style.layout("mystyle.Treeview",
                          [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.Datafreame1 = Frame(self.root, bg='#19232d', relief=RIDGE)
        self.Datafreame1.place(x=0, y=0, width=700, height=280)


        self.Datafreame3 = Frame(self.root, bd=2, bg='#19232d', relief=RIDGE)
        self.Datafreame3.place(x=0, y=280, width=700, height=30)

        exit = Button(self.Datafreame3, text='Back', command=self.Exit, bg='black', fg='white')
        exit.place(x=660, y=0)

        self.db_conect()

    def Exit(self):
        self.root.destroy()

    def db_conect(self):
        self.conn = mysql.connector.connect(username = 'root', host ='localhost', password = self.PWS,database = "anpr_final_db")
        self.my_curser = self.conn.cursor()
        sql = "select * from anpr_final_db.owner_data"
        self.my_curser.execute(sql)
        self.result = self.my_curser.fetchall()
        self.conn.close()
        self.new_table(self.result)

    def new_table(self, result):
        # Add a Treeview widget
        tree = ttk.Treeview(self.Datafreame1, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=13,
                            selectmode="extended", style="mystyle.Treeview")
        tree.column("# 1", width=10, anchor="nw")
        tree.heading("# 1", text="ID")

        tree.column("# 2", width=100, anchor="nw")
        tree.heading("# 2", text="Vehicle Number")

        tree.column("# 3", width=100, anchor="nw")
        tree.heading("# 3", text="Name")

        tree.column("# 4", width=100, anchor="nw")
        tree.heading("# 4", text="Mobile num")

        tree.column("# 5", width=140, anchor="nw")
        tree.heading("# 5", text="Email")

        tree.column("# 6", width=70, anchor="nw")
        tree.heading("# 6", text="Address")

        for ind, val in enumerate(result):

            if ind % 2 != 0:
                tree.insert('', 'end', text=val[0], values=(ind+1,val[0],val[1],val[2],val[3],val[4]),
                            tags=('even',))
            else:
                tree.insert('', 'end', text=val[0], values=(ind+1,val[0],val[1],val[2],val[3],val[4]),
                            tags=('odd',))

        tree.tag_configure('odd', background='#E8E8E8')
        tree.tag_configure('even', background='#a3a3a3')
        self.y_scollbar = ttk.Scrollbar(self.Datafreame1, orient="vertical", command=tree.yview)
        self.y_scollbar.place(x=670, y=0, height=270)
        tree['yscroll'] = self.y_scollbar.set
        tree.place(width=670, height=270)

    def get_type(self):
        masg = self.value_entry.get()
        print(masg)
# obj = Find()
# obj.data()
# mainloop()