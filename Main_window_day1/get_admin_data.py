import mysql
import mysql.connector

class Conecter:
    def __init__(self,admin_id):
        self.conn = None
        self.result = None
        self.admin_id = admin_id

    def get_admin_data(self):
        self.conn=mysql.connector.connect(host="localhost",username="root",password="rakesh",database="admin_data")
        self.my_cursor=self.conn.cursor()
        sql='''SELECT * FROM admin_data.admin_info'''
        

        try:
            self.my_cursor.execute(sql)
            self.result=self.my_cursor.fetchall();
        except:
            print("In get_admin_data not conecter to data_base !")

        
        for data in self.result:
            if self.admin_id in data:
                return list(data)