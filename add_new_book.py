from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg

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

class AddNew(Tk):
    def __init__(self):
        super(AddNew, self).__init__()
        self.drawWidgets()
        self.minsize(400, 500)
        self.title("Login {*_*}")
        self.resizable(False, False)

    def drawWidgets(self):
        j = 40
        labels = ['ID: ', 'Name: ', 'Author: ', 'Publisher: ', 'Cost: ', 'Price: ']
        Label(self, text="Add New", fg='white', bg='black', width=25, font=('arial', 25, 'bold')).place(x=0, y=0)
        for i in labels:
            Label(self, text=i).place(x=20, y=40+j)
            j+=40

        
        


add_new = AddNew()
add_new.mainloop()
