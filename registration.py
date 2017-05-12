import tkinter as tk
from tkinter import ttk
from tkinter import *
import main
import pymysql
from functools import partial
from tkinter import messagebox

conn = pymysql.connect(user='root',password ="")
cursor = conn.cursor()
cursor.execute("USE tabulationSystemKU")
class Registration():


    counter = 0
    taken_courses = list()
    def show(self):

        def prerequisite(taken_courses,retakelist):
            #print(taken_courses)
           # print(retakelist)


            cannot_take=dict()
            for i in taken_courses:
                try:
                    cursor.execute("SELECT prerequisite from prerequisite_table where course='{}'".format(i.strip()))
                    prerequisite_subject = list(cursor.fetchall())
                    print(i)
                    print(prerequisite_subject)
                except pymysql.Error as err:
                    print(err)
                for j in prerequisite_subject:

                    if j[0] in retakelist:
                        cannot_take[i]=j[0]
            print(cannot_take)

            return cannot_take

        conn.commit()


        courseTuple = tuple()
        retakeTuple = tuple()
        yearTermTuple = tuple()
        coursenolist = list()
        coursetititlelist  =list()
        course_credit_list = list()
        batchno = tuple()
        rollNo=list()
        retakeVariable =list()

        try:
            cursor.execute("USE tabulationSystemKU")
            cursor.execute("SELECT DISTINCT courseNo,year,term,roll from sessional_result WHERE grade='F'")
            retakeTuple1 =cursor.fetchall()

            cursor.execute("SELECT DISTINCT courseNo,year,term,roll from sessional_result WHERE grade!='F'")
            passTuple1 = cursor.fetchall()

            cursor.execute("SELECT DISTINCT courseNo,year,term,roll from theory_result WHERE grade='F'")
            retakeTuple2=  cursor.fetchall()
           # print("retake")
           # print(retakeTuple2)

            cursor.execute("SELECT DISTINCT courseNo,year,term,roll from theory_result WHERE grade!='F'")
            passTuple2 = cursor.fetchall()

            passTuple =passTuple1+passTuple2

           # print("retake tuple ",retakeTuple)
           # print("pass tuple ", passTuple)

            retakeTuple = retakeTuple1+retakeTuple2

            finalRetakeList = []
            for i in retakeTuple:
                if i not in passTuple:
                    finalRetakeList.append(i)
            #print(finalRetakeList)
            retakeTuple = tuple(finalRetakeList)
            '''prerequite_test = list()
            def prerequisite_test_function():
                prerequite_test.clear()
                for i in finalRetakeList:
                    prerequite_test.append(i[0])'''


        except pymysql.Error as err:
            print(err)
        retakeSubjectList = list()
        try:
            cursor.execute("USE tabulationSystemKU")

            for i in retakeTuple:
                cursor.execute("SELECT coursetitle from courseTable where courseNo='{}'".format(i[0]))
                subject = cursor.fetchone()[0]
                if subject not in retakeSubjectList:
                    retakeSubjectList.append((i[0],subject,i[1],i[2],i[3]))

        except pymysql.Error as err:
            print(err)

        prerequite_test = list()
        prerequite_test = list()
        def prerequisite_test_function():
            prerequite_test.clear()
            for i in retakeSubjectList:
                prerequite_test.append(i[0])


        try:
            cursor.execute('USE tabulationSystemKU')
            cursor.execute('SELECT batch,year,term,session from courseconfiguration')

            cursor.execute('SELECT batch,year,term,session from courseconfiguration')
            batch_no_tpl=cursor.fetchone()

        except pymysql.Error as err:
            print(err)

        try:
            cursor.execute("USE tabulationSystemKU")
            cursor.execute("SELECT disciplineCode from disciplineInfo")
            dscplninfo=cursor.fetchone()
        except pymysql.Error as err:
            print(err)

        for i in range(1,101):
            if i<10:
                rollNo.append(batch_no_tpl[0]+dscplninfo[0]+'0'+str(i))
            else:
                rollNo.append(batch_no_tpl[0]+ dscplninfo[0]  + str(i))




        try:
            cursor.execute('USE tabulationSystemKU')
            cursor.execute('SELECT DISTINCT courseno,coursetitle,yearborsho,term from courseTable')
            courseTuple= cursor.fetchall()

        except pymysql.Error as err:
            print(err)

        try:
            cursor.execute("USE tabulationSystemKU")
            cursor.execute("SELECT year,term from courseConfiguration")
            yearTermTuple = cursor.fetchall()
           # print(yearTermTuple)
        except pymysql.Error as err:
            print(err)


        win = Tk()
        win.title("REGISTRATION")

        sessionVariable =StringVar()
        yearVariable =StringVar()
        termVariable = StringVar()
        rollVariable =StringVar()
        win.title('REGISTRATION')
        color = 'khaki3'
        lblfrm1=LabelFrame(win,pady=20,padx=15,text='Select General Data')
        Label(lblfrm1,text='YEAR',pady=10,padx=10).grid(row=0,column=0)
        yearCombobox = ttk.Combobox(lblfrm1,textvariable=yearVariable)
        yearCombobox['values'] = batch_no_tpl[1]
        yearCombobox.current(0)
        yearCombobox.configure(state='disable')
        yearCombobox.grid(row=0,column=1)

        Label(lblfrm1,text='TERM',pady=10,padx=10).grid(row=0,column=2)
        termComboBox =ttk.Combobox(lblfrm1,textvariable=termVariable)
        termComboBox['values']=batch_no_tpl[2]

        termComboBox.current(0)
        termComboBox.configure(state='disable')
        termComboBox.grid(row=0, column=3)

        Label(lblfrm1,text='SESSION',pady=10,padx=10).grid(row=0,column=4)
        sessionComboBox=  ttk.Combobox(lblfrm1,textvariable=sessionVariable)
        sessionComboBox['values'] = batch_no_tpl[3]
        sessionComboBox.current(0)
        sessionComboBox.configure(state='disable')
        sessionComboBox.grid(row=0,column=5)



        Label(lblfrm1,text='ROLL NO',pady=10,padx=10).grid(row=0,column=6)
        comboboxroll = ttk.Combobox(lblfrm1,textvariable=rollVariable,height=20)
        comboboxroll['values']=  tuple(rollNo)
        comboboxroll.current(0)
        comboboxroll.grid(row=0,column=7)
        #comboboxroll.bind("<<ComboboxSelected>>", comboTest )
        lblfrm1.pack(pady=10)

        lblfrm2 = LabelFrame(win,pady=20,padx=10)
        txta = StringVar()
        txtb = StringVar()
        txtc = StringVar()
        txtd =  StringVar()

        a =Entry(lblfrm2,textvariable=txta,width=20)
        txta.set('        COURSE NO')
        a.configure(background=color)
        a.grid(row=0,column=0)

        b = Entry(lblfrm2,textvariable=txtb,width=100)
        txtb.set('\t\t\t\t\t  COURSE TITLE')
        b.configure(background=color)
        b.grid(row=0,column=1)

        c = Entry(lblfrm2,textvariable=txtc,width=20)
        txtc.set('       CREDIT HOURS')
        c.configure(background=color)
        c.grid(row=0,column=2)

        d = Entry(lblfrm2,textvariable=txtd,width=10)
        txtd.set('  RETAKE')
        d.configure(background=color)
        d.grid(row=0,column=3)

        for i in range(22):
            coursenolist.append(StringVar())
            coursetititlelist.append(StringVar())
            course_credit_list.append(DoubleVar())
            retakeVariable.append(StringVar())
            Entry(lblfrm2,width=20,textvariable=coursenolist[i],justify ='center').grid(row=i+1,column=0)
            Entry(lblfrm2,width=100,textvariable=coursetititlelist[i],justify ='center').grid(row=i+1,column=1)
            Entry(lblfrm2,width=20,textvariable=course_credit_list[i],justify ='center').grid(row=i+1,column=2)
            Entry(lblfrm2,width=10,justify ='center',textvariable = retakeVariable[i]).grid(row=i+1,column=3)
        retake_variable =1
        def save():
            counter =0
            taken =list()
            for i in self.taken_courses:
                taken.append(i)
            print("retakeSuubjectList")
            print(retakeSubjectList)
            temp = list()
            for i in retakeSubjectList:
                if(i[4]==rollVariable.get()):
                    temp.append(i[0])
            print(taken,temp)
            prerequisite_dict = prerequisite(taken,temp)

            if(prerequisite_dict):
                print("PREREQUISITE")
                print(prerequisite_dict)
                text="  PREREQUISITE LIST\n"
                for i in prerequisite_dict:
                    text +=str(i)+ " "+prerequisite_dict[i]+"\n"
                messagebox.showerror("PREREQUISITE ERROR",text)
               # prerequisite_dict.clear()
                #taken.clear()
               # prerequite_test.clear()
                prerequisite_test_function()

            else:

                totalCredit=0.0
                try:
                    cursor.execute("USE tabulationSystemKU")
                    for i in range(22):
                        if(retakeVariable[i].get()):
                            self.retakeValue=1
                        else:
                            self.retakeValue=0
                        if coursenolist[i].get() and coursetititlelist[i].get() :
                            counter+=1

                            cursor.execute("INSERT INTO registration (rollNo,courseNo,year,term,es,retake)"
                                       "VALUES ('{}','{}','{}','{}','{}','{}')".format(rollVariable.get(),
                                        coursenolist[i].get(),yearVariable.get(),termVariable.get(),
                                        sessionVariable.get(),self.retakeValue))
                            totalCredit+=course_credit_list[i].get()
                    if totalCredit<=25.00:
                            #print(retakeValue,retakeVariable[i].get())
                        print(totalCredit)
                        self.taken_courses.clear()
                        conn.commit()
                        if(counter):
                            messagebox.showinfo("SUCCESSFUL","COURSE REGISTRATION SUCCESSFULLY COMPLETED")
                        win.destroy()
                        main.showMainPage()

                    else:
                        messagebox.showerror("CREDIT LIMIT CROSSED","YOU CAN REGISTER FOR AT MOST 25.00 CREDITS HOURS")
                        print(totalCredit)
                except pymysql.Error as err:
                    print(err)



        Button(lblfrm2,text='SAVE',background='khaki3',command = save,width=8,pady=5).grid(row=24,column=3)
        lblfrm3 = LabelFrame(win)

        labelFrame4 = LabelFrame(lblfrm3)
        Label(labelFrame4,text='OFFERED COURSES').pack()

        scrollbar = Scrollbar(labelFrame4)
        scrollbar.pack(side=RIGHT, fill=Y)

        listbox = Listbox(labelFrame4, yscrollcommand=scrollbar.set,width=60,height=20)

        def doubleClickTest(event):
            prerequisite_test_function()

            print("done")
            text=listbox.get(ACTIVE)
            #self.counter

            course_no_substring = ""
            course_title_substring = ""
            for j in range(len(text)):
                if text[j]==' ' and text[j+1]==' ' and text[j+2]==' ':
                    course_no_substring=  text[:j]
                    course_title_substring = text[j:]
            if(course_no_substring not in self.taken_courses):
                    try:
                        cursor.execute("USE tabulationSystemKU")
                        cursor.execute("SELECT credit from courseTable WHERE courseno ='{}'".format(course_no_substring.strip()))
                        course_credit_list[self.counter].set(cursor.fetchone()[0])

                    except pymysql.Error as err:
                        print(err)
                    coursenolist[self.counter].set(course_no_substring.strip())
                    coursetititlelist[self.counter].set(course_title_substring.strip())
                    self.counter+=1
                    self.taken_courses.append(course_no_substring)


        for i in courseTuple:
            #print(yearTermTuple,courseTuple)
            if i[2]==yearTermTuple[0][0] and i[3]==yearTermTuple[0][1]:
                listbox.insert(END, "  "+i[0]+"        "+i[1])
        listbox.bind('<Double-1>',partial(doubleClickTest))
        listbox.pack(side=LEFT, fill=BOTH)

        scrollbar.config(command=listbox.yview)


        labelFrame4.pack()

        labelFrame5 = LabelFrame(lblfrm3)

        Label(labelFrame5, text='RETAKES').pack()

        scrollbar2 = Scrollbar(labelFrame5)
        scrollbar2.pack(side=RIGHT, fill=Y)


        listbox2 = Listbox(labelFrame5, yscrollcommand=scrollbar2.set,width=60,height=10)
        for i in retakeSubjectList:
            #print(rollVariable.get(),i[4])
            if i[1]!=yearTermTuple[0][0] and i[2]!=yearTermTuple[0][1] and i[4]==rollVariable.get():
                listbox2.insert(END, i[0]+ "   "+i[1])

        def fillRetakeList(event):
            prerequisite_test_function()
            listbox2.delete(0,END)

            for i in retakeSubjectList:
                print(i[2],yearTermTuple[0][0],i[3],yearTermTuple[0][1],i[4],rollVariable.get())
                if i[4]==rollVariable.get():#i[2] != yearTermTuple[0][0] and i[3] != yearTermTuple[0][1] and i[4] == rollVariable.get().strip():
                    listbox2.insert(END, i[0] + "   " + i[1])
            self.taken_courses.clear()

            try:
                self.counter=0
                prerequisite_test_function()
                for i in range(100):
                    retakeVariable[i].set("")
                    coursenolist[i].set("")
                    coursetititlelist[i].set("")
                    course_credit_list[i].set(0.0)
            except:
                pass




        def test(event):
            print("done test")
            text = listbox2.get(ACTIVE)
            # self.counter

            course_no_substring = ""
            course_title_substring = ""
            for j in range(len(text)):
                if text[j] == ' ' and text[j + 1] == ' ' and text[j + 2] == ' ':
                    course_no_substring = text[:j]
                    course_title_substring = text[j:]

            if(course_no_substring not in self.taken_courses):
                try:
                    cursor.execute("USE tabulationSystemKU")
                    cursor.execute(
                        "SELECT credit from courseTable WHERE courseno ='{}'".format(course_no_substring.strip()))
                    course_credit_list[self.counter].set(cursor.fetchone()[0])

                except pymysql.Error as err:
                    print(err)
                coursenolist[self.counter].set(course_no_substring.strip())
                coursetititlelist[self.counter].set(course_title_substring.strip())
                retakeVariable[self.counter].set("YES")
                self.counter += 1

                self.taken_courses.append(course_no_substring)


        comboboxroll.bind("<<ComboboxSelected>>", fillRetakeList )
        listbox2.bind('<Double-1>',partial(test))
        listbox2.pack(side=LEFT, fill=BOTH)

        scrollbar2.config(command=listbox2.yview)



        labelFrame5.pack()



        lblfrm2.pack(side = tk.LEFT)

        lblfrm3.pack(side = tk.RIGHT,padx=10)
        def doSomething():

            win.destroy()
            main.showMainPage()

        win.protocol('WM_DELETE_WINDOW', doSomething)
        win.state('zoomed')
        win.resizable(False,False)
        win.mainloop()