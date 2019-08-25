"""                                                          VERIFIED                                                          """

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import database
import messages
# Username: vivekascoder, Password: 9871496866
# Username: admin, Username: spy123
"""
ID
Name

Author
Publisher
Cost
Price
Date
Image
"""

class AddNewUser(Tk):
    def __init__(self):
        super(AddNewUser, self).__init__()
        self.drawWidgets()
        self.minsize(300, 280)
        self.title("Add New User.")
        self.resizable(False, False)

    def drawWidgets(self):
        j = 40
        labels = ['Username: ', 'Password: ']
        Label(self, text="Add New User", fg='white', bg='black', width=15, font=('arial', 25, 'bold')).place(x=0, y=0)
        for i in labels:
            Label(self, text=i).place(x=20, y=40+j)
            j+=40
        self.txt_username = ttk.Entry(self, width=26)
        self.txt_username.place(x=100, y=80)
        self.txt_password = ttk.Entry(self, width=26, show="●")
        self.txt_password.place(x=100, y=120)
        Button(self, text="Add User", bg="#2c3e50", fg="white", width=15, border=0, font=('Arial', 15, 'bold'), command=self.insert_user).place(x=50, y=180)

    def insert_user(self):
        database.insertUser((self.txt_username.get(), self.txt_password.get()))
        msg.showinfo(messages.add_new_user_done[0], messages.add_new_user_done[1])


        
        

