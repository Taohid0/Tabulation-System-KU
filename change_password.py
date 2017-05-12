from tkinter import *
import pymysql
from tkinter import ttk
from tkinter import messagebox
import main
conn =pymysql.connect(user ="root",password= "")
cursor =conn.cursor()

class Settings():
    def change_password(self):
        win =Tk()
        win.title("CHANGE PASSWORD")
        try:
            cursor.execute("Use tabulationSystemKU")
            cursor.execute("Select password from login")
            old_password = cursor.fetchone()[0]
            print(old_password)
        except pymysql.Error as err:
            print(err)

        labelFrame = ttk.LabelFrame(win)

        old_password_variable = StringVar()
        new_password_variable = StringVar()
        re_enter_new_password_variable = StringVar()

        def save():
            if(new_password_variable.get() !=  re_enter_new_password_variable.get()):
                messagebox.showerror("ERROR","NEW PASSWORD MISMATCHED")
            elif old_password != old_password_variable.get():
                messagebox.showerror("ERROR","INCORRECT OLD PASSWORD")
            elif len(new_password_variable.get())<3:
                messagebox.showerror("ERROR","LENGTH OF THE PASSWORD SHOULD BE AT LEAST 3")
            else:
                try:
                    cursor.execute("UPDATE login SET password='{}' where username='{}'".format(

                        new_password_variable.get(),"admin"))
                    conn.commit()
                    messagebox.showinfo("SUCCESSFUL", "YOUR PASSWORD IS SUCCESSFULLY CHANGED")
                    win.destroy()
                    main.showMainPage()

                except pymysql.Error as err:
                    print(err)





        Label(labelFrame,text ="CURRENT PASSWORD : ").grid(row=0,column=0,padx=15,pady=5)
        Entry(labelFrame,textvariable =old_password_variable,show="*").grid(row=0,column=1,padx=15,pady=15)

        Label(labelFrame,text = "ENTER NEW PASSWORD : ").grid(row=1,column=0,padx=15,pady=15)
        Entry(labelFrame,textvariable=new_password_variable,show="*").grid(row=1,column=1,padx=15,pady=15)

        Label(labelFrame,text = "RE-ENTER NEW PASSWORD : ").grid(row=2,column=0,padx=15,pady=15)
        Entry(labelFrame,textvariable =re_enter_new_password_variable,show="*").grid(row=2,column=1,padx=15,pady=15)

        Button(labelFrame,text="DONE",command=save,background="khaki3",width=10).grid(row=3,column=1,pady=15,padx=15)


        labelFrame.pack()

        def doSomething():

            win.destroy()
            main.showMainPage()

        win.protocol('WM_DELETE_WINDOW', doSomething)
        win.mainloop()

