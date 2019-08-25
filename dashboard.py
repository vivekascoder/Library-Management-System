from tkinter import *
from tkinter import ttk
import add_new_user as add


class Dashboard(Tk):
    def __init__(self):
        super(Dashboard, self).__init__()
        self.title("Dashboard")
        self.minsize(1170, 800)
        self.resizable(False, False)
        self.drawWidgets()

    def drawWidgets(self):
        self.font = ('Arial', 15, 'bold')
        # self Title
        lbl_main = Label(self, text='Library Management System', width=24, relief='solid', background='black', foreground='white', font=('arial', 60, 'bold'))
        lbl_main.place(x=0, y=0)

        Button(self, text="Add New\nBooks", border=0, width=15, height=7, bg="#2c3e50", fg="white", font=self.font, activebackground='#7f8c8d', activeforeground='white').place(x=20, y=130)
        Button(self, text="Remove\nBooks", border=0, width=15, height=7, bg="#2c3e50", fg="white", font=self.font, activebackground='#7f8c8d', activeforeground='white').place(x=250, y=130)
        Button(self, text="Search Books\nBy ID", border=0, width=15, height=7, bg="#2c3e50", fg="white", font=self.font, activebackground='#7f8c8d', activeforeground='white').place(x=480, y=130)
        Button(self, text="Search Books\nBy Name", border=0, width=15, height=7, bg="#2c3e50", fg="white", font=self.font, activebackground='#7f8c8d', activeforeground='white').place(x=710, y=130)
        Button(self, text="Search Books\nBy Author", border=0, width=15, height=7, bg="#2c3e50", fg="white", font=self.font, activebackground='#7f8c8d', activeforeground='white').place(x=940, y=130)
        Button(self, text="Search Books\nBy Publisher", border=0,width=15, height=7, bg="#2c3e50", fg="white", font=self.font, activebackground='#7f8c8d', activeforeground='white').place(x=940, y=130)
        Button(self, text="See All \nBooks", border=0, width=15, height=7, bg="#2c3e50", fg="white", font=self.font, activebackground='#7f8c8d', activeforeground='white').place(x=20, y=350)
        Button(self, text="See All \nIssued Books", border=0, width=15, height=7, bg="#2c3e50", fg="white", font=self.font, activebackground='#7f8c8d', activeforeground='white').place(x=250, y=350)
        Button(self, text="See All \nUsers", border=0, width=15, height=7, bg="#2c3e50", fg="white", font=self.font, activebackground='#7f8c8d', activeforeground='white').place(x=480, y=350)
        Button(self, text="Update Profile", border=0, width=15, height=7, bg="#2c3e50", fg="white", font=self.font, activebackground='#7f8c8d', activeforeground='white').place(x=710, y=350)
        Button(self, text="Send Email\nTo Students", border=0, width=15, height=7, bg="#2c3e50", fg="white", font=self.font, activebackground='#7f8c8d', activeforeground='white').place(x=940, y=350)
        Button(self, text="Add New\nUser", border=0, width=15, height=7, bg="#2c3e50", fg="white", font=self.font, activebackground='#7f8c8d', activeforeground='white', command=self.add_new_user).place(x=20, y=570)

        Label(self, text="For More Feature Call : XXXXXXXXXX Or Visit Our Site XXXXXXXX.XXXX", width=170, bg='black', fg='white').place(x=0, y=785)
        
    def add_new_user(self):
        addnew = add.AddNewUser()
        addnew.mainloop()

