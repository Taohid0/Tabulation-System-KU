import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox
import main

conn = pymysql.connect(user='root',password='')
cursor=conn.cursor()
from functools import partial
class Login ():
    win = tk.Tk()

    def login_info_check(self,username,password):


        try:
            cursor.execute("USE tabulationSystemKU")
            cursor.execute("SELECT * FROM login")
            #print(cursor.fetchone())

        except pymysql.Error as err:
            print(err)
        data = cursor.fetchone()
        #print(data[1],data[2],username,password)
       # print(data[1],username,data[2],password)
        if(data[1]==username and data[2]==password):
            Login.win.destroy()
            main.showMainPage()
        else:
            messagebox.showerror('ERROR',"Username and password mismatched")




    def show(self):

        Login.win.title('TABULATION SYSTEM KU')
        Login.win.minsize(width=300,height=400)
        Login.win.resizable(False,False)

        ttk.Label(Login.win,text="PLEASE LOGIN TO CONTINUE...").grid(column=0,row=0,pady=20)
        usernameVar = tk.StringVar()
        passwordVar = tk.StringVar()
        ttk.Label(Login.win,text="User Name : ").grid(column=0,row=1,pady=15)
        userName=tk.StringVar()
        userName.set('admin')
        ttk.Entry(Login.win,textvariable=userName).grid(column=1,row=1,sticky=tk.W)

        ttk.Label(Login.win,text="Password : ").grid(column=0,row=2)
        password=tk.StringVar()
        passwordEntry = ttk.Entry(Login.win,textvariable=password,show="*")
        passwordEntry.focus()
        passwordEntry.grid(column=1,row=2,sticky=tk.W)

        action_with_arg = partial(Login.login_info_check,self, usernameVar.get(),password.get())

        tk.Button(Login.win,background="khaki3",text='LOGIN',command=lambda : Login.login_info_check(None,userName.get(),password.get()),
                  width=10).grid(row=3,column=1,pady=15,padx=30)
        Login.win.mainloop()

    def loginUnitTest(self,):
        pass


