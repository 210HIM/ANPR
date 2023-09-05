import mysql 
import mysql.connector

def create_db():
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


        self.conn=mysql.connector.connect(host="localhost",username="root",password="rakesh",database="admin_data")
        self.my_cursor=self.conn.cursor()
        sql='''SELECT * FROM admin_data.admin_info'''
        self.my_cursor.execute(sql)
        self.result=self.my_cursor.fetchall();
        #close connection here after completed programme @@@@@@

        print(self.result)

    def Login(self):
        #user_id creation 
        if len(self.result) > 0:
            temp=list(self.result[-1])
            x=temp[0]
            a,b=x.split('_')
            self.admin_id='admin_'+str(int(b)+1)
        else:
            self.admin_id = "admin_1"

        print(f"{self.admin_id},{self.password},{self.name},{self.mobile_num},{self.email}")

        q1 = """INSERT INTO admin_data.admin_info(admin_id,password,admin_name,email,mobile_num) VALUES(%s,%s,%s,%s,%s)"""
        data = (self.admin_id, self.password, self.name, self.email, self.mobile_num)
        try:
            self.my_cursor.execute(q1,data)
            self.conn.commit()
        except:
            print("not done")
        finally:
            self.conn.close()
            

    def get_data(self):
        self.name = input("Enter Name: ")
        self.email = input("Enter email :")
        self.password = input("Enter password :")
        self.mobile_num = input("Enter mobile_num :")

    def Register(self):
        self.get_data()

        while True :

            if len(self.name) == 0 or len(self.mobile_num) == 0 or len(self.password) == 0 or len(self.email)==0:
                print("Data not complited !")
                continue

            #chck name is coorect or not
            if self.name.isalpha() == False:
                print('Name contains only characters')
                

            #Mobile nummber chcek
            if len(self.mobile_num) == 10 :
                if len(self.result) == 0:
                    break
                for i in range(len(self.result)):
                    if self.mobile_num in  list(self.result[i]):
                        #show erroe masege mobile number is incurect
                        print("Warning","Mobile no. is already registered please try again")
                        continue
                        
            else:
                #show erroe masege mobile number is incurect
                print("Information","Mobile no. is invalid please try again")
                continue
            
            break

        self.Login()

obj = Admnin_data()
obj.Register()






