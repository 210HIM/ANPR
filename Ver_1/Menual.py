from tkinter import *
from tkinter import ttk
import cv2 as cv                        #python lib for open image and video play
from PIL import ImageTk,Image           #Python lib for open image
from PIL import *      
from tkinter import filedialog


class Menual:
    def __init__(self):
        self.root = None
        file = open("Text/Menuall.txt",'r')
        self.mesg =file.read()
        self.path = None
                 
    def informetion(self):
        self.root = Tk()
        self.root.title("APMS/Menuale")
        self.root.wm_iconbitmap("Images/download.ico")
        self.root.geometry("800x700")
        
        Datafream1=Frame(self.root,bg="#3da8d8")
        Datafream1.place(x = 0 ,y = 0,width = 650 ,height = 670)
        
        text = Text(Datafream1,width=69,height=39,font=("Courier New",11))
        text.place(x = 0, y = 0)
        text.insert(END,self.mesg)

        self.y_scollbar = ttk.Scrollbar(Datafream1,orient ="vertical",command = text.yview)
        self.y_scollbar.place(x=625, y=0,height=670)
        text['yscroll'] = self.y_scollbar.set
        text.config(state= DISABLED,xscrollcommand = self.y_scollbar.set)
    
        Datafream2=Frame(self.root,bd=5,bg="#3da8d8")
        Datafream2.place(x = 650 ,y = 0,width = 150,height = 670)

        values = ("Block Daigram", "Flow chart", "Process chart")
        self.path = StringVar()
        self.path.set("Block Daigram")
        Table_s = OptionMenu(Datafream2, self.path, *values)
        Table_s.place(x = 0, y = 0, width=10)

        status_buttun = Button(Datafream2,text ='Select',font=("arial",8,"bold"),fg="#e0e1e3",bg="#003153",width=10,
                              command=self.select_img)
        status_buttun.place(x=30, y=0)

        Datafream3 =Frame(self.root,bd=5,bg="black")
        Datafream3.place(x=0, y=670, width=800, height=30)

        back_butt = Button(Datafream3,text="back",font=("arial",10,"bold"),command=self.Exit)
        back_butt.place(x=750,y=0)
    
    def Exit(self):
        self.root.destroy()

    def select_img(self):
        file_name = self.path.get()
        # print(file_name)
        value = ["Block Daigram","Flow chart","Process chart"]
        Path_offile = ["Images/Block Diagram.jpg","Images/Flowchart.jpg","Images/Process chart.jpg"]
        ind = value.index(file_name)
        img=cv.imread(Path_offile[ind])
        cv.imshow("img",img)
        
