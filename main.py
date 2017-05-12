import loginPage
import disciplineForm

#import addCourse
import home
import registration
import  marksEntry
import pymysql
from tkinter import *
import  sys
from tkinter import scrolledtext


def showMainPage():

    h = home.Home()
    h.show()

if __name__=='__main__':


    conn = pymysql.connect(user='root',password="")
    cursor = conn.cursor()

    try:
        cursor.execute('CREATE DATABASE {} DEFAULT CHARACTER SET "utf8"'.format('tabulationSystemKU'))
    except pymysql.Error as err:
        print(err)
    try:
        cursor.execute('USE tabulationSystemKU')
        #cursor.execute('DROP TABLE coursetable')
        cursor.execute('CREATE TABLE coursetable (course_ID INT NOT NULL AUTO_INCREMENT,'
                       'yearborsho VARCHAR(10) NOT NULL ,'
                       'term VARCHAR (10) NOT NULL ,'
                       'courseno VARCHAR(20) NOT NULL,'
                       'coursetitle VARCHAR(250) NOT NULL,'
                       'credit DOUBLE NOT NULL ,'
                       'PRIMARY KEY(course_ID))'
                       'ENGINE=InnoDB')

    except pymysql.Error as err:
        print(err)

    try:
        cursor.execute("USE tabulationSystemKU")
        #cursor.execute("DROP TABLE students")
        cursor.execute("CREATE TABLE students ("
                       "rollNo VARCHAR(20) NOT NULL,"
                       "name VARCHAR(250) NOT NULL,"
                       "batch INT NOT NULL,"
                       "tech DOUBLE NOT NULL,"
                       "tecp DOUBLE NOT NULL ,"
                       "PRIMARY KEY(rollNo)) ENGINE=InnoDB")

    except pymysql.Error as err:
        print(err)

    #addcrs=addCourse.AddCourse()
    #addcrs.show()

    try:
        cursor.execute('USE tabulationSystemKU')
        #cursor.execute("DROP TABLE disciplineInfo")
        cursor.execute('CREATE TABLE disciplineInfo (ID INT NOT NULL AUTO_INCREMENT,'
                       'disciplineName VARCHAR (250) NOT NULL, '
                       'schoolName VARCHAR(100) NOT NULL ,'
                       'disciplineCode VARCHAR(10) NOT NULL,'
                       'requiredCredit DOUBLE NOT NULL ,'
                       'thesisCategory VARCHAR(400) NOT NULL,'
                       'PRIMARY KEY(ID))ENGINE=InnoDB ')

    except pymysql.Error as err:
        print(err)


    try:
        cursor.execute("USE tabulationSystemKU")
        #cursor.execute("DROP TABLE theory_result")
        cursor.execute("CREATE TABLE theory_result (ID INT NOT NULL AUTO_INCREMENT,"
                       "session VARCHAR(30) NOT NULL,"
                       "year VARCHAR (30) NOT NULL,"
                       "term VARCHAR(30) NOT NULL,"
                       "courseNo VARCHAR (50) NOT NULL,"
                       "roll VARCHAR (20) NOT NULL,"
                       "attendance DOUBLE NOT NULL,"
                       "ct DOUBLE NOT NULL,"
                       "seca DOUBLE NOT NULL,"
                       "secb DOUBLE NOT NULL,"
                       "gpa DOUBLE NOT NULL,"
                       "grade VARCHAR (10) NOT NULL,"
                       "PRIMARY KEY (ID))ENGINE = InnoDB")

    except pymysql.Error as err:
        print(err)

    try:
        cursor.execute("USE tabulationSystemKU")
        #cursor.execute("DROP TABLE prerequisite_table")
        cursor.execute("CREATE TABLE prerequisite_table (ID INT NOT NULL AUTO_INCREMENT,"
                       "course VARCHAR(30) NOT NULL,"
                       "prerequisite VARCHAR (30) NOT NULL,"
                       "PRIMARY KEY (ID))ENGINE = InnoDB")

    except pymysql.Error as err:
        print(err)

    try:
        cursor.execute("USE tabulationSystemKU")
        #cursor.execute("DROP TABLE sessional_result")
        cursor.execute("CREATE TABLE sessional_result (ID INT NOT NULL AUTO_INCREMENT,"
                       "session VARCHAR(30) NOT NULL,"
                       "year VARCHAR (30) NOT NULL,"
                       "term VARCHAR(30) NOT NULL,"
                       "courseNo VARCHAR (50) NOT NULL,"
                       "roll VARCHAR (20) NOT NULL,"
                       "attendance DOUBLE NOT NULL,"
                       "sa DOUBLE NOT NULL,"
                       "viva DOUBLE NOT NULL,"
                       "gpa DOUBLE NOT NULL,"
                       "grade VARCHAR (10) NOT NULL,"
                       "PRIMARY KEY (ID))ENGINE = InnoDB")

    except pymysql.Error as err:
        print(err)

    try:
        cursor.execute("USE tabulationSystemKU")
        #cursor.execute("DROP TABLE batch")
       # cursor.execute("CREATE  TABLE batch (ID INT NOT NULL AUTO_INCREMENT,"
        #               "batch_number VARCHAR(5) NOT NULL,"
         #              "PRIMARY KEY (ID))ENGINE =InnoDB")
    except pymysql.Error as err:
        print(err)

    try:
        cursor.execute("USE tabulationSystemKU")
        #cursor.execute('DROP TABLE login')
        cursor.execute("CREATE TABLE login (ID INT NOT NULL AUTO_INCREMENT,"
                       "username VARCHAR(50) NOT NULL,"
                       "password VARCHAR(50) NOT NULL,"
                       "PRIMARY KEY(ID))ENGINE=InnoDB")
        cursor.execute("INSERT INTO login (username,password) VALUES ('{}','{}')".format("admin" ,'cse'))
        conn.commit()

    except pymysql.Error as err:
        print(err)

    try:
        cursor.execute("USE tabulationSystemKu")
        #cursor.execute("DROP TABLE CourseConfiguration")
        cursor.execute("CREATE TABLE CourseConfiguration (ID INT NOT NULL AUTO_INCREMENT,"
                       "year VARCHAR(25) NOT NULL,"
                       "term VARCHAR (25) NOT NULL,"
                       "session VARCHAR (25) NOT NULL,"
                       "creditLimit VARCHAR (25),"
                        "batch VARCHAR (10) NOT NULL,"
                       "PRIMARY KEY(ID))ENGINE  = InnoDB")

    except pymysql.Error as err:
        print(err)

    try:
        cursor.execute("USE tabulationSystemKU")
        #cursor.execute("DROP TABLE registration")
        cursor.execute('''CREATE TABLE registration (ID INT NOT NULL AUTO_INCREMENT,
                        rollNo VARCHAR(15) NOT NULL,
                        courseNo VARCHAR (20) NOT NULL,
                        year VARCHAR (15) NOT NULL,
                        term VARCHAR (15) NOT NULL,
                        es VARCHAR (20) NOT NULL,
                        retake INT NOT NULL DEFAULT 0,
                        PRIMARY KEY(ID))ENGINE=InnoDB''')
    except pymysql.Error as err:
        print(err)

    conn.close()



    loginObject =loginPage.Login()
    loginObject.show()

    #discipline=disciplineForm.DisciplineFormClass()
    #discipline.show_form()
    #test =inputtest.InputTest()
    # test.show()
    #nstndt=newstudentform.NewStudentForm()
    #nstndt.show()

    #hm=home.Home()
    #hm.show()

    #rgtr = registration.Registration()
    #rgtr.show()

    #mrks= marksEntry.MarksEntry()
    #mrks.show()

    #loginPageObject = loginPage.Login()
    #loginPageObject.show()


#mainloop()