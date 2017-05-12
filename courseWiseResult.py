from tkinter import *
import pymysql
from tkinter import ttk
from functools import partial
import tkinter as tk
from tkinter import messagebox

conn = pymysql.connect(user = "root",password = "")
cursor = conn.cursor()
cursor.execute("Use tabulationSystemKU")
#conn.commit()
import main
class CourseWiseResult():
    win = None
    def show_result(self,year,term,batch,session,course):

        if(not year.get() or not term.get() or not batch.get() or not session.get() or not course.get()):
            messagebox.showwarning("ERROR","PLEASE FILL UP ALL THE FIELDS CORRECTLY")

        else:

                global win
                win.destroy()

                win2 = Tk()
                win2.title("COURSE WISE RESULT")


                try:
                    cursor.execute("Select DISTINCT courseTitle from courseTable where courseNo='{}'".format(course.get()))
                except pymysql.Error as err:
                    print("Course")

                course_title =cursor.fetchone()
                if(course_title is None):
                    course_title="No course is selected"
                else:
                    course_title = course_title[0]

                lblfrm1 = LabelFrame(win2)
                Label(lblfrm1,text="RESULT FOR COURSE "+str(course.get()),font=("",15)).pack(pady=10)
                Label(lblfrm1,text = course_title,font=("",15)).pack(pady=10)
                text = "YEAR : "+str(year.get())+"\t "+"TERM : "+str(term.get())+" \tSESSION : "+str(session.get())
                Label(lblfrm1,text=text,font=("",15)).pack(pady=10,padx=10)
                lblfrm1.pack(pady=10)

                lblfrm2 = LabelFrame(win2)
                length = len(course.get())
                if(course.get()[length-1] in "13579"):
                    try:
                        cursor.execute("Select roll,grade from theory_result where year='{}' AND term='{}' AND session='{}'".format(
                            year.get(),term.get(),session.get()
                        ))
                        result =cursor.fetchall()
                    except pymysql.Error as err:
                         print(err)
                else:
                    try:
                        cursor.execute("Select roll,grade from sessional_result where year='{}' AND term='{}',session='{}'".format(
                            year.get(), term.get(), session.get()
                        ))
                        result = cursor.fetchall()
                    except pymysql.Error as err:
                        print(err)

                print(result)
                counter = 0
                canvas = Canvas(lblfrm2)
                frame = Frame(canvas)

                for i in result:
                    roll_variable = StringVar()
                    grade_variable = StringVar()
                    counter_variable = IntVar()
                    roll_variable.set(i[0])
                    grade_variable.set(i[1])
                    counter_variable.set(counter+1)
                    Entry(frame,text=counter_variable,justify="center",width=10).grid(row=counter,column=0)
                    Entry(frame,text =roll_variable,justify="center",width=40).grid(row=counter,column=1)
                    Entry(frame,text=grade_variable,justify="center",width=40).grid(row =counter,column=2)
                    counter=counter+1
                lblfrm2.pack()

                #number of individual grades have to be calculated
                myscrollbar = Scrollbar(lblfrm2,orient ="vertical",command =canvas.yview)
                canvas.configure(yscrollcommand=myscrollbar.set)
                myscrollbar.pack(side = "right",fill="y")
                canvas.pack(side="left")


                def myfunction(event):
                    canvas.configure(scrollregion=canvas.bbox("all"), width=550, height=400)

                canvas.create_window((0, 0), window=frame, anchor="nw")
                frame.bind("<Configure>",myfunction)

                win2.state("zoomed")

                def doSomething():

                    win2.destroy()
                    main.showMainPage()

                win2.protocol('WM_DELETE_WINDOW', doSomething)
                win2.mainloop()

    def get_term_data(self):
        global win
        win = Tk()
        win.title("SHOW RESULT CONFIGURATION")
        year = StringVar()
        term = StringVar()
        session = StringVar()
        batch = StringVar()
        course = StringVar()



        year_tuple = ("First","Second","Third","Fourth")
        term_tuple = ("I","II","III","IV")
        try:
            cursor.execute("Select DISTINCT es from registration")
        except pymysql.Error as err:
            print(err)

        session_list= list(cursor.fetchall())

        try:
            cursor.execute("Select DISTINCT session from sessional_result")
        except pymysql.Error as err:
            print(err)

        session_list2 =cursor.fetchall()
        print(session_list2)

        try:
            cursor.execute("Select DISTINCT session from theory_result")
        except pymysql.Error as err:
            print(err)

        session_list3= cursor.fetchall()

        for i in session_list2:
            if i not in session_list:
                session_list.append(i)

        for i in session_list3:
            if i not in session_list:
                session_list.append(i)


        session_tuple = tuple(session_list)
        try:
            cursor.execute("Select DISTINCT LEFT(rollNo,2) from registration")
        except pymysql.Error as err:
            print(err)
        batch_list = cursor.fetchall()
        batch_tuple = tuple(batch_list)

        try:
            cursor.execute("Select courseNo from courseTable")
        except pymysql.Error as err:
            print(err)


        temp = cursor.fetchall()
        courseNo_list = list()
        for i in temp:
            for j in i:
                courseNo_list.append(j)

        courseNo_tuple = tuple(courseNo_list)

        lblfrm =ttk.LabelFrame(win,text = "PLEASE FILL UP ALL THE FIELDS")
        Label(lblfrm,text ="YEAR : ",pady=15,padx=10).grid(row=0,column=0)
        year_combobox = ttk.Combobox(lblfrm,textvariable =year)
        year_combobox["values"] =year_tuple
        year_combobox.grid(row =0,column=1,pady=15,padx=10)

        Label(lblfrm,text = "TERM : ",pady=15,padx=10).grid(row=1,column=0)
        term_combobox = ttk.Combobox(lblfrm,textvariable =term)
        term_combobox["values"] =term_tuple
        term_combobox.grid(row=1,column=1,pady=15,padx=10)

        Label(lblfrm,text ="SESSION : ",padx=10,pady=15).grid(row=2,column=0)
        session_combobox = ttk.Combobox(lblfrm,textvariable = session)
        session_combobox["values"] =session_tuple
        session_combobox.grid(row=2,column=1,pady=15,padx=10)

        Label(lblfrm,text="COURSE : ",padx=10,pady=15).grid(row=4,column=0)
        course_combobox = ttk.Combobox(lblfrm,textvariable =course)
        course_combobox["values"] = courseNo_tuple
        course_combobox.grid(row=4,column=1,pady=15,padx=10)

        Label(lblfrm,text = "BATCH : ",padx = 10,pady=15).grid(row=3,column=0)
        batch_combobox = ttk.Combobox(lblfrm,textvariable = batch)
        batch_combobox["values"] = batch_tuple
        batch_combobox.grid(row=3,column=1,padx=10,pady=15)



        save_button = Button(lblfrm,text="SHOW RESULT",background ="khaki3",
                             command= partial(self.show_result,year,term,batch,session,course))
        save_button.grid(row=5,column=1,padx=10,pady=15)
        lblfrm.pack(pady=60,padx=80)

        def doSomething():

            win.destroy()
            main.showMainPage()

        win.protocol('WM_DELETE_WINDOW', doSomething)
        win.mainloop()

#objectCourse = CourseWiseResult()
#objectCourse.get_term_data()