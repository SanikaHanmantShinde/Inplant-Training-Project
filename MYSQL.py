# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 23:05:26 2024

@author: Admin
"""

import mysql.connector
from tkinter import messagebox


def Save_Data_MySql(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R):
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="Sanika@123")
        mycursor=mydb.cursor()
        print("connection stablished")
    except:
        messagebox.showerror("connection","Database connection not stablished")
    try:
        
        command='create database Heart_Data'
        mycursor.execute(command)
        
        command = 'use Heart_Data'
        mycursor.execute(command)
        
        command = 'create table data(user int auto_increment key not null, Name varchar(50),Date varchar(50),DOB varchar(100), age varchar(100) , sex varchar(100), Cp varchar(100), trestbps varchar(100), chol varchar(100), fbs varchar(100), restecg varchar(100), thalach varchar(100), exang varchar(100),oldpeak varchar(100),slope varchar(100), ca varchar(100),thal varchar(100),result varchar(100))'
        mycursor.execute(command)

        command = 'insert into data(Name,Date,DOB,age,sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,Result) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        mycursor.execute(command,(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Register","New user added successfully!!!")
        
    except:
        # incase of daabase is not already existing
        mycursor.execute("use Heart_Data")
        mydb=mysql.connector.connect(host = "localhost",user="root",password="Sanika@123",database="Heart_Data")
        mycursor = mydb.cursor()
        
        command = 'insert into data(Name,Date,DOB,age,sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,Result) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        mycursor.execute(command,(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Register","New user added successfully!!!")

        