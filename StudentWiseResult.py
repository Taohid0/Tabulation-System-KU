from tkinter import *
import  pymysql
from tkinter import  ttk
import Info
from functools import partial
from tkinter import messagebox
conn = pymysql.connect(user = "root",password ="")
cursor =conn.cursor()
cursor.execute("Use tabulationSystemKU")
import main
class StudentWiseResult():
    win =None

    def show_result(self,roll,year,term,batch):

        if (not roll.get() or not year.get() or not term.get() or not batch.get()):
            messagebox.showwarning("ERROR", "PLEASE FILL UP ALL THE FIELDS CORRECTLY")
        else:
            global win
            win.destroy()
            win2 = Tk()
            win2.title("STUDENT WISE RESULT")

            if(len(roll.get())<2):
                r="0"+roll.get()
                roll=StringVar()
                roll.set(r)
            if(len(batch.get())<2):
                b = "0"+batch.get()
                batch = StringVar()
                batch.set(b)

            print(roll.get())
            print(batch.get())
            print(year.get())
            print(term.get())


            try:
                cursor.execute("Select disciplineCode from disciplineInfo")
                discipline_code = cursor.fetchone()[0]
                print(discipline_code)
            except pymysql.Error as err:
                print(err)

            student_id= str(batch.get())+str(discipline_code)+str(roll.get())
            print(student_id)


            try:

                cursor.execute(
                    "Select courseNo,grade,gpa from theory_result where year='{}' AND term='{}' AND roll='{}'".format(
                        year.get(),term.get(),student_id
                    ))
                theory_result =list(cursor.fetchall())

            except pymysql.Error as err:
                print(err)

            try:
                cursor.execute(
                    "Select courseNo,grade,gpa from sessional_result where year='{}' AND term='{}' AND roll='{}'".format(
                        year.get(), term.get(), student_id
                    ))
                sessional_result = list(cursor.fetchall())

            except pymysql.Error as err:
                print(err)

            result = theory_result+sessional_result

            total_gpa=0.0
            total_credit=0.0
            total_fail=0
            passed_credit=0.0

            for i in result:
                if(i[1]!="F"):
                    try:
                        cursor.execute("Select credit from courseTable where courseNo='{}'".format(i[0]))
                        credit=cursor.fetchone()[0]
                        total_gpa+=credit*i[2]
                        total_credit+=credit
                    except pymysql.Error as err:
                        print(err)
                else:
                    total_fail+=1

            lblfrm3 = LabelFrame(win2)
            gpa =total_gpa/total_credit
            Label(lblfrm3,text="TOTAL COURSES : "+ str(len(result)),font=("",15)).pack(padx=30)
            if(total_fail>0):
                Label(lblfrm3,text="RETAKES : "+str(total_fail),font=("",15)).pack()
            Label(lblfrm3,text = "TERM GPA : "+str('{0:.2f}'.format(gpa)),font=("",15)).pack()

            lblfrm1 = LabelFrame(win2)
            Label(lblfrm1, text="RESULT FOR STUDENT ID " + str(student_id),font=("",15)).pack(pady=10)
            text = "YEAR : " + str(year.get()) + "\t " + "TERM : " + str(term.get())# + " \tSESSION : " + str(session.get())
            Label(lblfrm1, text=text,font=("",15)).pack(pady=10, padx=10)
            lblfrm1.pack(pady=10)
            lblfrm3.pack(pady=10)

            lblfrm2 = LabelFrame(win2)

            counter = 0
            canvas = Canvas(lblfrm2)
            frame = Frame(canvas)

            for i in result:
                course_variable = StringVar()
                grade_variable = StringVar()
                counter_variable = IntVar()
                course_variable.set(i[0])
                grade_variable.set(i[1])
                counter_variable.set(counter + 1)
                Entry(frame, text=counter_variable, justify="center", width=10).grid(row=counter, column=0)
                Entry(frame, text=course_variable, justify="center", width=40).grid(row=counter, column=1)
                Entry(frame, text=grade_variable, justify="center", width=40).grid(row=counter, column=2)
                counter = counter + 1
            lblfrm2.pack()

            myscrollbar = Scrollbar(lblfrm2, orient="vertical", command=canvas.yview)
            canvas.configure(yscrollcommand=myscrollbar.set)
            myscrollbar.pack(side="right", fill="y")
            canvas.pack(side="left")

            canvas.create_window((0, 0), window=frame, anchor="nw")

            def myfunction(event):
                canvas.configure(scrollregion=canvas.bbox("all"), width=550, height=400)

            frame.bind("<Configure>", myfunction)

            win2.state("zoomed")

            def doSomething():

                win2.destroy()
                main.showMainPage()

            win2.protocol('WM_DELETE_WINDOW', doSomething)
            win2.mainloop()
    def get_info(self):
        global win
        win = Tk()
        win.title("STUDENT WISE RESULT CONFIGURATION")
        labelframe = ttk.LabelFrame(win)
        roll = StringVar()
        year =StringVar()
        term = StringVar()
        batch = StringVar()

        Label(labelframe,text = "BATCH :  ").grid(row=0,column=0,pady=15,padx=10)
        info = Info.Info()
        batch_tuple = tuple(info.get_batch())
        batch_combobox = ttk.Combobox(labelframe,textvariable =batch)
        batch_combobox["values"]=batch_tuple
        batch_combobox.grid(padx=10,pady=15,row=0,column=1)

        Label(labelframe,text="ROLL : ").grid(row=1,column=0,pady=15,padx=10)
        roll_list =list()
        for i in range(200):
            roll_list.append(i+1)
        roll_combo = ttk.Combobox(labelframe,textvariable = roll)
        roll_combo["values"] = tuple(roll_list)
        roll_combo.grid(row=1,column=1,pady=15,padx=10)

        Label(labelframe,text = "YEAR : ").grid(row=2,column=0,padx =10,pady=15)
        year_combobox = ttk.Combobox(labelframe,textvariable = year)
        year_combobox["values"] = ("First","Second","Third","Fourth")
        year_combobox.grid(row=2,column=1,padx=10,pady=15)

        Label(labelframe,text ="TERM : ").grid(row=3,column=0,padx=10,pady=15)
        term_combobox = ttk.Combobox(labelframe,textvariable =term)
        term_combobox["values"] = ("I","II","III","IV")
        term_combobox.grid(row=3,column=1,padx=10,pady=15)

        Button(labelframe,text="SHOW RESULT",background ="khaki3",command = partial(self.show_result,roll,year,term,batch)).grid(row=4,column=1,
                                                                                                       pady=15,padx=10)
        labelframe.pack(pady=60,padx=80)
        win.resizable(width=False,height =False)

        def doSomething():
            win.destroy()
            main.showMainPage()

        win.protocol('WM_DELETE_WINDOW', doSomething)
        win.mainloop()

#studentResult =StudentWiseResult()
#studentResult.get_info()