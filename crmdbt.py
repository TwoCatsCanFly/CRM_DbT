"""Customer Relationship Tools on TKInter"""

from tkinter import *
import sqlite3

root = Tk()
root.title('TKInter Tips')


d_base = 'crm_dbt.db'
frame_for_database = LabelFrame(root, text='CRM', padx=15, pady=15)
frame_for_database.grid(row=0, column=4, padx=10, pady=10)
conn = sqlite3.connect(d_base) # create database + connect to it
c = conn.cursor() # create cursor

c.execute('''CREATE TABLE IF NOT EXISTS addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer)''')

f_name = Entry(frame_for_database, width=30)
l_name = Entry(frame_for_database, width=30)
address = Entry(frame_for_database, width=30)
city = Entry(frame_for_database, width=30)
state = Entry(frame_for_database, width=30)
zip_code = Entry(frame_for_database, width=30)
f_name.grid(row=0, column=1)
l_name.grid(row=1, column=1)
address.grid(row=2, column=1)
city.grid(row=3, column=1)
state.grid(row=4, column=1)
zip_code.grid(row=5, column=1)

f_name_lbl = Label(frame_for_database, text='Имя')
l_name_lbl = Label(frame_for_database, text='Фамилия')
address_lbl = Label(frame_for_database, text='Адрес')
city_lbl = Label(frame_for_database, text='Город')
state_lbl = Label(frame_for_database, text='Штат')
zip_code_lbl = Label(frame_for_database, text='Индекс')
f_name_lbl.grid(row=0, column=0)
l_name_lbl.grid(row=1, column=0)
address_lbl.grid(row=2, column=0)
city_lbl.grid(row=3, column=0)
state_lbl.grid(row=4, column=0)
zip_code_lbl.grid(row=5, column=0)

def submit():
    conn = sqlite3.connect(d_base)  # create database + connect to it
    c = conn.cursor()  # create cursor
    c.execute('INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zip_code)',
        {'f_name': f_name.get(),
        'l_name': l_name.get(),
        'address': address.get(),
        'city': city.get(),
        'state': state.get(),
        'zip_code': zip_code.get()})
    conn.commit()  # commit changes to database
    conn.close()  # close connection
    # clear texboxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zip_code.delete(0,END)
def query():
    conn = sqlite3.connect(d_base)  # create database + connect to it
    c = conn.cursor()  # create cursor
    c.execute('SELECT *,oid FROM addresses')
    records = c.fetchall()# сколько записей взять
    for id, record in enumerate(records):
        rid=9+id
        Label(frame_for_database,text=record).grid(row=rid,column=0)
    conn.commit()  # commit changes to database
    conn.close()  # close connection
def destr_database():
    conn = sqlite3.connect(d_base)  # create database + connect to it
    c = conn.cursor()  # create cursor
    c.execute('DELETE FROM addresses')
    conn.commit()  # commit changes to database
    conn.close()  # close connection


submit_btn = Button(frame_for_database, text='Submit to Database',command=submit).grid(row=6,column=0, columnspan =2,pady=10,padx=10,ipadx=50)
query_btn = Button(frame_for_database, text='Show from Database',command=query).grid(row=7,column=0, columnspan =2,ipadx=50)
clear_btn = Button(frame_for_database, text='DESTROY Database',command=destr_database).grid(row=8,column=0, columnspan =2,ipadx=50)


conn.commit()  #commit changes to database
conn.close()  #close connection



root.mainloop()