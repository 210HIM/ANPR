from db_create import *
from tkinter import *
from tkinter import messagebox
import cv2 as cv
from PIL import ImageTk,Image

#db_create our own file that created for functions and 
# method that help to bild gui fream and also hendle login database

try: 
    class fream():

        def __init__(self) -> None:
            self.root = Tk()
            self.OTP = None

            # Admin_data refer to db_create 
            self.obj = Admnin_data(self.root)

            #main  screen
            self.root.geometry("800x500")
            self.root.title("ANPR/Login")

            frame=Frame(self.root,bg='gray')
            frame.place(x=0,y=0,width=800,height=500)

            self.main_img=Label(frame)
            self.main_img.pack()

            #Main  fream
            self.Datafreame2=Frame(self.root,background='#4caedb')
            self.Datafreame2.place(x=490,y=30,width=300,height=350)


            #title
            input_label=Label(self.Datafreame2,text='Login/Registr',fg='white',bg='#013764',font=("times new roman",13,'bold'),relief=RAISED,padx=10)
            input_label.grid(padx=0,pady=0)

            temp_lable=Label(self.Datafreame2,bg='#4caedb')
            temp_lable.grid(row=1,column=0)


            Login=Button(self.Datafreame2,text='Login',width=20,command=self.Login_user)
            Login.grid(row=2,column=1,pady=20)

            Login=Button(self.Datafreame2,text='Registration',width=20,command=self.New_user)
            Login.grid(row=4,column=1,pady=20)

            # lower 
            lower_frame=Frame(self.root,bd=1,bg='black')
            lower_frame.place(x=0,y=475,width=800,height=25)

            #lower/info buutn
            info=Button(lower_frame,text='info',command=self.info,bg='black',fg='white',relief=SUNKEN)
            info.place(x=0,y=0)

            #lower/exit buutn
            Exit=Button(lower_frame,text='Exit',command=quit,bg='black',fg='white',relief=SUNKEN)
            Exit.place(x=770,y=0)
            self.show_img()


        def info(self):
            masg ="""Welcome You . This is a 'ANPR' Login window . We are happy  to see you here, There are some information for you it's help you to login.\n1) Name Block : It is only conted  charecter please do not type number,sepecial charecter .\n2) Mobile number : It is alwees uniqe and atlist 10 digit \n3) Email Block : Please enter right email addres becuse when you want to reset your password that time on  your email send one 6digit OTP .
                    """
            messagebox.showinfo('Informetion',masg)

        # Show_img hendle by background img on Login gui fream 
        def show_img(self):
            img=cv.imread("main3.jpg")
            photo = cv.resize(img, (800,500))
            new_img=photo
                
            opencv_image = cv.cvtColor(new_img, cv.COLOR_BGR2RGBA)
            captured_image = Image.fromarray(opencv_image)
            photo_image = ImageTk.PhotoImage(image=captured_image)
            self.main_img.photo_image = photo_image
            self.main_img.configure(image=photo_image)

        # Inside Login_user Login funcnction refer to create_db file  
        def Login_user(self):
            self.obj.Login()

        # Inside New_user, Register funcnction refer to create_db file  
        def New_user(self):
            self.obj.Register()

except:
    messagebox.showerror('showerror',"GUI Not suported !")
    
        
        
obj = fream()
mainloop()