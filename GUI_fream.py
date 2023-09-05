from tkinter import *
from tkinter import messagebox
import cv2 as cv
from PIL import ImageTk,Image

class fream():

    def __init__(self) -> None:
        self.root = Tk()

        #main  screen
        self.root.geometry("800x500")
        self.root.title("ANPR/Login")

        frame=Frame(self.root,bg='gray')
        frame.place(x=0,y=0,width=800,height=500)

        self.main_img=Label(frame)
        self.main_img.pack()

        #Main  fream
        Datafreame2=Frame(self.root,background='#4caedb')
        Datafreame2.place(x=490,y=30,width=300,height=350)


        #title
        input_label=Label(Datafreame2,text='Login/Registr',fg='white',bg='#013764',font=("times new roman",13,'bold'),relief=RAISED,padx=10)
        input_label.grid(padx=0,pady=0)

        temp_lable=Label(Datafreame2,bg='#4caedb')
        temp_lable.grid(row=1,column=0)


        Login=Button(Datafreame2,text='Login',width=20,command=self.Login_user)
        Login.grid(row=2,column=1,pady=20)

        Login=Button(Datafreame2,text='Registration',width=20,command=self.New_user)
        Login.grid(row=4,column=1,pady=20)

        # lower 
        lower_frame=Frame(self.root,bd=1,bg='black')
        lower_frame.place(x=0,y=475,width=800,height=25)

        #lower/exit buutn
        Exit=Button(lower_frame,text='Exit',command=quit,bg='black',fg='white',relief=SUNKEN)
        Exit.place(x=760,y=0)
        self.show_img()

    def show_img(self):
        img=cv.imread('main3.jpg')
        photo = cv.resize(img, (800,500))
        # new_img=img[10:410,400:700]
        new_img = img

        opencv_image = cv.cvtColor(new_img, cv.COLOR_BGR2RGBA)
        captured_image = Image.fromarray(opencv_image)
        photo_image = ImageTk.PhotoImage(image=captured_image)
        self.main_img.photo_image = photo_image
        self.main_img.configure(image=photo_image)

    def Login_user(self):
        pass

    def New_user(self):
        pass
        
obj = fream()
mainloop()