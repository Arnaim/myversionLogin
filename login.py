import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()
root.title("Login Page")
root.geometry("900x660+50+50")
root.configure(bg='#194d19')
root.resizable(0,0)

#commands
def login(): 
    username=username_entry.get()
    password=password_entry.get()
    #CREATE TABLE users (
    #id INT AUTO_INCREMENT PRIMARY KEY,
    #username VARCHAR(255) NOT NULL UNIQUE,
    #password VARCHAR(255) NOT NULL
    #);
    insert_query = "INSERT INTO `users`(`username`, `password`) VALUES (%s,%s)"
    vals = (username,password)
    c.execute(insert_query,vals)
    connection.commit()
def signup():
    root.destroy()
    import signup.py
#widgets
heading=Label(root,text="LOGIN", bg="#194d19", fg="#ffffff", font=("Arial", 60))
username=Label(root, text="Usename",bg="#194d19", fg="#ffffff", font=("Arial",20))
username_entry=Entry(root,width=25,font=("Arial", 20))
password=Label(root, text="Password",bg="#194d19", fg="#ffffff", font=("Arial",20))
password_entry=Entry(root,width=25,font=("Arial", 20), show="*")
login_button=tk.Button(root, text="Login", bg='#ffffff', fg='#194d19',font=('Ariel',20),cursor="hand2", bd=0, width=10)
new_acc=Label(root,text="New here? Click to signup~",bg="#194d19", fg="#ffffff", font=("Arial",10))
signup_button=tk.Button(root, text="Signup", bg='#194d19', fg='#ffffff',font=('Ariel',10, "bold underline"),cursor="hand2", bd=0, command=signup)

#postion
heading.place(y=100, x=300)
username.place(y=200,x=300)
username_entry.place(y=200, x=430)
password.place(y=270,x=300)
password_entry.place(y=270, x=430)
login_button.place(y=330,x=300)
new_acc.place(y=400,x=300)
signup_button.place(y=400,x=470)
root.mainloop()