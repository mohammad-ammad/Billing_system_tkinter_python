from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkmsg
from connection import menucol

class mymenu(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("750x450")
        self.title("Biling System")

    def menu_section(self):
        f1 = Frame(self, bg="black", borderwidth=3, relief=SUNKEN)
        l1 = Label(f1, text="MENU", bg="black", fg="white", font="comicsms 15 bold")
        f1.pack(side=TOP, fill=X)
        l1.pack()

    def main_menu(self):
        global check1, check2, check3, check4, check5, check6, check7, check8, var, treeview
        check1 = IntVar()
        check2 = IntVar()
        check3 = IntVar()
        check4 = IntVar()
        f2 = LabelFrame(self, text="Main course", font="comicsms 10 bold", borderwidth=2, relief=SUNKEN)
        list = ['biryani', 'haleem', 'karahi', 'roti']
        check = [check1, check2, check3, check4]
        for i in range(len(list)):
            checkbox = Checkbutton(f2, text=list[i], variable=check[i], padx=15, pady=5)
            checkbox.pack(anchor="w")

        f2.pack(side=LEFT, padx=15)

        check5 = IntVar()
        check6 = IntVar()
        check7 = IntVar()
        check8 = IntVar()
        f3 = LabelFrame(self, text="Drinks", font="comicsms 10 bold", borderwidth=2, relief=SUNKEN)
        lists = ['coke', 'sprite', 'marinda', 'Dew']
        check = [check5, check6, check7, check8]
        for i in range(len(lists)):
            checkbox = Checkbutton(f3, text=lists[i], variable=check[i], padx=15, pady=5)
            checkbox.pack(anchor="w")

        f3.pack(side=LEFT, padx=15)

        f4 = LabelFrame(self, text="Size", font="comicsms 10 bold", borderwidth=2, relief=SUNKEN)
        var = IntVar()
        radio = Radiobutton(f4, text="small", variable=var, value="1")
        radio.pack(anchor="n")
        radio1 = Radiobutton(f4, text="large", variable=var, value="2")
        radio1.pack(anchor="n")
        f4.pack(side=LEFT)
        f5 = Frame(self)
        btn = Button(f5, text="Add", width=10, bg="black", fg="white", command=self.Add)
        btn.pack()
        f5.pack(side=BOTTOM, padx=8, pady=8)

        f6 = Frame(self)
        col = ('id', 'item', 'price')
        treeview = ttk.Treeview(self, height=10, show="headings", columns=col)
        treeview.column('id', width=50, anchor=CENTER)
        treeview.column('item', width=100, anchor=CENTER)
        treeview.column('price', width=100, anchor=CENTER)
        treeview.heading('id', text="No.")
        treeview.heading('item', text="Item")
        treeview.heading('price', text="Price")
        treeview.pack(pady=40)
        f6.pack(side=LEFT)

        f7 = Frame(self)
        btn1 = Button(f7, text="Delete", width=10, bg="black", fg="white", command=self.deleteItem)
        btn1.pack()
        f7.pack(side=BOTTOM, padx=8, pady=8)

    def Add(self):
        i = 0
        food = ""
        price = 0
        if check1.get() == 1 and var.get() == 1:
            treeview.insert('', i, values=(1, 'Biryani', 200))
            food = 'biryani'
            price = 200
        elif check1.get() == 1 and var.get() == 2:
            treeview.insert('', i, values=(1, 'Biryani', 250))
            food = 'biryani'
            price = 250
        if check2.get() == 1 and var.get() == 1:
            treeview.insert('', i, values=(1, 'Haleem', 70))
            food = 'haleem'
            price = 70
        elif check2.get() == 1 and var.get() == 2:
            treeview.insert('', i, values=(1, 'Haleem', 150))
            food = 'haleem'
            price = 150
        if check3.get() == 1 and var.get() == 1:
            treeview.insert('', i, values=(1, 'Karahi', 600))
            food = 'karahi'
            price = 600
        elif check3.get() == 1 and var.get() == 2:
            treeview.insert('', i, values=(1, 'Karahi', 850))
            food = 'karahi'
            price = 850
        if check4.get() == 1:
            treeview.insert('', i, values=(1, 'Roti', 20))
            food = 'Roti'
            price = 20
        if check5.get() == 1 and var.get() == 1:
            treeview.insert('', i, values=(1, 'Coke', 90))
            food = 'coke'
            price = 90
        elif check5.get() == 1 and var.get() == 2:
            treeview.insert('', i, values=(1, 'Coke', 130))
            food = 'coke'
            price = 130
        if check6.get() == 1 and var.get() == 1:
            treeview.insert('', i, values=(1, 'Sprite', 90))
            food = 'sprite'
            price = 90
        elif check6.get() == 1 and var.get() == 2:
            treeview.insert('', i, values=(1, 'Sprite', 130))
            food = 'sprite'
            price = 130
        if check7.get() == 1 and var.get() == 1:
            treeview.insert('', i, values=(1, 'Marinda', 90))
            food = 'marinda'
            price = 90
        elif check7.get() == 1 and var.get() == 2:
            treeview.insert('', i, values=(1, 'Marinda', 130))
            food = 'marinda'
            price = 130
        if check8.get() == 1 and var.get() == 1:
            treeview.insert('', i, values=(1, 'Dew', 90))
            food = 'Dew'
            price = 90
        elif check8.get() == 1 and var.get() == 2:
            treeview.insert('', i, values=(1, 'Dew', 130))
            food = 'Dew'
            price = 130
        menucol.insert_one({'item': food, 'price': price})


    def deleteItem(self):
        try:
            item = treeview.selection()
            treeview.delete(item)
        except:
            tkmsg.showinfo("Billing System", "Please select something to delete")



