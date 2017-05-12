from tkinter import  *
from tkinter import ttk
import tkinter as tk
import pymysql
from functools import partial
import main
import  registration

conn = pymysql.connect(user='root',password="")
cursor = conn.cursor()

class RegistrationConfiguratinClass():




    def show(self):

        win = Tk()
        win.title("REGISTRATION CONFIGURATION")
        year=tk.StringVar()
        term = tk.StringVar()
        session = tk.StringVar()
        creditLimit = tk.DoubleVar()

        labelFrame1 = LabelFrame(win,pady=20,padx=20)

        win.title("Configure Registration")

        Label(labelFrame1,text='YEAR',pady=10,padx=10).grid(row=0,column=0)
        combobox1 = ttk.Combobox(labelFrame1,textvariable = year)
        combobox1['values']= ("First","Second","Third","Fourth")
        combobox1.grid(row=0,column=1,pady=10,padx=10)

        Label(labelFrame1,text='SESSION',pady=10,padx=10).grid(row=0,column=2)
        entry = ttk.Entry(labelFrame1,textvariable = session)
        entry.grid(row=0,column=3,pady=10,padx=10)

        Label(labelFrame1,text='TERM',pady=10, padx=10).grid(row=1,column=0)
        combobox3 = ttk.Combobox(labelFrame1,textvariable = term)
        combobox3['values'] = ("I","II","III","IV")
        combobox3.grid(row=1,column=1,pady=10,padx=10)

        Label(labelFrame1,text = 'CREDIT LIMIT').grid(row=1,column=2)
        entry2 = ttk.Entry(labelFrame1,textvariable =creditLimit)
        creditLimit.set(25.00)

        entry2.grid(row=1,column=3,pady=10, padx=10)
        bathcVariable =tk.StringVar()
        Label(labelFrame1, text='BATCH', pady=10, padx=10).grid(row=2, column=0)
        entry = ttk.Entry(labelFrame1, textvariable=bathcVariable,width=23)
        entry.grid(row=2, column=1, pady=10, padx=10)

        labelFrame1.pack(anchor='center',pady=20,padx=20)


        win.minsize(width=40,height=300)

        win.resizable(False,False)


        def save():

            try:
                cursor.execute("USE tabulationSystemKU")
                cursor.execute("DELETE FROM courseConfiguration")
                cursor.execute("INSERT INTO courseConfiguration (year,term,session,creditLimit,batch)"
                               "VALUES ('{}','{}','{}','{}','{}')".format(year.get(), term.get(), session.get(),
                                                                          creditLimit.get(),bathcVariable.get()))

                conn.commit()

                win.destroy()
                main.showMainPage()
            except pymysql.Error as err:
                print(err)


        #func = partial(save,year.get(), term.get(), session.get(), creditLimit.get())
        Button(win,text='SAVE',width=15,background='khaki3',command = save).pack(side = RIGHT,padx=20)

        def doSomething():
            win.destroy()
            main.showMainPage()

        win.protocol('WM_DELETE_WINDOW', doSomething)


        win.mainloop()
