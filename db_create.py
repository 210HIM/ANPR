import mysql 
import mysql.connector

conn=mysql.connector.connect(host="localhost",username="root",password="rakesh",database="admin_data")
my_cursur = conn.cursor()

q1="""CREATE TABLE IF NOT EXISTS `admin_data`.`admin_info` (
  `admin_id` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `admin_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `mobile_num` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`admin_id`));"""
try:
    my_cursur.execute(q1)
    conn.commit()
except:
    print("not done")
finally:
    conn.close()



class Admnin_data:

    def __init__(self):
        self.name = ''
        self.admin_id = ''
        self.mobile_num = ''
        self.email = ''
        self.password = ''


        conn=mysql.connector.connect(host="localhost",username="root",password="rakesh",database="anpr")
        my_cursor=conn.cursor()
        sql='''SELECT * FROM anpr.user_data'''
        my_cursor.execute(sql)
        self.result=my_cursor.fetchall();
        #close connection here after completed programme @@@@@@

    def Login(self):
        print("user login Done !")

    def get_data(self):
        self.name = input("Enter Name: ")
        self.email = input("Enter email :")
        self.password = input("Enter password :")
        self.mobile_num = input("Enter mobile_num :")

    def Register(self):
        self.get_data()

        if len(self.name) == 0 or len(self.mobile_num) == 0 or len(self.password) == 0 or len(self.email)==0:
            print("Data not complited !")

        #chck name is coorect or not
        if self.name.isalpha() == False:
            print('Name contains only characters')

        #Mobile nummber chcek
        if len(self.mobile_num) == 10 :
            for i in range(len(self.result)):
                if self.mobile_num in  list(self.result[i]):
                    #show erroe masege mobile number is incurect
                    print("Warning","Mobile no. is already registered please try again")
                    
        else:
            #show erroe masege mobile number is incurect
            print("Information","Mobile no. is invalid please try again")
            return 2

        self.Login()

obj = Admnin_data()
obj.Register()