from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import database
import dashboard
import messages


class Login(Tk):
    def __init__(self):
        super(Login, self).__init__()
        self.drawWidgets()
        self.minsize(400, 240)
        self.title("Login {*_*}")
        self.resizable(False, False)

    def drawWidgets(self):
        labels = ['Username: ', 'Password: ']
        j=40
        Label(self, text="Login", fg='white', bg='black', width=20, font=('arial', 25, 'bold')).place(x=0, y=0)

        for i in labels:
            Label(self, text=i).place(x=50, y=40+j)
            j+=40

        self.txt_username = ttk.Entry(self, width=30)
        self.txt_password = ttk.Entry(self, width=30, show="●")
        self.txt_username.place(x=150, y=80)
        self.txt_password.place(x=150, y=120)

        ttk.Button(self, text="Login", width=15, command=self.login).place(x=60, y=170)
        ttk.Button(self, text="Exit", width=15, command=self.exit).place(x=220, y=170)

        lbl_forgot = Label(self,text="Forgot Password?", fg='blue')
        lbl_forgot.place(x=150, y=200)
        lbl_forgot.bind('<Button-1>', lambda e:self.forgot())

    def login(self):
        if database.validateUser(self.txt_username.get(), self.txt_password.get()):
            print("Logged in as : ", self.txt_username.get(), self.txt_password.get())
            dash = dashboard.Dashboard()
            dash.mainloop()
        else:
            print("Not a user.")
            msg.showerror(messages.login_error[0], messages.login_error[1])

    def forgot(self):
        msg.showinfo("Forgot Password", "Dont't Worry.\nContact to XXXXXXXXXX to \nknow your password.")
    
    def exit(self):
        exit()
        


login = Login()
login.mainloop()
