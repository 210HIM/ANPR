import mysql 
import mysql.connector

conn=mysql.connector.connect(host="localhost",username="root",password="rakesh",database="rto_copy")
my_cursor=conn.cursor()
sql=""" INSERT INTO rto_copy.rto(Vehicle_number,name,mobile_num,email,address) VALUES(%s,%s,%s,%s,%s)"""
#data=('MH28MG4241','raj','9098101351','himanshukalambe22@gmail.com','bhopal')

Name=['riya', 'ranya', 'Priyanka', 'divya', 'tanvi', 'Ishita', 'ani', 'jali', 'Shreya', 'riya']

Vehicle_number = "MH28MG4241"
for i in range(len(Name)):
    name = Name[i]
    Vehicle_number += str(i)
    email = "hkalambe007@gmail.com"
    mobile_num = "7570459835"
    adreess = "Bhopal"
    data = (Vehicle_number, name, mobile_num, email, adreess)

    try:
        my_cursor.execute(sql,data)
        conn.commit()
        print("ok")
    except:
        print("Not ok")



try:
    sql='''SELECT * FROM rto_copy.rto'''
    my_cursor.execute(sql)
    result=my_cursor.fetchall();
    for i in range(len(result)):
        print(result[i])
except:
    print("data not updated")
finally:
    conn.close()
