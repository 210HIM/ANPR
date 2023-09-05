from tkinter import *
from tkinter import messagebox
import cv2 as cv
from PIL import ImageTk,Image
import mysql
import mysql.connector
from mysql.connector import cursor
import datetime as dt
#import Demo1

def print_msg(titel,msg):
    messagebox.showinfo(titel,msg)

def show_img(label_widget,path,x=400,y=700,r=0):
    img=cv.imread(path)
    photo = cv.resize(img, (x,y))
    if r==1:
        new_img=img[10:410,400:700]
    else:
        new_img=img

    opencv_image = cv.cvtColor(new_img, cv.COLOR_BGR2RGBA)
    captured_image = Image.fromarray(opencv_image)
    photo_image = ImageTk.PhotoImage(image=captured_image)
    label_widget.photo_image = photo_image
    label_widget.configure(image=photo_image)

def check_data(name,password,mobilno,email):
    #Conection whit database and fech data 
    conn=mysql.connector.connect(host="localhost",username="root",password="rakesh",database="anpr")
    my_cursor=conn.cursor()
    sql='''SELECT * FROM anpr.user_data'''
    my_cursor.execute(sql)
    result=my_cursor.fetchall();

    # check all data is fille or not 
    if len(name) == 0 or len(mobilno) == 0 or len(password) == 0 or len(email)==0:
        messagebox.showwarning('Warning','Fill all data')

    #chck name is coorect or not
    if name.isalpha() == False:
        print_msg('Information','Name contains only characters')
        return 0

    #Mobile nummber chcek
    if len(mobilno) == 10 :
        for i in range(len(result)):
            if mobilno in  list(result[i]):
                #show erroe masege mobile number is incurect
                messagebox.showwarning("Warning","Mobile no. is already registered please try again")
                return 2
    else:
        #show erroe masege mobile number is incurect
        messagebox.showwarning("Information","Mobile no. is invalid please try again")
        return 2



    #user_id creation 
    temp=list(result[-1])
    x=temp[0]
    a,b=x.split('_')
    user_id='admin_'+str(int(b)+1)

    #   INSERT DATA INTO DATABASE
    SQL='''INSERT INTO user_data(user_id,password,user_name,mobile_no,email_id)VALUES(%s,%s,%s,%s,%s)'''
    data=(user_id,password,name,mobilno,email)

    try:
        my_cursor.execute(SQL,data)
        conn.commit()
    except:
        print('not update data')
        return 
    msg='Congratulations your account has been created \n user_id:-  '+user_id
    messagebox.showinfo('Upadet',msg)
    conn.close()
    Login_user()
#------------------------------------------------------------------------------------------
def check_Login_data(userid,Password):
    #Conection whit database and fech data 
    conn=mysql.connector.connect(host="localhost",username="root",password="rakesh",database="anpr")
    my_cursor=conn.cursor()
    sql='''SELECT * FROM anpr.user_data'''
    my_cursor.execute(sql)
    result=my_cursor.fetchall();

    for i in range(len(result)):
        if userid in list(result[i]) and Password in list(result[i]):
            messagebox.showinfo("Information","Login  Successfully !.")
            conn.close()
            return True
    
    messagebox.showwarning('Alert',"Invalid user id and password .\n Try again")
    
    conn.close()

def Login_user():
    Datafreame2=Frame(root,background='#4caedb')
    Datafreame2.place(x=490,y=30,width=300,height=350)  
    #title
    input_label=Label(Datafreame2,text='Login',fg='white',bg='#013764',font=("times new roman",13,'bold'),relief=RAISED,padx=10)
    input_label.grid(padx=0,pady=0)

    temp_lable=Label(Datafreame2,bg='#4caedb')
    temp_lable.grid(row=1,column=0)

    #user_id
    user_id=Label(Datafreame2,text="USER -ID:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=2,column=0,pady=15,sticky=W)

    user_id_entry=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
    user_id_entry.grid(row=2,column=1,padx=5)

    #pass_word
    Password=Label(Datafreame2,text="Password:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=3,column=0,pady=15,sticky=W)

    Pass_entry=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
    Pass_entry.grid(row=3,column=1,padx=5)

    
    def get_data():
        msg1=user_id_entry.get()
        msg2=Pass_entry.get()

        val=check_Login_data(userid=msg1,Password=msg2)
            

        if val == True:
            error_msg=Label(Datafreame2,text=msg1+msg2,font=("arial",10,"bold"),fg='red',bg='#81c3e5',width=25,height=5)
            error_msg.grid(row=7,column=1,pady=25)
            #Demo1.
            new_windows()

        user_id_entry.delete(0,END)
        Pass_entry.delete(0,END)

    Login_butt=Button(Datafreame2,text='Sig in',width=15,command=get_data)
    Login_butt.grid(row=5,column=1)

    BACK=Button(Datafreame2,text='Register',width=15,command=New_user)
    BACK.grid(row=7,column=1,pady=15)


def New_user():
    Datafreame2=Frame(root,background='#4caedb')
    Datafreame2.place(x=490,y=30,width=300,height=350)

    #title
    input_label=Label(Datafreame2,text='Registration',fg='white',bg='#013764',font=("times new roman",13,'bold'),relief=RAISED)
    input_label.grid(padx=0,pady=0)

    temp_lable=Label(Datafreame2,bg='#4caedb')
    temp_lable.grid(row=1,column=0,padx=10)

    #user_id
    Name=Label(Datafreame2,text="Name:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=2,column=0,pady=15,sticky=W)

    user_Name_entry=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
    user_Name_entry.grid(row=2,column=1,padx=5)

    #mobil_number
    Mobil_no=Label(Datafreame2,text="Mobil No:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=3,column=0,pady=15,sticky=W)

    user_mobil_entry=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
    user_mobil_entry.grid(row=3,column=1,padx=5)

    #email
    emil=Label(Datafreame2,text="Email -Id:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=4,column=0,pady=15,sticky=W)

    user_Email_entry=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
    user_Email_entry.grid(row=4,column=1,padx=5)

    #pass_word
    Password=Label(Datafreame2,text="Password:",font=("arial",10,"bold"),padx=2,pady=4,fg='white',bg='#0071a7').grid(row=5,column=0,pady=15,sticky=W)

    Pass_entry=Entry(Datafreame2,font=("arial",10,"bold"),bg='#81c3e5',width=22,fg='black')
    Pass_entry.grid(row=5,column=1,padx=5)

    def get_data():
        msg1=user_Name_entry.get()
        msg2=Pass_entry.get()
        msg3=user_mobil_entry.get()
        msg4=user_Email_entry.get()

        val=check_data(name=msg1,password=msg2,mobilno=msg3,email=msg4)

        if val == 0:
            msg1=user_Name_entry.delete(0,END)
           # val=check_data(name=msg1,password=msg2,mobilno=msg3,email=msg4)
        elif val == 1:
            msg2=Pass_entry.delete(0,END)
            #val=check_data(name=msg1,password=msg2,mobilno=msg3,email=msg4)
        elif val == 2:
            msg3=user_mobil_entry.delete(0,END)
           # val=check_data(name=msg1,password=msg2,mobilno=msg3,email=msg4)
        elif val == 3:
            msg4=user_Email_entry.delete(0,END)
           # val=check_data(name=msg1,password=msg2,mobilno=msg3,email=msg4)


    Login_butt=Button(Datafreame2,text='Register',width=15,command=get_data)
    Login_butt.grid(row=7,column=1,pady=5)

    BACK=Button(Datafreame2,text='Login',width=15,command=Login_user)
    BACK.grid(row=9,column=1,padx=5)







#main  screen
root=Tk()
root.geometry("800x500")
root.title("ANPR/Login")

frame=Frame(root,bg='gray')
frame.place(x=0,y=0,width=800,height=500)

main_img=Label(frame)
main_img.pack()

#Main  fream
Datafreame2=Frame(root,background='#4caedb')
Datafreame2.place(x=490,y=30,width=300,height=350)


#title
input_label=Label(Datafreame2,text='Login/Registr',fg='white',bg='#013764',font=("times new roman",13,'bold'),relief=RAISED,padx=10)
input_label.grid(padx=0,pady=0)

temp_lable=Label(Datafreame2,bg='#4caedb')
temp_lable.grid(row=1,column=0)


Login=Button(Datafreame2,text='Login',width=20,command=Login_user)
Login.grid(row=2,column=1,pady=20)


Login=Button(Datafreame2,text='Registration',width=20,command=New_user)
Login.grid(row=4,column=1,pady=20)
# lower 
lower_frame=Frame(root,bd=1,bg='black')
lower_frame.place(x=0,y=475,width=800,height=25)

#lower/exit buutn
Exit=Button(lower_frame,text='Exit',command=quit,bg='black',fg='white',relief=SUNKEN)
Exit.place(x=760,y=0)


class platform():
    def __init__(self,root) -> None:

        vid=cv.VideoCapture(0)
        #vid=cv.VideoCapture(0)

        width, height = 1000, 400
        vid.set(cv.CAP_PROP_FRAME_WIDTH, width)
        vid.set(cv.CAP_PROP_FRAME_HEIGHT, height)

        def open_video():
            isTrue , frame =vid.read()

            #date and time
            temp=dt.datetime.now()
            date_time=list(str(temp).split())

            time_entry=Label(Datafreame2,font=("arial",13,"bold"),text=date_time[1],width=30,bg='white')
            time_entry.grid(row=3,column=2)

            cv.putText(frame,str(temp),(50,350),cv.FONT_HERSHEY_TRIPLEX,0.50,(0,255,0),1)
            cv.rectangle(frame,(730,420),(2,180),(0,255,0),thickness=2)
            opencv_image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
            captured_image = Image.fromarray(opencv_image)
            photo_image = ImageTk.PhotoImage(image=captured_image)
            label_widget1.photo_image = photo_image
            label_widget1.configure(image=photo_image)
            label_widget1.after(25, open_video)


        self.root=root
        self.root.title("Automatic License/Number Plate Recognition (ANPR)")
        self.root.geometry("1540x800+0+0")

        lalttitle=Label(self.root,bd=5,relief=RAISED,text="Automatic License/Number Plate Recognition (ANPR)",fg='black',bg='cyan',font=("times new roman",20,'bold'))
        lalttitle.pack(side=TOP,fill=X)

        # video block 

        #left video fream
        Datafreame1=Frame(self.root,bd=5,padx=20,bg='Black',relief=RIDGE)
        Datafreame1.place(x=10,y=50,width=1000,height=400)

        label_widget1 =Label(Datafreame1,bg='black')
        label_widget1.pack()

        

        #righ video fream
        Datafreame2=Frame(self.root,bd=5,padx=20,relief=GROOVE)
        Datafreame2.place(x=1020,y=50,width=500,height=400)

        #left fream data
        Datafreame1_left1=Frame(self.root,bd=5,padx=20,bg='black',relief=SUNKEN )
        Datafreame1_left1.place(x=0,y=460,width=380,height=300)

        img_label_1=Label(Datafreame1_left1,bg='black')
        img_label_1.pack()

        Datafreame1_left2=Frame(self.root,bd=5,padx=20,bg='black',relief=SUNKEN )
        Datafreame1_left2.place(x=385,y=460,width=375,height=300)

        img_label_2=Label(Datafreame1_left2,bg='black')
        img_label_2.grid(row=4,column=2)

         # right fream data

        Datafreame2_right1=Frame(self.root,bd=5,padx=20,relief=RIDGE )
        Datafreame2_right1.place(x=770,y=460,width=375,height=300)

        Datafreame2_right2=Frame(self.root,bd=5,padx=20,bg='white',relief=SUNKEN )
        Datafreame2_right2.place(x=1150,y=460,width=380,height=300)

        #Deatels of right fream
        Left_title=Label(Datafreame2,text='Camera Settings',fg='black',bg='white',font=("times new roman",15,'bold'),relief=RAISED)
        Left_title.grid(row=0,column=0,sticky=S)


        temp_lable=Label(Datafreame2,padx=2,pady=4)
        temp_lable.grid(row=1,column=0)

        #1

        temp=dt.datetime.now()
        date_time=list(str(temp).split())

        date_label=Label(Datafreame2,font=("arial",12),text="Date:",padx=2,pady=6)
        date_label.grid(row=2,column=0,sticky=W)

        date_entry=Label(Datafreame2,font=("arial",13,"bold"),text=date_time[0],width=30,bg='white')
        date_entry.grid(row=2,column=2)

        #2
        time_label=Label(Datafreame2,font=("arial",12),text="Time:",padx=2,pady=6)
        time_label.grid(row=3,column=0,sticky=W)

        # time_entry=Label(Datafreame2,font=("arial",13,"bold"),text=date_time[1],width=30,bg='white')
        # time_entry.grid(row=3,column=2)

        #3
        Location=Label(Datafreame2,font=("arial",12),text="Location:",padx=2,pady=6)
        Location.grid(row=4,column=0,sticky=W)

        Location_entry=Entry(Datafreame2,font=("arial",13,"bold"),width=35,bg='white')
        Location_entry.grid(row=4,column=2)

        #4
        fine_label=Label(Datafreame2,font=("arial",12),text="Fine amount:",padx=2,pady=6)
        fine_label.grid(row=5,column=0,sticky=W)

        fine_entry=Entry(Datafreame2,font=("arial",13,"bold"),width=35,bg='white')
        fine_entry.grid(row=5,column=2)

        #5
        cartype_label=Label(Datafreame2,font=("arial",12),text="Type:",padx=2,pady=6)
        cartype_label.grid(row=6,column=0,sticky=W)

        type_entry=Entry(Datafreame2,font=("arial",13,"bold"),width=35,bg='white')
        type_entry.grid(row=6,column=2)

        #6
        cartype_label=Label(Datafreame2,font=("arial",12),text="Camera no:",padx=2,pady=6)
        cartype_label.grid(row=7,column=0,sticky=W)

        cartype_entry=Entry(Datafreame2,font=("arial",13,"bold"),width=35,bg='white')
        cartype_entry.grid(row=7,column=2)

        #7

        Update_buttun=Button(Datafreame2,text='UPDATE',activebackground='green',width=20)
        Update_buttun.grid(row=9,column=2)

        #8

        count_label=Label(Datafreame2,font=("arial",12),text="count:",padx=2,pady=6)
        count_label.grid(row=10,column=0,sticky=W)

        count_print=Label(Datafreame2,font=("arial",13,"bold"),text='0',width=30,bg='white')
        count_print.grid(row=10,column=2)

        #9
        Update_buttun=Button(Datafreame2,text='Exit',activebackground='green',width=20,command=quit)
        Update_buttun.grid(row=12,column=2)

        #10
        Update_buttun=Button(Datafreame2,text='Stop/Poss',activebackground='green',width=20)
        Update_buttun.grid(row=11,column=2)

        open_video()

def new_windows():
    ROOT=Tk()
    application=platform(ROOT)
    root.mainloop()












show_img(main_img,'main3.jpg',800,500)
#show_img(label2,'main3.jpg',800,500,1)
root.mainloop()