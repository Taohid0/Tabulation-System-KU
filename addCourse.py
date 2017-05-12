import tkinter as tk
from tkinter import ttk
from tkinter import *
import pymysql
conn = pymysql.connect(user='root', password="")
cursor = conn.cursor()
import main



class AddCourse():

    def on_closing(self):
        main.showMainPage()

    color='khaki3'
    def show(self):
        win = tk.Tk()
        win.title("ADD COURSES")
        year1=StringVar()
        term=StringVar()

        labelFrame=ttk.LabelFrame(win,text='Select General data')

        ttk.Label(labelFrame,text='Year').grid(column=0,row=0,pady=10,padx=10)
        cmbx1=ttk.Combobox(labelFrame,textvariable=year1)
        cmbx1['values']=('First','Second','Third','Fourth')
        cmbx1.grid(column=1,row=0,pady=10,padx=10)

        ttk.Label(labelFrame,text='Term').grid(row=1,column=0,pady=10,padx=10)
        cmbx2=ttk.Combobox(labelFrame,textvariable=term)
        cmbx2['values']=('I','II','III','IV')
        cmbx2.grid(row=1,column=1,pady=10,padx=10)

        labelFrame.pack(pady=25)

        labelFrame2=ttk.LabelFrame(win)

        #ttk.Label(labelFrame2,text='SERIAL NO').grid(row=0,column=0)
        #ttk.Label(labelFrame2,text='COURSE NO').grid(row=0,column=1)
        #ttk.Label(labelFrame2,text='COURSE TITLE').grid(row=0,column=2)
        #ttk.Label(labelFrame2,text='CH').grid(row=0,column=3)
        #ttk.Label(labelFrame2,text='STATUS').grid(row=0,column=4)
        txta = tk.StringVar()
        txtb = tk.StringVar()
        txtc = tk.StringVar()
        txtd = tk.StringVar()


        a = Entry(labelFrame2,width=15,background = 'khaki3',textvariable =txta)
        txta.set('SERIAL NO')
        a.configure(background = 'khaki3')
        a.grid(row=0,column=0)

        b = Entry(labelFrame2,width=20,background= 'khaki3',textvariable=txtb)
        txtb.set('COURSE NO')
        b.configure(background='khaki3')
        b.grid(row=0,column=1)

        c = Entry(labelFrame2,width=80,background='khaki3',textvariable=txtc)
        txtc.set('COURSE TITLE')
        c.configure(background= 'khaki3')
        c.grid(row=0,column=2)

        d = Entry(labelFrame2,width=15,background='khaki3',textvariable=txtd)
        txtd.set('CREDIT HOURS')
        d.configure(background='khaki3')
        d.grid(row=0,column=3)

        l = list()
        crseNo=list()
        crseTitle=list()
        creditHrs=list()
        status=list()

        for i in range(25):
            l.append(tk.StringVar())
            crseNo.append(StringVar())
            crseTitle.append(StringVar())
            creditHrs.append(DoubleVar())
            status.append(StringVar())


        for i in range(1,21):
            a= ttk.Entry(labelFrame2,width=15,textvariable=l[i])
            l[i].set("             "+str(i))
            a.grid(row=i,column=0)

            ttk.Entry(labelFrame2,width=20,textvariable=crseNo[i-1]).grid(row=i,column=1)
            ttk.Entry(labelFrame2,width=80,textvariable=crseTitle[i-1]).grid(row=i,column=2)
            ttk.Entry(labelFrame2,width=15,textvariable=creditHrs[i-1]).grid(row=i,column=3)
            #ttk.Entry(labelFrame2,width=15,textvariable=status[i-1]).grid(row=i,column=4)



        def save():

            cursor.execute('USE tabulationSystemKu')
            for i in range(21):


                if year1.get() and term.get() and crseNo[i].get():
                    cursor.execute("INSERT INTO coursetable (yearborsho,term,courseno,coursetitle,credit)"
                                   "VALUES ('{}','{}','{}','{}',{})".format(year1.get(),term.get(),crseNo[i].get().strip()
                                                                            ,crseTitle[i].get().strip(),creditHrs[i].get()))

            conn.commit()
            win.destroy()
            main.showMainPage()
        Button(labelFrame2,text='SAVE',background='khaki3',width=10,command=save).grid(row=22,column=3,pady=5)


        labelFrame2.pack()

        win.state('zoomed')
        def doSomething():

            win.destroy()
            main.showMainPage()

        win.protocol('WM_DELETE_WINDOW', doSomething)



        win.mainloop()