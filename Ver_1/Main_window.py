from tkinter import *                   #Python LIB GUI
from tkinter import ttk                 #Python LIB GUI
from tkinter import filedialog          #Python LIB for access file menager
from Admin_info import *                #LIB get user informetion 
from Menual import *                    #for project working process
from _new_vhi import *                  #LIB ADD New vhi in db
import datetime as dt                   #Python LIB DATE_TIME
from find import *                     #Python
from _edit_vhi import *                 #Python
from _vhi_record import *               #Python
from _other_fun import *                #Python
from PIL import Image,ImageTk           #Python
from drop import *
import cv2 as cv
from Entery_Exit import *               #Python
from Program import *
import re


class Main_windows:
    def __init__(self,admin_id):
        self.admin_id = admin_id
        self.root = Tk()
        self.root.winfo_toplevel()
        self.root.state('zoomed')
        self.root.wm_iconbitmap("Images/download.ico")
        self.camera_num = None
        self.temp = 0

        self.root.bind('<space>', lambda e: self.root.quit())

        #vareables
        self.Name_camera = None
        self.root.title("AMPS/Home")
        width= self.root.winfo_screenwidth()
        height= self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (width, height))
        #Title
        lalttitle=Label(self.root,bd=5,relief=RAISED,text="Automated Parking Management System",fg='#e0e1e3',bg='#455364',font=("times new roman",15,'bold'))
        lalttitle.place(x = 0, y = 0,width=1540)

        self.Datafreame_1=Frame(self.root,bd=5,padx=20,bg='#19232d',relief=RIDGE)
        self.Datafreame_1.place(x = 0,y = 40,width= 600,height= 500)

        title_entry = Label (self.Datafreame_1, text = "Entry Get",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="black",bg="#87ceeb" ).pack()
        
        self.vid_widget1 =Label(self.Datafreame_1,bg='#19232d')
        self.vid_widget1.pack()

        self.Datafreame_2=Frame(self.root,bd=5,padx=20,bg='#19232d',relief=RIDGE)
        self.Datafreame_2.place(x = 600,y = 40,width= 600,height= 500)

        title_exit =Label (self.Datafreame_2, text = "Exit Get",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="black",bg="#87ceeb" ).pack()

        self.vid_widget2 =Label(self.Datafreame_2,bg='#19232d')
        self.vid_widget2.pack()

        #Datafream2 is defaind userinfo
        self.Datafreame2 = Frame(self.root,bd=5,padx=20,bg='#19232d',relief=GROOVE)
        self.Datafreame2.place(x = 1205, y = 40, width= 330, height= 400)

        #Datafream3 is defaind lower fream
        self.Datafreame3 = Frame(self.root,bd=5,padx=20,bg='#19232d',relief=GROOVE)
        self.Datafreame3.place(x = 1205, y = 445, width= 330, height= 350)

        #Datafream4 is defaindd lower left fream 
        self.Datafreame4 = Frame(self.root,bd=5,bg='white',relief=GROOVE)
        self.Datafreame4.place(x = 0, y = 545, width= 1200, height= 250)

        #Admin _ data
        self.obj = Admin(self.admin_id)
        Admin_buttun = Button(self.Datafreame2,text ='Your Profile',command=self.obj.Admin__data,font=("arial",10,"bold"),relief=GROOVE,fg="black",bg="#87ceeb",width=15)
        Admin_buttun.place(x = 10,y = 10)
        self.changeOnHover(Admin_buttun,'#003153','#87ceeb')
  
        #Entry and Exit
        self.status = StringVar()
        comNameTable_s=ttk.Combobox(self.Datafreame2,textvariable=self.status,font=("arial",10,"bold"),width=15)

        comNameTable_s["values"]=("Select form system","En_Cemera_1","En_Cemera_2","En_Cemera_3") 
        comNameTable_s.current(0)
        comNameTable_s.place(x = 5 ,y = 55)

        status_buttun =Button (self.Datafreame2,text ='Select',command=self.Entry_get_cam_sel,font=("arial",8,"bold"),fg="#e0e1e3",bg="#003153",width=10)
        status_buttun.place(x = 180,y = 55 )
        self.changeOnHover(status_buttun,'#87ceeb','#003153')

        # done list
        self.Name_camera = StringVar()
        comNameTable=ttk.Combobox(self.Datafreame2,textvariable=self.Name_camera,font=("arial",10,"bold"),width=15)

        comNameTable["values"]=("Select form system","Ex_Cemera_1","Ex_Cemera_2","Ex_Cemera_3")
        comNameTable.current(0)
        comNameTable.place(x = 5 ,y = 100)

        Admin_buttun = Button(self.Datafreame2,text ='Select',command=self.print_data,font=("arial",8,"bold"),fg="#e0e1e3",bg="#003153",width=10)
        Admin_buttun.place(x = 180,y = 100 )
        self.changeOnHover(Admin_buttun,'#87ceeb','#003153')

        vhi_count = Label (self.Datafreame2, text = "Number of Cars :",font=("arial",10,"bold"),relief=RIDGE,width=15,fg="#e0e1e3",bg="#19232d")
        vhi_count.place(x = 5 , y = 150)

        vhi_count_data = Label (self.Datafreame2, text = "0",font=("arial",10,"bold"),relief=GROOVE,width=15,fg="#e0e1e3",bg="#19232d")
        vhi_count_data.place(x = 150 , y = 150)

        temp=dt.datetime.now()
        date,time=list(str(temp).split())

        Date_label = Label (self.Datafreame2, text = "Data :",font=("arial",10,"bold"),  relief=GROOVE,width=15,fg="#e0e1e3",bg="#19232d" ).place(x = 5, y = 200)
        print_Date_label = Label (self.Datafreame2, text = temp.strftime("%d-%b-%Y"),font=("arial",10,"bold"),relief=GROOVE,width=15,fg="#e0e1e3",bg="#19232d" ).place(x = 150, y = 200)

        cap_label = Label (self.Datafreame2, text = "Capiciti :",font=("arial",10,"bold"),relief=GROOVE ,width=15,fg="#e0e1e3",bg="#19232d").place(x = 5, y = 250)
        self.print_cap_label = Label (self.Datafreame2, text = 0,font=("arial",10,"bold"),width=15,fg="#e0e1e3",bg="#19232d",relief=GROOVE )
        self.print_cap_label.place(x = 150, y = 250)
        
        Av_Cap_label = Label (self.Datafreame2, text = "Avilable Cap :",font=("arial",10,"bold"),  relief=GROOVE ,width=15,fg="#e0e1e3",bg="#19232d").place(x = 5, y = 300)
        print_Av_cap_label = Label (self.Datafreame2, text =10, font=("arial",10,"bold"),width=15,relief=GROOVE,fg="#e0e1e3",bg="#19232d" ).place(x = 150, y = 300)

        Quit_but = Button(self.Datafreame2, text="EXIT", command=self.root.quit, font=("arial", 8, "bold"),
                          fg="#e0e1e3", bg="#003153", width=10)
        Quit_but.place(x=5, y=350)
        self.changeOnHover(Quit_but, 'RED', '#003153')

        Edit_but = Button(self.Datafreame2, text="Edit", command=self.Edit_cpicity, font=("arial", 8, "bold"),
                          fg="#e0e1e3", bg="#003153", width=10)
        Edit_but.place(x=180, y=350)
        self.changeOnHover(Edit_but, '#87ceeb', '#003153')


        #data_fream 3 add new vhicL GUI
        self.add_vhic = new_memb()
        self.add_vhic.add_pass()

        self.Records = Detels()
        self.Records.add_pass()

        self.edit_info= Edit_vhi()
        self.edit_info.add_pass()

        self.find_info = Find()
        self.find_info.add_pass()

        self.other= Other()
        self.dop = drop_file()

        Menu = Menual()

        Add_label = Label (self.Datafreame3, text = "Setting",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="black",bg="#87ceeb" ).grid(row = 0, column = 0, pady=10,sticky = W)

        Add_label = Label (self.Datafreame3, text = "Add New Vehicle :",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="#e0e1e3",bg="#19232d" ).grid(row = 1, column = 0)
        Add_butt = Button(self.Datafreame3,text = "ADD",font=("arial",8,"bold"),fg="#e0e1e3",bg="#003153",command=self.add_vhic.add_new_vhi,width=10)
        Add_butt.grid(row = 1, column = 2,padx=35,pady=10)
        self.changeOnHover(Add_butt,'#87ceeb','#003153')

        Add_label = Label (self.Datafreame3, text = "Edit Veh_info :",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="#e0e1e3",bg="#19232d" ).grid(row = 2, column = 0)
        Add_butt = Button(self.Datafreame3,text = "Edit",font=("arial",8,"bold"),fg="#e0e1e3",bg="#003153",command=self.edit_info.find_vhi,width=10)
        Add_butt.grid(row = 2, column = 2,padx=35,pady=10)
        self.changeOnHover(Add_butt,'#87ceeb','#003153')

        Add_label = Label (self.Datafreame3, text = "Find Veh_Detels :",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="#e0e1e3",bg="#19232d" ).grid(row = 3, column = 0)
        Add_butt = Button(self.Datafreame3,text ="Find",font=("arial",8,"bold"),fg="#e0e1e3",bg="#003153",width=10,command=self.find_info.data)#change after implimention
        Add_butt.grid(row = 3, column = 2,padx=35,pady=10)
        self.changeOnHover(Add_butt,'#87ceeb','#003153')

        Add_label = Label (self.Datafreame3, text = "Vehicle Records :",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="#e0e1e3",bg="#19232d" ).grid(row = 4, column = 0)
        Add_butt = Button(self.Datafreame3,text = "Find",font=("arial",8,"bold"),fg="#e0e1e3",bg="#003153",command=self.Records.data,width=10)
        Add_butt.grid(row = 4, column = 2,padx=35,pady=10)
        self.changeOnHover(Add_butt,'#87ceeb','#003153')

        Add_label = Label (self.Datafreame3, text = "Delete Vehical :",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="#e0e1e3",bg="#19232d" ).grid(row = 5, column = 0)
        Add_butt = Button(self.Datafreame3,text = "Delete",font=("arial",8,"bold"),fg="#e0e1e3",bg="#003153",width=10,command=self.dop.data)
        Add_butt.grid(row = 5, column = 2,padx=35,pady=10)
        self.changeOnHover(Add_butt,'#87ceeb','#003153')

        Add_label = Label (self.Datafreame3, text = "Other Functions :",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="#e0e1e3",bg="#19232d").grid(row = 6, column = 0,sticky=W)
        Add_butt = Button(self.Datafreame3,text = "Go",font=("arial",8,"bold"),fg="#e0e1e3",bg="#003153",width=10,command=self.other.Other_data)
        Add_butt.grid(row = 6, column = 2,padx=35,pady=10)
        self.changeOnHover(Add_butt,'#87ceeb','#003153')

        Info = Button(self.Datafreame3,text = "Manual",font=("arial",10,"italic"),fg="black",bg="#87ceeb",command=Menu.informetion)
        Info.grid(row = 7, column = 2,padx=35)
        #self.changeOnHover(Add_butt,'#87ceeb','#003153')


        #Datafream_4
        #In Dataframe4 divedetion of block
        #fream1,2 is belong Entry_get
        self.fream_1 = Frame(self.Datafreame4,bd=4,bg='#19232d',relief=GROOVE)
        self.fream_1.place(x = 0, y = 0, width= 250, height= 240)
        title_entry = Label (self.fream_1, text = "Entry Get",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="black",bg="#87ceeb" ).pack()
        self.Img = Label(self.fream_1,bg="#19232d",relief=GROOVE,fg="black" ,font=("arial",15,"bold"))
        self.Img.pack()
        img_butt = Button(self.fream_1,text="Take img",font=("arial",8,"bold"),fg="#e0e1e3",bg="#19232d",width=10,command=self.select_img)
        img_butt.pack()



        self.fream_2 = Frame(self.Datafreame4,bd=4,bg='#19232d',relief=GROOVE)
        self.fream_2.place(x = 250, y = 0, width= 250, height= 240)
        title_entry = Label (self.fream_2, text = "Entry Get",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="black",bg="#87ceeb" ).pack()
        self.lb_num_p = Label(self.fream_2,bg="#19232d",font=("arial",10,"bold"),width=20)
        self.lb_num_p.pack()
        cunvert_butt = Button(self.fream_2,text="filter",font=("arial",8,"bold"),fg="#e0e1e3",bg="#19232d",width=10,command=self.filter_img)
        cunvert_butt.pack()
        self.lb_num_p_1 = Label(self.fream_2, bg="#19232d", font=("arial", 10, "bold"), width = 20)
        self.lb_num_p_1.pack()



        #fream3,4 is belong Exit_get
        self.fream_3 = Frame(self.Datafreame4,bd=4,bg='#19232d',relief=GROOVE)
        self.fream_3.place(x = 505, y = 0, width= 250, height= 240)
        title_entry = Label (self.fream_3, text = "Exit Get",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="black",bg="#87ceeb" ).pack()
        self.Img_1 = Label(self.fream_3, bg="#19232d", relief=GROOVE, fg="black", font=("arial", 15, "bold"))
        self.Img_1.pack()
        img_butt = Button(self.fream_3, text="Take img", font=("arial", 8, "bold"), fg="#e0e1e3", bg="#19232d",
                          width=10, command=self.select_img_1)
        img_butt.pack()


        self.fream_4 = Frame(self.Datafreame4,bd=4,bg='#19232d',relief=GROOVE)
        self.fream_4.place(x = 755, y = 0, width= 245, height= 240)
        title_entry = Label (self.fream_4, text = "Exit Get",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="black",bg="#87ceeb" ).pack()

        self.lb_num_Exit = Label(self.fream_4, bg="#19232d", font=("arial", 10, "bold"), width=20)
        self.lb_num_Exit.pack()
        cunvert_butt = Button(self.fream_4, text="filter", font=("arial", 8, "bold"), fg="#e0e1e3", bg="#19232d",
                              width=10, command=self.filter_img_1)
        cunvert_butt.pack()
        self.lb_num_p_Exit = Label(self.fream_4, bg="#19232d", font=("arial", 10, "bold"), width=20)
        self.lb_num_p_Exit.pack()


        #Daatafream5 access for vhical
        self.fream_5 = Frame(self.Datafreame4,bd=4,bg='#19232d',relief=GROOVE)
        self.fream_5.place(x = 1005, y = 0, width= 195, height= 240)

        Acc_label_butt = Label(self.fream_5,text="Aoutometic Access",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="black",bg="#87ceeb" )
        Acc_label_butt.place(x=5,y=5)
        
        Access_button = Button(self.fream_5,text="Denay",bg="Red",width=10,fg="white",font=("arial",10,"bold"))
        Access_button.place(x=37,y=35)
        self.changeOnHover(Access_button,'green','red')

        Acc_label_b = Label(self.fream_5,text="Manually Access",font=("arial",10,"bold"), relief=GROOVE,width=20,fg="black",bg="#87ceeb" )
        Acc_label_b.place(x=5,y=75)

        Access_button_men = Button(self.fream_5,text="Access",width=10,fg="black",bg='#acacac',font=("arial",10,"bold"))
        Access_button_men.place(x=35,y=105)
        self.changeOnHover(Access_button_men,'green','#acacac')

        self.T = Text(self.fream_5, height = 3,relief=GROOVE,width=17,fg="#e0e1e3",bg="#19232d",font=("arial",12,"bold"))
        self.T.place(x=10,y=150)

        self.T.insert(END,"Access Granted")

    def select_img_1(self):
        name_img = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Image files", "*.jpeg*"), ("all files","*.*")))
        if len(name_img) == 0:
            return
        self.img=cv.imread(name_img)
        photo = cv.resize(self.img, (200,180))
        new_img=photo            
        opencv_image = cv.cvtColor(new_img, cv.COLOR_BGR2RGBA)
        captured_image = Image.fromarray(opencv_image)
        photo_image = ImageTk.PhotoImage(image=captured_image)
        self.Img_1.photo_image = photo_image
        self.Img_1.configure(image=photo_image)

    def select_img(self):
        name_img = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Image files", "*.jpeg*"), ("all files","*.*")))
        if len(name_img) == 0:
            print("return")
            return
        self.img=cv.imread(name_img)
        photo = cv.resize(self.img, (200,180))
        new_img=photo
        opencv_image = cv.cvtColor(new_img, cv.COLOR_BGR2RGBA)
        captured_image = Image.fromarray(opencv_image)
        photo_image = ImageTk.PhotoImage(image=captured_image)
        self.Img.photo_image = photo_image
        self.Img.configure(image=photo_image)


    def filter_img(self):
        number_plate = number_plate_detection(self.img)
        if number_plate != None:
            res2 = str("".join(re.split("[^a-zA-Z0-9]*", number_plate)))
            res2=res2.upper()
            self.Num_PL = res2
            self.lb_num_p_1.config(text=self.Num_PL,fg="red",font=('arial',15,'bold'))
            update_entry_get(self.Num_PL)
        else:
            self.Num_PL = None
            self.lb_num_p_1.config(text="NONE",fg="red",font=('arial',15,'bold'))

    def filter_img_1(self):
        number_plate = number_plate_detection(self.img)
        if number_plate != None:
            res2 = str("".join(re.split("[^a-zA-Z0-9]*", number_plate)))
            res2=res2.upper()
            self.Num_PL = res2
            self.lb_num_p_Exit.config(text=self.Num_PL,fg="red",font=('arial',15,'bold'))
            update_Exit_get(self.Num_PL)
        else:
            self.Num_PL = None
            self.lb_num_p_Exit.config(text="NONE",fg="red",font=('arial',15,'bold'))


    def Edit_cpicity(self):
        temp_root = Tk()
        temp_root.geometry('300x200')
        temp_root.title("APMS/Edit cepicity")
        temp_root.wm_iconbitmap("Images/download.ico")
        title = Label(temp_root,text="You can Edit Cepicity",font=("arial",10),relief=GROOVE,width=20,fg="black",bg="#87ceeb" )
        title.place(x=20,y=15)

        cep = Label(temp_root,text="Cepicity :",font=("arial",10,"bold"), relief=GROOVE,fg="black",bg="#87ceeb")
        cep.place(x=15,y=50)

        self.cep_Entry = Entry(temp_root,font=("arial",10,"bold"))
        self.cep_Entry.place(x=100,y=50)

        update_butt = Button(temp_root,font=("arial",10,"bold"),text="update",command =self.change_data,relief=GROOVE,fg="black",bg="#87ceeb" )
        update_butt.place(x=120,y=100)

    def change_data(self):
        val = self.cep_Entry.get()
        self.print_cap_label.config(text=val)

    def changeOnHover(self,button, colorOnHover, colorOnLeave):
            button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover,fg="black"))
            button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave,fg="black"))


    #Play video on mainscrren 
    def open_video_Entry(self):
        try:
            isTrue , frame =self.vid.read()
        except:
            messagebox.showwarning("warning","The video is currently unavailable and will be available again in a few time.")
            return
        #date and time
        temp=dt.datetime.now()
        date_time=list(str(temp).split())
        cv.putText(frame,str(temp),(50,350),cv.FONT_HERSHEY_TRIPLEX,0.50,(0,255,0),1)
        cv.rectangle(frame,(730,420),(2,180),(0,255,0),thickness=2)
        try:
            opencv_image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
        except:
            return
        captured_image = Image.fromarray(opencv_image)
        photo_image = ImageTk.PhotoImage(image=captured_image)
        self.vid_widget2.photo_image = photo_image
        self.vid_widget2.configure(image=photo_image)
        self.vid_widget2.after(25, self.open_video_Entry)


    def open_video_Exit(self):
        try:
            isTrue , frame =self.vid_EX.read()
        except:
            messagebox.showwarning("warning","The video is currently unavailable and will be available again in a few time.")
            return
        #date and time
        temp=dt.datetime.now()
        date_time=list(str(temp).split())
        cv.putText(frame,str(temp),(50,350),cv.FONT_HERSHEY_TRIPLEX,0.50,(0,255,0),1)
        cv.rectangle(frame,(730,420),(2,180),(0,255,0),thickness=2)
        try:
            opencv_image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
        except:
            return
        captured_image = Image.fromarray(opencv_image)
        photo_image = ImageTk.PhotoImage(image=captured_image)
        self.vid_widget1.photo_image = photo_image
        self.vid_widget1.configure(image=photo_image)
        self.vid_widget1.after(25, self.open_video_Exit)


    def print_data(self):
        self.camera_num = self.Name_camera.get()
        cam_list = ["Select form system","Videos/car.mp4","Videos/DON.mp4","Videos/girl.mp4"]
        if cam_list[0] == self.camera_num:
            self.filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Image files", "*.mp4*"), ("all files","*.*")))
            print(self.filename)
            if len(self.filename) != 0:
                self.vid=cv.VideoCapture(self.filename)
                self.open_video_Entry()
        else:
            n = int(self.camera_num[-1])
            self.vid=cv.VideoCapture(cam_list[n])
            self.open_video_Entry()


    def Entry_get_cam_sel(self):
        self.camera_num_1 = self.status.get()
        cam_list = ["Select form system","Videos/car.mp4","Videos/DON.mp4","Videos/girl.mp4"]
        if cam_list[0] == self.camera_num_1:
            self.filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Image files", "*.mp4*"), ("all files","*.*")))
            print(self.filename)
            if len(self.filename) != 0:
                self.vid_EX=cv.VideoCapture(self.filename)
                self.open_video_Exit()
        else:
            n = int(self.camera_num_1[-1])
            self.vid_EX=cv.VideoCapture(cam_list[n])
            self.open_video_Exit()

    


if __name__ =="__main__":
    obj = Main_windows("admin_1")

    mainloop()
 