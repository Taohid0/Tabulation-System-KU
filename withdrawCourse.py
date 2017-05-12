from tkinter import *
import pymysql
from Info import *
from tkinter import ttk
from tkinter import messagebox
import main

conn = pymysql.connect(user="root",password="")
cursor = conn.cursor()
cursor.execute("USE tabulationSystemKU")

class WithdrawCoures():
    def show(self):

        win = Tk()
        rollVariable = StringVar()
        batch_variable = StringVar()
        year_variable = StringVar()
        term_variable = StringVar()
        session_variable = StringVar()
        win.title("WITHDRAW COURSES")
        labelframe1 = LabelFrame(win)

        Label(labelframe1,text="BATCH : ").grid(row=0,column=0,padx=15,pady=15)
        info_object= Info()
        batch_list= info_object.get_batch()
        batch_comobobox = ttk.Combobox(labelframe1,textvariable = batch_variable)
        batch_comobobox["values"] = tuple(batch_list)
        batch_comobobox.grid(row=0,column=1,padx=15,pady=15)

        Label(labelframe1,text="ROLL : ").grid(row=0,column=2,padx=1,pady=15)
        roll_list = list()
        for i in range(200):
            roll_list.append(i+1)

        roll_combobox = ttk.Combobox(labelframe1,textvariable =rollVariable)
        roll_combobox["values"] = tuple(roll_list)
        roll_combobox.grid(row=0,column=3)

        Label(labelframe1,text="YEAR : ").grid(row=1,column=0,pady=15,padx=15)
        year_combobox = ttk.Combobox(labelframe1,textvariable =year_variable)
        year_combobox["values"] =("First","Second","Third","Fourth","Fifth")
        year_combobox.grid(row=1,column=1,padx= 15,pady=15)

        Label(labelframe1,text="TERM : ").grid(row=1,column=2,padx=15,pady=15)
        term_comobox= ttk.Combobox(labelframe1,textvariable = term_variable)
        term_comobox["values"]= ("I","II","III","IV","V")
        term_comobox.grid(row=1,column=3,padx= 15,pady=15)

        Label(labelframe1, text="SESSION : ").grid(row=0, column=4, padx=15, pady=15)
        session_comobox = ttk.Combobox(labelframe1,textvariable = session_variable)
        session_comobox["values"] = tuple(info_object.get_session())
        session_comobox.grid(row=0, column=5,padx= 15,pady=15)

        course_no_list = list()
        course_title_list = list()
        status_list = list()
        checkButton = list()

        for i in range(50):
            course_title_list.append(StringVar())
            course_no_list.append(StringVar())
            status_list.append(StringVar())
            checkButton.append((IntVar()))
        labelframe2 = LabelFrame(win)
        labelframe3 = LabelFrame(win)

        def withdraw():
            withdraw_list = list()
            counter = 0
            for i in range(len(checkButton)):
                if checkButton[i].get()==1:
                    withdraw_list.append(course_no_list[i].get())
                    counter+=1
            try:
                for j in withdraw_list:
                    cursor.execute("DELETE FROM registration WHERE courseNo='{}'".format(j))
            except pymysql.Error as err:
                print(err)
            conn.commit()
            messagebox.showinfo("SUCCESSFULL","SUCCESSFULLY WITHDRAWN "+str(counter)+" COURSES")
            print(withdraw_list)
            win.destroy()
            main.showMainPage()


        Button(labelframe1,text="WITHDRAW",command=withdraw,background="khaki3",padx=5).grid(row=1,column=5)
        entry1=list()
        entry2 = list()
        checkbox=list()

        def show_labelFrame2(event):

            for i in range(50):
                course_title_list[i].set("")
                course_no_list[i].set("")
                status_list[i].set("")

            labelframe2.pack_forget()
            labelframe3.pack_forget()

            if(batch_variable.get() and rollVariable.get() and year_variable.get() and term_variable.get()
               and session_variable.get()):
                if (len(str(rollVariable.get()))<2):
                    r = '0'+str(rollVariable.get())
                else :
                    r = str(rollVariable.get())
                student_id = str(batch_variable.get())+str(info_object.discipline_code())+r
                year = year_variable.get()
                term = term_variable.get()
                session = session_variable.get()
                Label(labelframe3,text = "COURSE NO",padx=30,background="khaki3").grid(row=0,column=0)
                Label(labelframe3,text="COURSE TTTLE",padx=245,background="khaki3").grid(row=0,column=1)
                Label(labelframe3,text= "REMOVE ?",padx=5,background="khaki3").grid(row=0,column=2)
                labelframe3.pack()

                try:
                    cursor.execute("SELECT courseNo from registration where rollNo='{}' and year='{}' and term='{}'"
                                   "and es='{}' ".format(student_id,year,term,session))
                    courses = cursor.fetchall()
                except pymysql.Error as err:
                    print(err)
                counter=0
                for i in courses:
                        course_no_list[counter].set(i[0])
                        counter+=1
                #print(counter)
                counter=0
                for i in course_no_list:
                    if i.get():
                        try:
                            cursor.execute("Select courseTitle from courseTable where courseNo='{}'".format(i.get()))
                            title = cursor.fetchone()[0]
                            course_title_list[counter].set(title)
                            counter+=1
                        except pymysql.Error as err:
                            print(err)
                print(counter)
                for i in range(counter):

                    Entry(labelframe2,textvariable = course_no_list[i],justify="center",width=25).grid(row=i,column=0)
                    Entry(labelframe2,textvariable =course_title_list[i],justify="center",width=80).grid(row=i,column=1)
                    Checkbutton(labelframe2,text="",variable=checkButton[i]).grid(row=i,column=2)
                    print(checkButton[i].get())

                labelframe3.pack()
                labelframe2.pack(padx=15,pady=15)

        batch_comobobox.bind("<<ComboboxSelected>>",show_labelFrame2)
        roll_combobox.bind("<<ComboboxSelected>>",show_labelFrame2)
        year_combobox.bind("<<ComboboxSelected>>",show_labelFrame2)
        term_comobox.bind("<<ComboboxSelected>>",show_labelFrame2)
        session_comobox.bind("<<ComboboxSelected>>",show_labelFrame2)




        labelframe1.pack(pady=15,padx=15)
        win.state("zoomed")
        def doSomething():
            win.destroy()
            main.showMainPage()

        win.protocol('WM_DELETE_WINDOW', doSomething)
        win.mainloop()


