from tkinter import *
import main

class Credit():
    def show(self):
        win = Tk()
        win.title("CREDIT")
        labelFrame = LabelFrame(win)
        credit_text = "THIS PROJECT IS DEVELOPED UNDER THE COURSE SOFTWARE DEVELOPMENT PROJECT\nCSE DISCIPLINE" \
                      "\nKHULNA UNIVERSITY"
        supervisors = "SUPERVISORS"
        debashish_sir_name = "DEBASISH CHAKROBORTI"
        tabassum_mam_name = "FATIMA TABASSUM"
        developer_text ="DEVELOPER"
        taohid ="TAOHIDUL ISLAM (140202)"
        farhana = "FARHANA KHANDOKAR (140203)"
        palash = "EKHLASHUR RAHMAN (130212)"

        Label(labelFrame,text =credit_text,font=("",20)).pack(pady=20,padx=10)

        Label(labelFrame, text="").pack(pady=10)
        Label(labelFrame,text=supervisors,font = ("",20)).pack()
        Label(labelFrame,text = debashish_sir_name,font=("",20)).pack(pady=5)
        Label(labelFrame,text =tabassum_mam_name,font = ("",20)).pack(pady=5)
        Label(labelFrame,text = "").pack(pady=10)
        Label(labelFrame,text = developer_text,font = ("",20)).pack()
        Label(labelFrame,text=taohid,font = ("",20)).pack(pady=5)
        Label(labelFrame,text=farhana,font = ("",20)).pack(pady=5)
        Label(labelFrame,text=palash,font = ("",20)).pack(pady=5)



        labelFrame.pack(pady=80)
        win.state("zoomed")
        def doSomething():

            win.destroy()
            main.showMainPage()

        win.protocol('WM_DELETE_WINDOW', doSomething)
        win.mainloop()

