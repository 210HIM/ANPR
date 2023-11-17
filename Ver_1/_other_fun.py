from tkinter import * 

class Other:
    def __init__ (self):
        self.root = None

    def Other_data(self):
        self.root = Tk()
        self.root.wm_iconbitmap("Images/download.ico")
        self.root.title("Functions")
        self.root.geometry("600x500")

        self.Datafreame1=Frame(self.root,bd=5,padx=20,bg='#a7d5ef')
        self.Datafreame1.place(x=0,y=0,width=450,height=470)

        Add_label = Label (self.Datafreame1, text = "Setting",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="black",bg="#8db6ff" ).grid(row = 0, column = 0, pady=10,sticky = W)

        Add_label = Label (self.Datafreame1, text = "Add New Vehicle :",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="black",bg="#6d99c5" ).grid(row = 1, column = 0)
        Add_butt = Button(self.Datafreame1,text = "ADD",font=("arial",8,"bold"),bg="#007acc",fg="#19232d",width=10)
        Add_butt.grid(row = 1, column = 2,padx=45,pady=15)

        Add_label = Label (self.Datafreame1, text = "Edit Veh_info :",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="black",bg="#6d99c5" ).grid(row = 2, column = 0)
        Add_butt = Button(self.Datafreame1,text = "Check",font=("arial",8,"bold"),bg="#007acc",fg="#19232d",width=10)
        Add_butt.grid(row = 2, column = 2,padx=45,pady=15)

        Add_label = Label (self.Datafreame1, text = "Find Veh_Detels :",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="black",bg="#6d99c5" ).grid(row = 3, column = 0)
        Add_butt = Button(self.Datafreame1,text ="Find",font=("arial",8,"bold"),bg="#007acc",fg="#19232d",width=10)#change after implimention
        Add_butt.grid(row = 3, column = 2,padx=45,pady=15)

        Add_label = Label (self.Datafreame1, text = "Vehicle Records :",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="black",bg="#6d99c5" ).grid(row = 4, column = 0)
        Add_butt = Button(self.Datafreame1,text = "Edit",font=("arial",8,"bold"),bg="#007acc",fg="#19232d",width=10)
        Add_butt.grid(row = 4, column = 2,padx=45,pady=15)

        Add_label = Label (self.Datafreame1, text = "Delete Vehical :",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="black",bg="#6d99c5" ).grid(row = 5, column = 0)
        Add_butt = Button(self.Datafreame1,text = "Edit",font=("arial",8,"bold"),bg="#007acc",fg="#19232d",width=10)
        Add_butt.grid(row = 5, column = 2,padx=45,pady=15)
        
        Add_label = Label (self.Datafreame1, text = "Other Functions :",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="black",bg="#6d99c5").grid(row = 6, column = 0,sticky=W)
        Add_butt = Button(self.Datafreame1,text = "Go",font=("arial",8,"bold"),bg="#007acc",fg="#19232d",width=10)
        Add_butt.grid(row = 6, column = 2,padx=45,pady=15)

        Datafreame2=Frame(self.root,bd=5,padx=20,bg='#f9dd4b')
        Datafreame2.place(x=450,y=0,width=150,height=470)

        Datafreame3=Frame(self.root,bd=5,padx=20,bg='black')
        Datafreame3.place(x=0,y=470,width=600,height=30)

        Exit=Button(Datafreame3,text='Back',command=self.Exit,bg='black',fg='white')
        Exit.place(x=535,y=0) 

    def Exit(self):
        self.root.destroy()

# obj = Other()
# obj.Other_data()
# mainloop()

        