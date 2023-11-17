import mysql
import mysql.connector

#Conection whit database and fech data 
conn=mysql.connector.connect(host="localhost",username="root",password="rakesh",database="rto_copy")
my_cursor=conn.cursor()

text = ["MH-28-3985","Himanhu_2","9098101356","hk.com","bhopal"]
q2 = """INSERT INTO rto_copy.owner_data (Vehicle_number,owner_name,mobile_num,email_id,address) VALUES (%s, %s, %s, %s, %s);"""
data = (text[0],text[1],text[2],text[3],text[4])
try:
    my_cursor.execute(q2,data)
    conn.commit()
except:
    print("not done")

