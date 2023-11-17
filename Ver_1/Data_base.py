from Passwoed import PASS_WORD
from tkinter import *
from tkinter import messagebox
from Passwoed import *
import mysql 
import mysql.connector
import os


class db:
    def add_pass(self):
        # P = PASS_WORD()
        # P.get_password()
        try:
            file = open("Text/password.txt",'r')
            self.PSW = file.read()
            file.close()
        except:
            print("Password not get")

    def create_data_base(self):
        self.add_pass()
        conn=mysql.connector.connect(host="localhost",username="root",password=self.PSW)
        my_cursur = conn.cursor()

        sql = "CREATE  SCHEMA IF NOT EXISTS `anpr_final_db`;"

        sql_1 = """CREATE TABLE IF NOT EXISTS `anpr_final_db`.`admin_info` (
        `admin_id` VARCHAR(45) NOT NULL,
        `password` VARCHAR(45) NULL,
        `admin_name` VARCHAR(45) NULL,
        `email` VARCHAR(45) NULL,
        `mobile_num` VARCHAR(10) NULL,
        PRIMARY KEY (`admin_id`));
        """
        
        sql_2 = """CREATE TABLE IF NOT EXISTS `anpr_final_db`.`owner_data` (
        `Vehicle_number` VARCHAR(45) NOT NULL,
        `owner_name` VARCHAR(45) NOT NULL,
        `mobile_num` VARCHAR(12) NOT NULL,
        `email_id` VARCHAR(45) NOT NULL,
        `address` VARCHAR(45) NOT NULL,
        PRIMARY KEY (`Vehicle_number`));"""

        sql_3 =""" CREATE TABLE IF NOT EXISTS `anpr_final_db`.`rto` (
        `index` INT NOT NULL AUTO_INCREMENT,
        `Vehicle_number` VARCHAR(45) NULL,
        `Entry_time` DATETIME(6) NULL,
        `Exit_time` DATETIME(6) NULL,
        PRIMARY KEY (`index`),
        UNIQUE INDEX `index_UNIQUE` (`index` ASC) VISIBLE);"""

        try:
            my_cursur.execute(sql)
            conn.commit()

            my_cursur.execute(sql_1)
            conn.commit()

            my_cursur.execute(sql_2)
            conn.commit()

            my_cursur.execute(sql_3)
            conn.commit()


        except:
            messagebox.showwarning("DataBase is not created due to Internet conection")
        finally:
            conn.close()
            
