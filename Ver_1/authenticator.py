from tkinter import *
from tkinter import messagebox
import smtplib
from email.message import EmailMessage
import random

class check:
    def __init__(self):
        self.root = None

    def send_otp_mes(self):
        self.root = Tk()
        self.root.geometry("400x300")
        self.root.title("Authenticator")
        lab_1 = Label(self.root, text="YOU HAVE ONLY ONE CHANCE TO START APPLICATION \nOTHER VOICE THIS IS DELETED",
                      font=("arial",10,'bold'),fg="red")
        lab_1.place(x=25, y=2)
        lab_2 = Label(self.root,text="Get Authenticator code",font=("arial",10,'bold')).place(x=5,y=50)

        send_butt=Button(self.root,text="SEND",command=self.maile_otp)
        send_butt.place(x=170,y=50)

        lab_3=Label(self.root,text="Enter Authenticator code",font=("arial",10,'bold')).place(x=5,y=100)
        self.password = Entry(self.root,font=("arial",10,'bold'))
        self.password.place(x=170,y=100)

        process_butt= Button(self.root,text="PROCESS",font=("arial",10,'bold'),fg="green",command=self.check_otp)
        process_butt.place(x=120,y=150)

    def maile_otp(self):
        self.OTP = random.randint(10000, 99999)
        print(self.OTP)
        try:
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login('rytcareer14@gmail.com','nqmmdsxvgfzyguxw')
            email = EmailMessage()
            masg = str(self.OTP)
            #email['From'] =
            email['To'] ="hkalambe007@gmail.com"
            email['Subject'] = 'OTP'
            email.set_content(masg)
            server.send_message(email)
        except:
            messagebox.showerror('Error',"The internet connection is not scalable.")

    def check_otp(self):
        copy = self.password.get()
        if copy == str(self.OTP):
            self.root.destroy()
        else:
            self.root.quit()



obj = check()
obj.send_otp_mes()
mainloop()


