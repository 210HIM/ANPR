from datetime import datetime
from tkinter import messagebox
import mysql.connector


def add_pass():
    try:
        file = open("Text/password.txt", 'r')
        PWS = file.read()
        file.close()
        return PWS
    except:
        print("Password not get")



def update_entry_get(number_p):
    PWS = add_pass()
    time = str(datetime.now())
    conn = mysql.connector.connect(host="localhost", username="root", password=PWS ,database="anpr_final_db")
    my_cursor = conn.cursor()
    sql = "INSERT INTO `anpr_final_db`.`rto` (`Vehicle_number`, `Entry_time`) VALUES (%s,%s);"
    data = (number_p,time)
    try:
        my_cursor.execute(sql,data)
        conn.commit()
        messagebox.showinfo("Informetion", "Data updated ")
    except:
        messagebox.showerror("Error","Data is not update server probalme ")
    finally:
        conn.close()



def update_Exit_get(number_p):
    PWS = add_pass()
    time = str(datetime.now())
    conn = mysql.connector.connect(host="localhost", username="root", password=PWS, database="anpr_final_db")
    my_cursor = conn.cursor()
    sql = "SELECT * FROM anpr_final_db.rto where Vehicle_number = %s or Exit_time = %s;"
    data = (number_p,None)
    try:
        my_cursor.execute(sql,data)
        result = (my_cursor.fetchall())
        conn.commit()
    except:
        messagebox.showerror("Error", "Data is not update server probalme 1 ")
    finally:
        conn.close()

    index = None
    for i in range(len(result)):
        if result[i][-1] == None:
            index = result[i][0]

    conn = mysql.connector.connect(host="localhost", username="root", password="rakesh", database="anpr_final_db")
    my_cursor = conn.cursor()
    q1 = "UPDATE`anpr_final_db`.`rto`SET`Exit_time` =  %s WHERE(`index` = %s);"
    d = (time,index)
    try:
        my_cursor.execute(q1,d)
        conn.commit()
        messagebox.showinfo("Informetion", "Data updated ")
    except:
        messagebox.showerror("Error", "Data is not update server probalme ")
    finally:
        conn.close()


# update_Exit_get("MH20EE7598")

