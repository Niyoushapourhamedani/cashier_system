import tkinter.ttk as ttk
import tkinter.messagebox as msg
from itertools import product
from tkinter import *
from tkinter import Tk, StringVar

import tk

from file_manager import *
from model import cashier
from cashier import casheir

cashier_list = []  #read_from_file()


def load_data(cashier_list):
    cashier_list = read_from_file()
    for row in table.get_children():
        table.delet(row)
    for cashier in cashier_list:
        table.insert("", End, values=cashier.to_tuple())


def reset_form():
    id.set(len(cashier_list) + 1)
    name.set("")
    username.set("")
    #load_data(cashier_list)

#استاد در save in cell خطا بود
def save_btn_click():
    cashier_list = cashier(id.get(), product_name.get(), username.get(),password.get(),)
    errors = cashier.validate()
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", " saved")
        cashier_list.append(cashier)
        write_to_file(cashier_list)
        reset_form()


def table_select():
    selected_cashier = cashier(table.item(table.focus())["values"])
    if selected:
        selected_cashier = casheir(*selected)
        if selected_cashier:
            id.set(selected_cashier.id)
            product.set(selected_cashier.name)
            username.set(selected_cashier.username)
            password.set(selected_cashier.password)


def edit_btn_click():
    selected = table.focus()
    if not selected:
        msg.showerror("Errors", "Please select a cashier")
        return
    update_cashier =(id.get(), product_name.get(), username.get())
    index = int(id.get())
    cashier_list[index] = update_cashier
    write_to_file(cashier_list)
    msg.showerror("Edit", "Edit cashier")
    reset_form()



def remove_btn_click():
    selected_product = (table.focus())["values"]
    if selected_product:
        table.delete(selected_product)


window: Tk = Tk()
window.title("Cashier info")
window.geometry("610x360")

Label(window, text="id").place(x=20, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=80, y=20)

#Name
Label(window, text="product_name").place(x=20, y=60)
name = StringVar()
Entry(window, textvariable=name).place(x=80, y=60)

#Username
Label(window, text="username").place(x=20, y=100)
username = StringVar()
Entry(window, textvariable=username).place(x=80, y=100)

table = ttk.Treeview(window, columns=[1, 2, 3, 4, ], show="headings")
table.heading(1, text="Id")
table.heading(2, text="product_Name")
table.heading(3, text="username")
table.heading(4, text="password")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)

table.bind("<<Treeviewselect>>",table_select)

table.place(x=230, y=20)

Button(window, text="Save", width=6, command=save_btn_click).place(x=20, y=220)
Button(window, text="Edit", width=6, command=edit_btn_click).place(x=90, y=220)
Button(window, text="Remove", width=6, command=remove_btn_click).place(x=160, y=220)
Button(window, text="Clear", width=6, command=reset_form).place(x=20, y=260, width=190)

reset_form()

window.mainloop()

