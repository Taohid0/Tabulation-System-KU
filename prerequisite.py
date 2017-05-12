from tkinter import *
import  pymysql
from tkinter import ttk
from functools import partial
from tkinter import messagebox
import main
conn = pymysql.connect(user="root",password="")
cursor = conn.cursor()
try:
    cursor.execute("Use tabulationSystemKU")
except pymysql.Error as err:
    print(err)

class Prerequisite():
    grid_counter = 0

    def show(self):
        win = Tk()
        win.title("ADD PREREQUISITES")
        label_list = []
        combobox_list = []

        for i in range(15):
            label_list.append(Label)
            combobox_list.append(ttk.Combobox)

        subject = StringVar()
        prerequites_variable =[]
        number_of_prerequisites = IntVar()
        for i in range(15):
            prerequites_variable.append(StringVar())
        try:
            cursor.execute("SELECT courseNo from courseTable")
            temp =list(cursor.fetchall())
        except pymysql.Error as err:
            print(err)
        subject_list = list()

        for i in temp:
            subject_list.append(i[0])

        labelFrame = LabelFrame(win)
        Label(labelFrame,text="SUBJECT : ").grid(row=0,column=0,padx=15,pady=15)
        subject_combobox = ttk.Combobox(labelFrame,textvariable =subject)
        subject_combobox["values"] = tuple(subject_list)
        subject_combobox.grid(row=0,column=1,padx=15,pady=15)

        number_of_prerequisites_list=[]
        for i in range(10):
            number_of_prerequisites_list.append(i+1)
        Label(labelFrame,text = "NUMBER OF PREREQUISITES : ").grid(row=1,column=0,pady=15,padx=15)
        number_of_prerequisites_combobox = ttk.Combobox(labelFrame,textvariable=number_of_prerequisites)
        number_of_prerequisites_combobox["values"] = tuple(number_of_prerequisites_list)
        labelFramePrerequisite = LabelFrame(labelFrame)
        def input_prerequisite(num,labelFramePrerequisite,event):

            labelFramePrerequisite.grid_forget()

            for i in range(15):
                prerequites_variable[i].set("")

            for j in range(self.grid_counter):
                label_list[j].grid_forget()
                combobox_list[j].grid_forget()
            self.grid_counter=0
            for i in range(num.get()):
                self.grid_counter+=1
                label_list[i]=Label(labelFramePrerequisite,text= "SUBJECT "+str(i+1)+ " : ")
                label_list[i].grid(row=i,column=0,padx=15,pady=15)
                combobox_list[i]=combobox = ttk.Combobox(labelFramePrerequisite,textvariable =prerequites_variable[i] )
                combobox["values"]=tuple(subject_list)
                combobox.grid(row=i,column=1,padx=15,pady=15)

            labelFramePrerequisite.grid(row=2,column=0,padx=15,pady=15)





        number_of_prerequisites_combobox.bind("<<ComboboxSelected>>",partial(input_prerequisite,number_of_prerequisites,
                                                                             labelFramePrerequisite))
        number_of_prerequisites_combobox.grid(row=1, column=1, pady=15, padx=15)

        def save():
            counter=0
            if(not subject.get()):
                messagebox.showerror("ERROR","PLEASE SELECT SUBJECT")
            else:
                for i in range(10):

                    if(prerequites_variable[i].get() and prerequites_variable[i].get() != subject.get()):
                        counter+=1
                        try:
                            cursor.execute("INSERT INTO prerequisite_table (course,prerequisite)"
                                       "VALUES ('{}','{}')".format(subject.get().strip(),prerequites_variable[i].get().strip()))
                        except pymysql.Error as err:
                            print(err)
                conn.commit()
                messagebox.showinfo("SUCCESSFULL","YOU HAVE SUCCESSFULLY ADDED " +str(counter)+ " "
                                                                                                "SUBJECT(S) AS PREREQUISITE")
                win.destroy()
                main.showMainPage()

        Button(labelFrame, text="SAVE" ,padx=30,command=save, background="khaki3").grid(row=2,column=1,sticky=N,pady=15)
        labelFrame.pack(pady=30, padx=30)

        win.mainloop()
