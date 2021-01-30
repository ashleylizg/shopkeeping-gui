from tkinter import *
import sqlite3

window = Tk()
window.geometry("400x450")
window.title("Inventory Summary")
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

def update():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    record_id = select_box.get()

    cursor.execute(
        'UPDATE items SET name=?, quantity=?, price=? WHERE oid=?',
        (item_name_editor.get(),item_quantity_editor.get(),item_price_editor.get(),record_id)
    )
    connection.commit()
    connection.close()
    editor.destroy()

def edit():
    global editor
    editor = Tk()
    editor.geometry("450x125")
    editor.title("Edit Inventory")
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    record_id = select_box.get()

    cursor.execute("SELECT * FROM items WHERE oid=?",(record_id))
    records = cursor.fetchall()

    global item_name_editor
    global item_quantity_editor
    global item_price_editor

    item_name_editor = Entry(editor, width=20)
    item_name_editor.grid(row=0, column=1, sticky=W)
    item_quantity_editor = Entry(editor, width=20)
    item_quantity_editor.grid(row=1, column=1, sticky=W)
    item_price_editor = Entry(editor, width=20)
    item_price_editor.grid(row=2, column=1, sticky=W)

    item_name_label_editor = Label(editor, text='Name ')
    item_name_label_editor.grid(row=0, column=0, sticky=E)
    item_quantity_label_editor = Label(editor,  text='Quantity ')
    item_quantity_label_editor.grid(row=1, column=0, sticky=E)
    item_price_label_editor = Label(editor, text ='Price ($) ')
    item_price_label_editor.grid(row=2,column=0, sticky=E)

    for record in records:
        item_name_editor.insert(0, record[0])
        item_quantity_editor.insert(0, record[1])
        item_price_editor.insert(0, record[2])
    save_btn = Button(editor, text="Save Record", command=update)
    save_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=145)
    connection.commit()
    connection.close()

def delete():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    cursor.execute("DELETE from items WHERE oid=?",(select_box.get()))
    connection.commit()
    connection.close()

def submit():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO items(name,quantity,price) VALUES (?,?,?)",(item_name.get(),item_quantity.get(),item_price.get()))
    connection.commit()
    connection.close()
    item_name.delete(0, END)
    item_quantity.delete(0, END)
    item_price.delete(0, END)

def query():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    cursor.execute("SELECT *, oid FROM items")
    records = cursor.fetchall()
    print(records)
    print_records = ''
    for record in records:
        print_records += str(record[0]) + ", " + str(record[1]) + " items, $" + "{:.2f}".format(float(record[2])) + ", ID" + "\t" + str(record[3]) +"\n"
    query_label = Label(window, text=print_records)
    query_label.grid(row=5, column=0, columnspan=2)
    connection.commit()
    connection.close()

def calc_price():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM items WHERE oid=?",(select_box.get()))
    records = cursor.fetchall()
    price_sum = []
    for record in records:
        price_sum.append(round((record[2] / record[1]) * int(price_calc.get()),2))
    global calc_sum_label
    calc_sum_label = Label(window, text=price_sum)
    calc_sum_label.grid(row=9, column=0, columnspan=2, pady=2)
    connection.commit()
    connection.close()

def clear_output():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    calc_sum_label.destroy()
    connection.commit()
    connection.close()

item_name = Entry(window, width=20)
item_name.grid(row=0, column=1, pady=2, sticky=W)
item_quantity = Entry(window, width=20)
item_quantity.grid(row=1, column=1, pady=2, sticky=W)
item_price = Entry(window, width=20)
item_price.grid(row=2, column=1, pady=2, sticky=W)
select_box=Entry(window, width=20)
select_box.grid(row=6, column=1, pady=2, sticky=W)
price_calc=Entry(window, width=20)
price_calc.grid(row=7, column=1, pady=2, sticky=W)

item_name_label = Label(window, text='Name ')
item_name_label.grid(row=0, column=0, pady=2, sticky=E)
item_quantity_label = Label(window,  text='Quantity ')
item_quantity_label.grid(row=1, column=0, pady=2, sticky=E)
item_price_label = Label(window, text ='Price ($) ')
item_price_label.grid(row=2,column=0, pady=2, sticky=E)
select_box_label = Label(window, text='Select ID ')
select_box_label.grid(row=6, column=0, pady=2, sticky=E)
price_calc_label = Label(window, text='Quantity for Price Sum ')
price_calc_label.grid(row=7, column=0, pady=2, sticky=E)

submit_btn = Button(window, text="Add Record to Database", command=submit)
submit_btn.grid(row=3, column=0, columnspan=2, pady=2)

query_btn = Button(window, text="Show Records", command=query)
query_btn.grid(row=4, column=0, columnspan=2, pady=2)

delete_btn = Button(window, text="Delete Record", command=delete)
delete_btn.grid(row=12, column=0, columnspan=2, pady=2)

edit_btn = Button(window, text="Update Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=2)

calculate_price_btn = Button(window, text="Calculate Price Sum", command=calc_price)
calculate_price_btn.grid(row=8, column=0, columnspan=2, pady=2)

clear_output_btn = Button(window, text="Clear Output", command=clear_output)
clear_output_btn.grid(row=10, column=0, columnspan=2, pady=2)

window.mainloop()