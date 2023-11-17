import mysql
import mysql.connector

class Conecter:
    def __init__(self,admin_id):
        self.conn = None
        self.result = None
        self.admin_id = str(admin_id)
        file = open("Text\password.txt",'r')
        self.PWS = file.read()
        file.close()

    def get_admin_data(self):
        self.conn=mysql.connector.connect(host="localhost",username="root",password=self.PWS,database="anpr_final_db")
        self.my_cursor=self.conn.cursor()

        sql=f"SELECT * FROM anpr_final_db.admin_info where admin_id = '{self.admin_id}';"
        
        try:
            self.my_cursor.execute(sql)
            self.result=self.my_cursor.fetchall()
        except:
            print("In get_admin_data not conecter to data_base !")
        finally:
            self.conn.close()

        #print(self.result,"get_admin_data")
        return list(self.result[0])



# obj = Conecter('admin_1')
# print(obj.get_admin_data())

