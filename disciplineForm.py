import tkinter as tk
from tkinter import ttk
from tkinter import *
import pymysql
import main
class DisciplineFormClass():

    def show(self):
        win = tk.Tk()
        win.title('Configure Discipline')
        win.minsize(width=500,height=400)
        win.maxsize(width=500,height=400)


        ttk.Label(win, text='Discipline Name : ').grid(column=0, row=0, pady=10)
        disciplineName = tk.StringVar()
        ttk.Entry(win, textvariable=disciplineName,width=55).grid(column=1, row=0, pady=10)

        ttk.Label(win, text='School Name : ').grid(column=0, row=1, pady=10)
        schoolName = tk.StringVar()
        ttk.Entry(win, textvariable=schoolName).grid(column=1, row=1, pady=10)

        ttk.Label(win, text='Discipline Code : ').grid(column=0, row=2, pady=10)
        disciplineCode = tk.StringVar()
        ttk.Entry(win, textvariable=disciplineCode).grid(column=1, row=2, pady=10)

        ttk.Label(win, text='Required credit to pass : ').grid(column=0, row=3, pady=10)
        requiredCredit = tk.DoubleVar()
        ttk.Entry(win, textvariable=requiredCredit).grid(column=1, row=3, pady=10)

        ttk.Label(win, text="Thesis Caregory : ").grid(column=0, row=4, pady=10)
        thesisCategory = tk.StringVar()
        category = ttk.Combobox(win, width=55, textvariable=thesisCategory)
        category['values'] = ('(I) No thesis.', '(II) Single course. Registration term I, Evaluation term II.'
                              , '(III) Single course in single term.', '(IV) Two courses, separate Evaluation.',
                              '(V) Two courses. Registration term I and II. Evaluation term II.')
        category.grid(column=1, row=4, pady=10)
        category.current(0)




        conn = pymysql.connect(user='root',password='')
        cursor=conn.cursor()

        def saveCommand():
            try:

                if  disciplineName.get() and schoolName.get() and disciplineCode.get():
                    cursor.execute("USE tabulationSystemKU")
                    cursor.execute("DELETE FROM disciplineInfo")
                    cursor.execute('INSERT INTO disciplineInfo (disciplineName,schoolName,disciplineCode,'
                               'requiredCredit,thesisCategory) VALUES ("{}","{}","{}","{}","{}")'.format(

                 disciplineName.get(),schoolName.get(),disciplineCode.get(),requiredCredit.get(),thesisCategory.get()))

                    conn.commit()

                    cursor.close()
                    win.destroy()
                    main.showMainPage()

            except pymysql.Error as err:
                print(err)

        ttk.Button(win, text='save',command=saveCommand).grid(column=1, row=5, pady=20, sticky=tk.E)
        #ttk.Button(win, text='Exit').grid(column=0, row=5, pady=20, sticky=tk.E)
        def doSomething():

            win.destroy()
            main.showMainPage()

        win.protocol('WM_DELETE_WINDOW', doSomething)

        win.mainloop()