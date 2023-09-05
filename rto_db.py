import mysql
import mysql.connector
import random

def number():
    return str(random.randint(1000000000,9999999999))

#Conection whit database and fech data 
conn=mysql.connector.connect(host="localhost",username="root",password="rakesh",database="rto_copy")
my_cursor=conn.cursor()



SQL='''INSERT INTO rto_copy.rto('vehicle_number', 'name', 'mobile_num', 'email', 'address') VALUES(%s,%s,%s,%s,%s);'''


# SQL = """INSERT INTO `rto_copy`.`rto` (` vehicle_number`, `name`, `mobile_num`, `email`, `address`) VALUES ('MH02AB1239', 'Abishek', '7470459835', 'hkalambe007@gmail.com', 'bhopal');"""

text = ['riya', 'ranya', 'Priyanka', 'divya', 'tanvi', 'Ishita', 'ani', 'jali', 'Shreya', 'riya', 'Sneha', 'shwarya', 'Gayatri', 'varsha', 'Ira', 'sanjana', 'Niharika', 'Nikita', 'natasha', 'Neha', 'ahul', 'Abhishek', 'Aditya', 'Amit', 'Mahesh', 'ROHIT', 'Yash', 'Ankit', 'shyam', 'Deepak', 'Aryan', 'Raj', 'Arjun', 'Manoj', 'ankur', 'kash', 'Karan', 'Rakesh', 'Sam', 'Naveen', 'Ashish', 'Vinay', 'Parth', 'Mayank', 'ivek', 'ananya', 'shivani', 'sakshi', 'Aswini', 'Suhani', 'leah', 'Pavithra', 'Seema', 'Anusha', 'simran', 'nishi', 'Anushri', 'Ayushi', 'Radhika', 'tanu', 'krithika', 'Anisha', 'Akansha', 'Sadaf', 'Nishita', 'diya', 'Siya', 'bigail', 'Kalyani', 'Rishitariya', 'ranya', 'Priyanka', 'divya', 'tanvi', 'Ishita', 'ani', 'jali', 'Shreya', 'riya', 'Sneha', 'shwarya', 'Gayatri', 'varsha', 'Ira', 'sanjana', 'Niharika', 'Nikita', 'natasha', 'Neha', 'ahul', 'Abhishek', 'Aditya', 'Amit', 'Mahesh', 'ROHIT', 'Yash', 'Ankit', 'shyam', 'Deepak', 'Aryan', 'Raj', 'Arjun', 'Manoj', 'ankur', 'kash', 'Karan', 'Rakesh', 'Sam', 'Naveen', 'Ashish', 'Vinay', 'Parth', 'Mayank', 'ivek', 'ananya', 'shivani', 'sakshi', 'Aswini', 'Suhani', 'leah', 'Pavithra', 'Seema', 'Anusha', 'simran', 'nishi', 'Anushri', 'Ayushi', 'Radhika', 'tanu', 'krithika', 'Anisha', 'Akansha', 'Sadaf', 'Nishita', 'diya', 'Siya', 'bigail', 'Kalyani', 'Rishita']


for i in range(10):
    #   INSERT DATA INTO DATABASE
    vehicle_number = "MH02AB1239"
    mobile_num = number()
    email = "hkalambe007@gmail.com"
    address = "Bhopal"
    name = text[i]

    data=(vehicle_number,name,mobile_num,email,address)
    try:
        my_cursor.execute(SQL,data)
        conn.commit()
        
        sql='''SELECT * FROM rto_copy.rto ;'''
        my_cursor.execute(sql)
        result=my_cursor.fetchall();
        print(result)
    except:
        print('not update data')
    finally:
        conn.close()
























# d

# try:
#     my_cursor.execute(SQL,data)
#     conn.commit()
# except:
#     print('not update data')

# # for i in range(len(da)):
# #     vehicle_number += str(i)
# #     name = da[i]
# #     mobile_num = number()
# #     email = "hkalambe007@gmail.com"
# #     address = "Bhopal"
# #     data=(vehicle_number,name,mobile_num,email,address)
# #     try:
# #         my_cursor.execute(SQL,data)
# #         conn.commit()
# #     except:
# #         print('not update data')

# # 20:57:53	INSERT INTO `rto_copy`.`rto` (` vehicle_number`, `name`, `mobile_num`, `email`, `address`) VALUES ('MH02AB1234', 'Mhoan', '7894561230', 'hkalambe007@gmail.com', 'bhopal')	1366: Incorrect integer value: 'MH02AB1234' for column ' vehicle_number' at row 1	
