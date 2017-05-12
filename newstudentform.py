import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pymysql
import main
import main


conn = pymysql.connect(user='root',password="")
cursor = conn.cursor()
from functools import partial

class NewStudentForm():

    def disciplineCode(self):
        try:
            cursor.execute("USE tabulationSystemKU")
            cursor.execute("SELECT disciplineCode from disciplineinfo")
            data=  cursor.fetchone()[0]
            return data

        except pymysql.Error as err:
            print(err)

    def batchRead(self):
        try:
            cursor.execute("USE tabulationSystemKU")
            cursor.execute("SELECT DISTINCT (batch) from students")

            tpl = cursor.fetchall()
            return tpl
        except pymysql.Error as err:
            print(err)

    def show(self):


        win= tk.Tk()
        win.title("ADD STUDENTS")

        labelFrame=ttk.LabelFrame(win,text='Select General data')
        win.minsize(width=500,height=500)



        ttk.Label(labelFrame,text="Batch : ").grid(column=0,row=0,padx=5,pady=10)

        btch=tk.StringVar()

        cmbx=ttk.Combobox(labelFrame,width=20,textvariable=btch)
        NewStudentForm.batchRead(None)

        cmbx['values']=NewStudentForm.batchRead(None)
        cmbx.grid(column=1,row=0,pady=10,padx=5)

        #ttk.Label(labelFrame,text='Year : ').grid(column=0,row=1,padx=5,pady=10)

        cmbx2=ttk.Combobox(labelFrame,width=20)
        cmbx2['values']=('First','Second','Third','Fourth','MS')
        #cmbx2.grid(column=1,row=1,pady=10,padx=5)

        #ttk.Label(labelFrame,text='Term : ').grid(column=0,row=2,padx=5,pady=10)

        cmbx3=ttk.Combobox(labelFrame,width=20)
        cmbx3['values']=('I',"II","III",'IV')
        #cmbx3.grid(column=1,row=2,pady=10,padx=5)


        labelFrame.pack(pady=40)

        labelFrame2=ttk.LabelFrame(win)



        roll = StringVar()
        name = StringVar()



        labelFrame3 = LabelFrame(win)

        a =Entry(labelFrame3, textvariable=roll, width=20)
        a.insert(END,'              ROLL')
        a.configure(background='khaki3')

        b = Entry(labelFrame3,textvariable=name, width=80)
        b.insert(END,"                                                                        NAME")
        b.configure(background='khaki3')

        a.grid(row=0,column=0)
        b.grid(row=0,column=1)
        labelFrame3.pack()
        #a.pack(side =LEFT)
        #b.pack(side =RIGHT)

        l= list()
        rollNo= list()
        name =list()
        for i in range(200):
            l.append(StringVar())
            rollNo.append(StringVar())
            name.append((StringVar()))

        discipline=''

        conn=  pymysql.connect(user='root',password='')
        cursor=conn.cursor()

        try:
            cursor.execute("USE tabulationSystemKU")
            cursor.execute('SELECT disciplineCode from disciplineInfo WHERE ID="1"')

            discipline = cursor.fetchone()

        except pymysql.Error as err:
            print(err)
        n = StringVar()

        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=585, height=400)

        canvas =Canvas(labelFrame2)
        frame = Frame(canvas)
        myscrollbar = Scrollbar(labelFrame2, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right", fill="y")
        canvas.pack(side="left")

        canvas.create_window((0, 0), window=frame, anchor='nw')
        frame.bind("<Configure>", myfunction)


        for i in range(200):
            a=Entry(frame,width=20,textvariable=rollNo[i])

            b=Entry(frame,width=80,textvariable=name[i])

            if i<9:
                 rollNo[i].set('    \t 0'+str(i+1))#14'+str(discipline[0])+'0'+str(i+1))
            else:
                rollNo[i].set(' \t '+str(i+1))#14'+str(discipline[0])+str(i+1))

            a.grid(row=i+5,column=0)
            b.grid(row=i+5,column=1)


        def save():
            if len(btch.get())>2 or len(btch.get())==0 :
                messagebox.showinfo("INVALID INPUT","Please insert last two digits of batch")
            else:

                for i in range(200):
                    if name[i].get():

                        try:
                            cursor.execute('USE tabulationSystemKU')
                            cursor.execute("INSERT INTO students (rollNo,name,batch,tech,tecp)"
                                           "VALUES('{}','{}','{}','{}','{}')".format((str(btch.get())+
                                                                                      NewStudentForm.disciplineCode(None)+
                                                                                               str(rollNo[i].get()).strip()),name[i].get(),
                                                                                 btch.get(),0.0,0.0))

                            conn.commit()
                        except pymysql.Error as err:
                            print(err)
                win.destroy()
                main.showMainPage()

        Button(labelFrame,text='SAVE STUDENTS',command=save,background = "khaki3",padx=5).grid(row=3,column=1)
        labelFrame2.pack(padx=15)

        def doSomething():

            win.destroy()
            main.showMainPage()

        win.protocol('WM_DELETE_WINDOW', doSomething)


        win.state("zoomed")

        win.mainloop()

