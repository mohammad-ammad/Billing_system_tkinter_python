# billing system by ammad

from tkinter import *
import tkinter.messagebox as msgbox
from menu import mymenu
from connection import mycol


class login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("250x200")
        self.title("Billing System")

    def form(self):
        global user, password
        user = StringVar()
        password = StringVar()
        l1 = Label(self, text="Login form:", font="comicsms 15 bold")
        l1.grid(row=0, column=1)
        l2 = Label(self, text="Username:")
        l2.grid(row=1)
        l3 = Label(self, text="Password:")
        l3.grid(row=2)
        userEntry = Entry(self, textvariable=user)
        userEntry.grid(row=1, column=1)
        passEntry = Entry(self, textvariable=password)
        passEntry.grid(row=2, column=1)
        btn = Button(self, text="login", command=self.submit)
        btn.grid()

    def submit(self):
        u1 = user.get()
        p1 = password.get()
        if mycol.find_one({"username": u1}) and mycol.find_one({"password": p1}):
            self.destroy()
            o = mymenu()
            o.menu_section()
            o.main_menu()
            o.mainloop()
        else:
            msgbox.showinfo("Billing System", "Wrong username and password")


if __name__ == '__main__':
    window = login()
    window.form()
    window.mainloop()
