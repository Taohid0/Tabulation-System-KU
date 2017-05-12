import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from addCourse import AddCourse
from newstudentform import NewStudentForm
from marksEntry import MarksEntry
import pymysql
import marksEntry
import loginPage
import registration
import disciplineForm
import registrationConfiguration
import sys
import pymysql
from StudentWiseResult import StudentWiseResult
from courseWiseResult import CourseWiseResult
from change_password import Settings
import credit
import prerequisite
import withdrawCourse
conn = pymysql.connect(user = "root",password = "")
cursor = conn.cursor()

class Home():


    def show(self):


        try:
            cursor.execute("USE tabulationSystemKU")
            cursor.execute("SELECT schoolName,disciplineName from disciplineInfo")
            discipline = cursor.fetchone()
        except pymysql.Error as err:

            print(err)
        if discipline==None:
            discipline = ("", "")
        win = tk.Tk()


        win.state('zoomed')
        win.title('TABULATION SYSTEM KHULNA UNIVERSITY')

        lblfrm=ttk.LabelFrame(win)
        lbl=ttk.Label(lblfrm,text='TABULATION SYSTEM KU',font=('',50))
        lbl.pack()

        schoolLabel =ttk.Label(lblfrm,text = "SCHOOL : "+discipline[0],font =("",50))
        schoolLabel.pack()
        disciplineLabel = ttk.Label(lblfrm,text="DISCIPLINE : "+discipline[1],font = ("",50))
        disciplineLabel.pack()


        lblfrm.pack()

        addcrse=AddCourse()
        addstdnt = NewStudentForm()
        mrksEntry=MarksEntry()



        def addcrsecommand():

            win.destroy()
            addcrse.show()


        def addStdntCmmnd():
            win.destroy()
            addstdnt.show()


        def mrksEntrycmmnd():
            win.destroy()
            mrksEntry.show()


        def loginPagecmmnd():
             win.destroy()
             lgnpage=loginPage.Login()
             lgnpage.show()

        def disciplineFormcommand():
            win.destroy()
            dscipline = disciplineForm.DisciplineFormClass()
            dscipline.show()
        def regisgtrationFormCommand():
            win.destroy()
            registrationObject = registration.Registration()
            registrationObject.show()

        def registrationConfigurationCommad():
            win.destroy()
            registrationConfigurationObject=registrationConfiguration.RegistrationConfiguratinClass()
            registrationConfigurationObject.show()

        def student_wise_show():
            win.destroy()
            student_wise_result =StudentWiseResult()
            student_wise_result.get_info()

        def course_wise_show():
            win.destroy()
            course_wise_result =CourseWiseResult()
            course_wise_result.get_term_data()

        def change_password():
            win.destroy()
            settings =Settings()
            settings.change_password()

        def credit_function():
            win.destroy()
            creditObject =credit.Credit()
            creditObject.show()

        def add_prerequisite():
            win.destroy()
            prerequisiteObject =prerequisite.Prerequisite()
            prerequisiteObject.show()

        def withdraw_courses_function():
            win.destroy()
            obj = withdrawCourse.WithdrawCoures()
            obj.show()


        def closeApplication():
            win.destroy()

        menubar=Menu(win)
        win.config(menu=menubar)

        menubar.add_separator()

        fileMenu=Menu(menubar,tearoff=0)
        fileMenu.add_command(label='Configure Discipline',command=disciplineFormcommand)
        fileMenu.add_separator()
        fileMenu.add_command(label='Add Student',command=addStdntCmmnd)
        fileMenu.add_separator()
        fileMenu.add_command(label='Add Courses',command=addcrsecommand)
        fileMenu.add_separator()
        fileMenu.add_command(label ="Add prerequisites",command  =add_prerequisite)
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit',command=closeApplication)

        menubar.add_cascade(label='File',menu=fileMenu)

        menubar.add_separator()

        editMenu = Menu(menubar,tearoff=0)
        editMenu.add_command(label="Withdraw courses",command = withdraw_courses_function)
        editMenu.add_separator()
        editMenu.add_command(label="Remove prerequisite")
        menubar.add_cascade(label="Edit",menu= editMenu)
        menubar.add_separator()

        reg=Menu(menubar)
        reg.configure(tearoff=0)
        reg.add_command(label='Configure Registration',command=  registrationConfigurationCommad)
        reg.add_separator()
        reg.add_command(label='Registration',command = regisgtrationFormCommand)
        #reg.add_separator()
        #reg.add_command(label='Add commant')

        menubar.add_cascade(label='Registration',menu=reg)

        menubar.add_separator()
        resultMenu=Menu(menubar,tearoff=0)
        resultMenu.add_command(label = 'Marks Entry',command=mrksEntrycmmnd)
        resultMenu.add_separator()
        #resultMenu.add_command(label='Show Result')
        #resultMenu.add_separator()
        #resultMenu.add_command(label='Print Result')

        show_result_submenu = Menu(resultMenu, tearoff=0)
        show_result_submenu.add_command(label="Course wise",command=course_wise_show)
        show_result_submenu.add_separator()
        show_result_submenu.add_command(label="Student wise",command =student_wise_show)
        resultMenu.add_cascade(label ="Show result",menu=show_result_submenu,underline=0)

        submenu1 =Menu(resultMenu,tearoff=0)
        submenu1.add_command(label="Course wise")
        submenu1.add_separator()
        submenu1.add_command(label = "Student wise")
        resultMenu.add_cascade(label='Print result', menu=submenu1, underline=0)

        menubar.add_cascade(label='Result',menu=resultMenu)

        menubar.add_separator()

        helpMenu=Menu(menubar,tearoff=0)

        helpMenu.add_command(label='Help')
        helpMenu.add_separator()
        helpMenu.add_command(label='About Us',command =credit_function)

        menubar.add_cascade(label='Help',menu=helpMenu)

        settings_menu = Menu(menubar,tearoff=0)
        settings_menu.add_command(label="Change password",command=change_password)
        menubar.add_cascade(label ="Settings",menu=settings_menu)

        win.mainloop()