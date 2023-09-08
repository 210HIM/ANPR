from tkinter import *
from Admin_info import *

class Main_windows:
    def __init__(self,admin_id):
        self.admin_id = admin_id
        self.root = Tk()
        self.root.title("Automatic License/Number Plate Recognition (ANPR)")
        #self.root.geometry("1540x800+0+0")
        width= self.root.winfo_screenwidth()
        height= self.root.winfo_screenheight()
        #setting tkinter window size
        self.root.geometry("%dx%d" % (width, height))
        #Title
        lalttitle=Label(self.root,bd=5,relief=RAISED,text="Automatic License/Number Plate Recognition (ANPR)",fg='black',bg='#f6f8fa',font=("times new roman",20,'bold'))
        lalttitle.place(x = 0, y = 0,width=1540)
        #Admin _ data
        self.obj = Admin(admin_id=self.admin_id)
        Admin_buttun = Button(self.root,text =self.admin_id,command=self.obj.Admin__data,font=("arial",13,"bold"))
        Admin_buttun.place(x = 0,y =50,width=70)


# obj = Main_windows("admin_1")
# mainloop()


