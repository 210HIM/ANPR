# import mysql
# import mysql.connector
# Pass = "123456"
# conn=mysql.connector.connect(host="localhost",username="root",password="rakesh",database="admin_data")
# my_cursor=conn.cursor()
# sql = '''UPDATE `admin_data`.`admin_info` SET `password` = %s WHERE (`admin_id` = %s);'''
# data = (Pass ,'admin_1')

# try:
#     my_cursor.execute(sql,data)
#     conn.commit()
#     print("Password chnage and save")
# except:
#     print("New password is not change and save ")
# finally:
#     conn.close()





import tkinter as tk
from tkinter import Button, ttk

def GET():
    print(n.get())

# Creating tkinter window
window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')

# label text for title
ttk.Label(window, text = "GFG Combobox Widget",
		background = 'green', foreground ="white",
		font = ("Times New Roman", 15)).grid(row = 0, column = 1)

# label
ttk.Label(window, text = "Select the Month :",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 5, padx = 10, pady = 25)

# Combobox creation
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)

# Adding combobox drop down list
monthchoosen['values'] = (' January',
						' February',
						' March',
						' April',
						' May',
						' June',
						' July',
						' August',
						' September',
						' October',
						' November',
						' December')

monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()
bu=Button(window,text = "Get data",command = GET).grid(row = 7, column = 1)

window.mainloop()
