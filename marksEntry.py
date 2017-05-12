import tkinter as tk
from  tkinter import  ttk
from tkinter import *
import main
import pymysql
import caltulateResult

conn = pymysql.connect(user = "root",password = "")
cursor = conn.cursor()
class MarksEntry:
    flag = 1
    e = Entry
    entry = []
    def show(self):

        calculateMarks = caltulateResult.CalculateResult()
        #courseTuple = ()
        courseList = []

        try:
            cursor.execute("USE tabulationSystemKU")
            cursor.execute("select courseno from coursetable")
            courseTuple = cursor.fetchall()
            #print(courseTuple)

        except pymysql.Error as err:
            print(err)
        for i in courseTuple:
            for j in i:
                courseList.append(j)
        #batch_tuple = ()
        batch_list = []

        try:
            cursor.execute("USE tabulationSystemKU")
            cursor.execute("SELECT DISTINCT batch from students")
            batch_tuple = cursor.fetchall()
            print(batch_tuple)
        except pymysql.Error as err:
            print(err)


        for i in batch_tuple:
            for j in i:
                batch_list.append(j)

        color = 'khaki3'
        win = Tk()
        win.title('MARKS ENTRY')

        lblfrm1 = LabelFrame(win,text='Select General Data')


        session= StringVar()
        year = StringVar()
        term = StringVar()
        couseNo=StringVar()
        batch = StringVar()
        Label(lblfrm1,text='EXAM SESSION',padx=10,pady=10).grid(row=0,column=0)
        ttk.Combobox(lblfrm1,textvariable = session).grid(row=0,column=1)

        Label(lblfrm1,text='YEAR',padx=10,pady=10).grid(row=0,column=2)
        year_combobox= ttk.Combobox(lblfrm1,textvariable = year)
        year_combobox['values'] = ("First","Second","Third","Fourth","MS")
        year_combobox.grid(row=0,column=3)

        Label(lblfrm1,text='TERM',padx=10,pady=10).grid(row=0,column=4)
        term_combobox= ttk.Combobox(lblfrm1,textvariable = term)
        term_combobox['values'] = ("I","II","III","IV")
        term_combobox.grid(row=0,column=5)
        courseVariable = StringVar()

        Label(lblfrm1,text='COURSE NO',padx=10,pady=10).grid(row=0,column=6)
        courseno_tuple = ttk.Combobox(lblfrm1,textvariable =courseVariable)
        courseno_tuple['values']=tuple(courseList)
        Label(lblfrm1,padx=8).grid(row=0,column=8)

        '''Label(lblfrm1,text='COURSE TITLE',pady=10,padx=10).grid(row=1,column=0)
        Entry(lblfrm1,width=30).grid(row=1,column=1)

        Label(lblfrm1,text='CREDIT HOURS',pady=10,padx=10).grid(row=1,column=2)
        Entry(lblfrm1,width=15).grid(row=1,column=3)'''
        Label(lblfrm1,text = 'BATCH',pady= 10,padx=10).grid(row=1,column=0)
        batch_combobox = ttk.Combobox(lblfrm1,textvariable =batch)
        batch_combobox['values'] = tuple(batch_list)

        batch_combobox.grid(row =1,column=1)






        lblfrm2=LabelFrame(win)

        txta = StringVar()
        txtb = StringVar()
        txtc = StringVar()
        txtd = StringVar()
        txte = StringVar()
        txtf = StringVar()
        txtg = StringVar()
        txth = StringVar()
        txti = StringVar()




        '''f = Entry(lblfrm2,text=txtf,width=20)
        txtf.set('RETAKE')
        f.configure(background=color)
        f.grid(row=0,column=5)'''
        roll_variable = []
        attendance_variable = []
        class_test_variable = []
        sectionA_variable = []
        sectionB_variable = []



        for i in range(300):
            roll_variable.append(StringVar())
            attendance_variable.append(StringVar())
            class_test_variable.append(StringVar())
            sectionB_variable.append(StringVar())
            sectionA_variable.append(StringVar())
            self.entry.append(Entry)

        lblfrm3 = LabelFrame(win)
        canvas = Canvas(lblfrm2)
        frame = Frame(canvas)
        myscrollbar = Scrollbar(lblfrm2, orient="vertical", command=canvas.yview)

        canvas2 = Canvas(lblfrm2)
        frame2 = Frame(canvas2)
        myscrollbar2 = Scrollbar(lblfrm2, orient="vertical", command=canvas2.yview)

        def show_spread_sheet():
            self.flag = 1
            canvas2.pack_forget()
            frame2.pack_forget()
            myscrollbar2.pack_forget()

            a = Label(lblfrm3, textvariable=txta, width=17)
            txta.set('ROLL NO')
            a.configure(background=color, justify="center")
            a.grid(row=0, column=0)

            b = Label(lblfrm3, text='ATTENDANCE(10)', width=25)
            txtb.set(r'ATTENDANCE(10)')
            b.configure(background=color, justify="center")
            b.grid(row=0, column=1)

            c = Label(lblfrm3, text='CLASS TEST(30)', width=25)
            txtc.set(r'CLASS TEST(30)')
            c.configure(background=color, justify="center")
            c.grid(row=0, column=2)

            d = Label(lblfrm3, text='SECTION A(30)', width=25)
            txtd.set(r'SECTION A(30)')
            d.configure(background=color, justify="center")
            d.grid(row=0, column=3)

            self.e = Label(lblfrm3, text='SECTION B(30)', width=25)
            txte.set(r'SECTION B(30)')
            self.e.configure(background=color, justify="center")
            self.e.grid(row=0, column=4)



            def myfunction(event):
                canvas.configure(scrollregion=canvas.bbox("all"), width=835, height=500)



            canvas.configure(yscrollcommand=myscrollbar.set)

            myscrollbar.pack(side="right", fill="y")
            canvas.pack(side="left")
            canvas.create_window((0, 0), window=frame, anchor='nw')
            frame.bind("<Configure>", myfunction)


            for i in range(100):
                 #roll = ""
                 if(i<9):
                     roll_variable[i].set("0"+str(i+1))
                 else:
                     roll_variable[i].set(str(i+1))
                 Entry(frame, width=20,textvariable = roll_variable[i],justify = "center").grid(row=i+1, column=0)

                 Entry(frame,  width=30,textvariable = attendance_variable[i],justify = "center").grid(row=i+1, column=1)

                 Entry(frame, width=30,textvariable = class_test_variable[i],justify = "center").grid(row=i+1, column=2)

                 Entry(frame, width=30,textvariable = sectionA_variable[i],justify = "center").grid(row=i+1, column=3)

                 self.entry[i]=Entry(frame, width=30,textvariable = sectionB_variable[i],justify = "center")
                 self.entry[i].grid(row=i+1, column=4)
            print(self.entry)


                 #Entry(lblfrm2, width=20).grid(row=i+1, column=5)


        lblfrm4 = LabelFrame(win)
        def save_button_function_theory():
                self.flag = 0
                #lblfrm2.pack_forget()
                #lblfrm2.pack()
                #lblfrm2.pack_forget()
                canvas.pack_forget()
                frame.pack_forget()
                myscrollbar.pack_forget()




                a = Entry(lblfrm3, textvariable=txta, width=20)
                txta.set('ROLL NO')
                a.configure(background=color, justify="center")
                a.grid(row=0, column=0)

                b = Entry(lblfrm3, text=txtb, width=30)
                txtb.set(r'ATTENDANCE(10)')
                b.configure(background=color, justify="center")
                b.grid(row=0, column=1)

                c = Entry(lblfrm3, text=txtc, width=30)
                txtc.set(r'SESSIONAL ASSESSMENT (60)')
                c.configure(background=color, justify="center")
                c.grid(row=0, column=2)

                d = Entry(lblfrm3, text=txtd, width=30)
                txtd.set(r'VIVA (30)')
                d.configure(background=color, justify="center")
                d.grid(row=0, column=3)


                def myfunction(event):
                    canvas2.configure(scrollregion=canvas2.bbox("all"), width=655, height=500)



                canvas2.configure(yscrollcommand=myscrollbar2.set)

                myscrollbar2.pack(side="right", fill="y")
                canvas2.pack(side="left")
                canvas2.create_window((0, 0), window=frame2, anchor='nw')
                frame2.bind("<Configure>", myfunction)

                for i in range(100):
                    # roll = ""
                    if (i < 9):
                        roll_variable[i].set("0" + str(i + 1))
                    else:
                        roll_variable[i].set(str(i + 1))
                    Entry(frame2, width=20, textvariable=roll_variable[i], justify="center").grid(row=i + 1, column=0)

                    Entry(frame2, width=30, textvariable=attendance_variable[i], justify="center").grid(row=i + 1,
                                                                                                         column=1)

                    Entry(frame2, width=30, textvariable=class_test_variable[i], justify="center").grid(row=i + 1,
                                                                                                         column=2)

                    Entry(frame2, width=30, textvariable=sectionA_variable[i], justify="center").grid(row=i + 1,
                                                                                                       column=3)

                   # Entry(lblfrm2, width=0, textvariable=sectionB_variable[i], justify="center").delete(0,END)

                    # Entry(lblfrm2, width=20).grid(row=i+1, column=5)
                    self.entry[i].grid_forget()
                self.e.grid_forget()

        show_spread_sheet()

        def save_button_function_sessional(event):
            print(courseVariable.get()[len(courseVariable.get())-1])
            if courseVariable.get()[len(courseVariable.get())-1] not in "24690":
                save_button_function_theory()
                show_spread_sheet()
            else:
                print("theory call")
                save_button_function_theory()

        courseno_tuple.bind("<<ComboboxSelected>>",save_button_function_sessional)
        courseno_tuple.grid(row=0, column=7)
        try:
            cursor.execute('USE tabulationSystemKU')
            cursor.execute("SELECT disciplineCode from disciplineInfo")
            disciplineCode = cursor.fetchone()

        except pymysql.Error as err:
            print(err)


        def save():
         try:
           cursor.execute("SELECT DISTINCT courseNo,rollNo from registration WHERE retake = 1")
           retakeTuple2 = cursor.fetchall()
           print(retakeTuple2)
         except pymysql.Error as err:
             print(err)

         try:
            cursor.execute("USE tabulationSystemKU")
            if self.flag==1:
                for i in range(100):

                    if attendance_variable[i].get() and class_test_variable[i].get() and sectionA_variable[i].get() and session.get() and year.get() and term.get()\
                        and courseVariable.get() and batch.get() and sectionB_variable[i].get():

                            total_marks = int(attendance_variable[i].get())+int(class_test_variable[i].get())+\
                                     int(sectionA_variable[i].get())+int(sectionB_variable[i].get())

                            for j in retakeTuple2:
                                print(j[0],courseVariable.get())
                                if (j[0]==courseVariable.get() and batch.get()+disciplineCode[0]+roll_variable[i].get()==j[1]):

                                    total_marks-=5
                                    if(total_marks<40):
                                        total_marks = 40

                                    elif total_marks>=80:
                                        total_marks = 75
                                        print(total_marks)
                                    break
                                print(total_marks)
                            gpa_grade = calculateMarks.calculate(total_marks)
                            #print(gpa_grade[0],gpa_grade[1])

                            cursor.execute("INSERT INTO theory_result (session,year,term,courseNo,roll,attendance,ct,"
                                           "seca,secb,gpa,grade)"
                                           "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(session.get(),
                                                year.get(),term.get(),courseVariable.get(),
                                                    batch.get()+disciplineCode[0]+roll_variable[i].get()

                                                ,attendance_variable[i].get(),class_test_variable[i].get(),sectionA_variable[i].get(),
                                                sectionB_variable[i].get(),gpa_grade[0],gpa_grade[1]))
                            conn.commit()
                win.destroy()
                main.showMainPage()
            else:
                for i in range(100):

                    if attendance_variable[i].get() and class_test_variable[i].get() and sectionA_variable[i].get() and session.get() and year.get() and term.get()\
                        and courseVariable.get() and batch.get():

                            total_marks = int(attendance_variable[i].get())+int(class_test_variable[i].get())+\
                                     int(sectionA_variable[i].get())

                            for j in retakeTuple2:
                                print(j[0],courseVariable.get())
                                if (j[0]==courseVariable.get() and batch.get()+disciplineCode[0]+roll_variable[i].get()==j[1]):

                                    total_marks-=5
                                    if(total_marks<40):
                                        total_marks = 40

                                    elif total_marks>=80:
                                        total_marks = 75
                                        print(total_marks)
                                    break
                                print(total_marks)
                            gpa_grade = calculateMarks.calculate(total_marks)
                            #print(gpa_grade[0],gpa_grade[1])

                            cursor.execute("INSERT INTO sessional_result (session,year,term,courseNo,roll,attendance,"
                                           "sa,viva,gpa,grade)"
                                           "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(session.get(),
                                                year.get(),term.get(),courseVariable.get(),
                                                    batch.get()+disciplineCode[0]+roll_variable[i].get()

                                                ,attendance_variable[i].get(),class_test_variable[i].get(),sectionA_variable[i].get(),
                                               gpa_grade[0],gpa_grade[1]))
                            conn.commit()
                win.destroy()
                main.showMainPage()

         except pymysql.Error as err:
             print(err)



        Button(lblfrm1, text="SAVE MARKS",command= save, background="khaki3", padx=20).grid(row=1, column=3)
        lblfrm1.pack(pady=10, padx=10)



        lblfrm3.pack()
        lblfrm2.pack(pady=10)

        def doSomething():

            win.destroy()
            main.showMainPage()

        win.protocol('WM_DELETE_WINDOW', doSomething)

        win.state('zoomed')
        win.mainloop()