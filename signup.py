import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()
root.title("Login Page")
root.geometry("900x660+50+50")
root.configure(bg='#194d19')
root.resizable(0,0)

connection = mysql.connector.connect(host='localhost', user='Pandora', password='aTaE8Epz1y',
                                     port='3306', database='serenity')
c = connection.cursor()

#commands
def signup():
    email=email_entry.get()
    username=username_entry.get()
    password=password_entry.get()
    insert_query = "INSERT INTO `signup`(`email`,`username`, `password`) VALUES (%s,%s,%s)"
    vals = (email,username,password)
    c.execute(insert_query,vals)
    connection.commit()
    """
    CREATE TABLE signup (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
"""


def login():
    root.destroy()
    import login.py

#widgets
heading=Label(root,text="SIGN UP", bg="#194d19", fg="#ffffff", font=("Arial", 60))
email=Label(root, text="Email", bg="#194d19", fg="#ffffff", font=("Arial",20))
email_entry=Entry(root,width=25,font=("Arial", 20))
username=Label(root, text="Usename",bg="#194d19", fg="#ffffff", font=("Arial",20))
username_entry=Entry(root,width=25,font=("Arial", 20))
password=Label(root, text="Password",bg="#194d19", fg="#ffffff", font=("Arial",20))
password_entry=Entry(root,width=25,font=("Arial", 20), show="*")
signup_button=tk.Button(root, text="Sign Up", bg='#ffffff', fg='#194d19',font=('Ariel',20),cursor="hand2", bd=0, width=10, command=signup)
already_acc=Label(root,text="Already have an account?", bg="#194d19", fg="#ffffff", font=("Arial",10))
login_button=tk.Button(root, text="Login", bg='#194d19', fg='#ffffff',font=('Ariel',10, "bold underline"),cursor="hand2", bd=0, command=login)
#postion
heading.place(y=100, x=270)
email.place(y=200,x=270)
email_entry.place(y=200,x=400)
username.place(y=250,x=270)
username_entry.place(y=250, x=400)
password.place(y=300,x=270)
password_entry.place(y=300, x=400)
signup_button.place(y=370,x=270)
already_acc.place(y=450,x=270)
login_button.place(y=450,x=430)



root.mainloop()