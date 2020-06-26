"""Customer Relationship Tools on TKInter"""

from tkinter import *
from tkinter import ttk
import sqlite3
import csv

root = Tk()
root.title('CRM Tool with TKInter')
root.iconbitmap('icon.ico')

frame_for_database = LabelFrame(root, padx=15, pady=15)
frame_for_database.grid(row=0, column=0, padx=10, pady=10)

# База данных
d_base = 'crm_dbt.db'
conn = sqlite3.connect(d_base) # create database + connect to it
c = conn.cursor() # create cursor

c.execute('''CREATE TABLE IF NOT EXISTS customers (
            first_name text,
            last_name text,
            username text,
            zipcode integer,
            price_paid real,
            email text(255),
            address_1 text(255),
            address_2 text(255),
            city text(50),
            state text(50),
            country text(255),
            phone text(255),
            payment_method text(50),
            discount_code text(255)
            )''')

first_name = Entry(frame_for_database, width=30)
last_name = Entry(frame_for_database, width=30)
zipcode = Entry(frame_for_database, width=30)
price_paid = Entry(frame_for_database, width=30)
email = Entry(frame_for_database, width=30)
address_1 = Entry(frame_for_database, width=30)
address_2 = Entry(frame_for_database, width=30)
city = Entry(frame_for_database, width=30)
state = Entry(frame_for_database, width=30)
country = Entry(frame_for_database, width=30)
phone = Entry(frame_for_database, width=30)
payment_method = Entry(frame_for_database, width=30)
discount_code = Entry(frame_for_database, width=30)
username = Entry(frame_for_database, width=30)

first_name.grid(row=0, column=1)
last_name.grid(row=1, column=1)
zipcode.grid(row=2, column=1)
price_paid.grid(row=3, column=1)
email.grid(row=4, column=1)
address_1.grid(row=5, column=1)
address_2.grid(row=6, column=1)
city.grid(row=7, column=1)
state.grid(row=8, column=1)
country.grid(row=9, column=1)
phone.grid(row=10, column=1)
payment_method.grid(row=11, column=1)
discount_code.grid(row=12, column=1)
username.grid(row=13, column=1)

first_name_label = Label(frame_for_database, text='Имя')
last_name_label = Label(frame_for_database, text='Фамилия')
zipcode_label = Label(frame_for_database, text='Индекс')
price_paid_label = Label(frame_for_database, text='Заплатил')
email_label = Label(frame_for_database, text='Email')
address_1_label = Label(frame_for_database, text='Адрес 1')
address_2_label = Label(frame_for_database, text='Адрес 2')
city_label = Label(frame_for_database, text='Город')
state_label = Label(frame_for_database, text='Штат')
country_label = Label(frame_for_database, text='Страна')
phone_label = Label(frame_for_database, text='Телефон')
payment_method_label = Label(frame_for_database, text='Метод оплаты')
discount_code_label = Label(frame_for_database, text='Дсконтный код')
username_label = Label(frame_for_database, text='Ник')

first_name_label.grid(row=0,column=0, sticky=W, padx=10)
last_name_label.grid(row=1,column=0, sticky=W, padx=10)
zipcode_label.grid(row=2,column=0, sticky=W, padx=10)
price_paid_label.grid(row=3,column=0, sticky=W, padx=10)
email_label.grid(row=4,column=0, sticky=W, padx=10)
address_1_label.grid(row=5,column=0, sticky=W, padx=10)
address_2_label.grid(row=6,column=0, sticky=W, padx=10)
city_label.grid(row=7,column=0, sticky=W, padx=10)
state_label.grid(row=8,column=0, sticky=W, padx=10)
country_label.grid(row=9,column=0, sticky=W, padx=10)
phone_label.grid(row=10,column=0, sticky=W, padx=10)
payment_method_label.grid(row=11,column=0, sticky=W, padx=10)
discount_code_label.grid(row=12,column=0, sticky=W, padx=10)
username_label.grid(row=13,column=0, sticky=W, padx=10)

def submit():
    conn = sqlite3.connect(d_base)  # create database + connect to it
    c = conn.cursor()  # create cursor
    c.execute('INSERT INTO customers VALUES (:first_name, :last_name, :zipcode, :price_paid, :email, :address_1, :address_2, :city, :state, :country, :phone, :payment_method, :discount_code, :username)',
        {"first_name":first_name.get(),"last_name":last_name.get(),"zipcode":zipcode.get(),
        "price_paid":price_paid.get(),"email":email.get(),"address_1":address_1.get(),
        "address_2":address_2.get(),"city":city.get(),"state":state.get(),
        "country":country.get(),"phone":phone.get(),"payment_method":payment_method.get(),
        "discount_code":discount_code.get(),"username":username.get()})
    conn.commit()  # commit changes to database
    conn.close()  # close connection
    clear_fields()

def query():
    conn = sqlite3.connect(d_base)
    c = conn.cursor()
    c.execute('SELECT *,oid FROM customers')
    records = c.fetchall()
    conn.commit()
    conn.close()
    print(records)
    return records

def destroy_database():
    conn = sqlite3.connect(d_base)  # create database + connect to it
    c = conn.cursor()  # create cursor
    c.execute('DELETE FROM addresses')
    conn.commit()  # commit changes to database
    conn.close()  # close connection

def clear_fields():
    first_name.delete(0,END)
    last_name.delete(0,END)
    zipcode.delete(0,END)
    price_paid.delete(0,END)
    email.delete(0,END)
    address_1.delete(0,END)
    address_2.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    country.delete(0,END)
    phone.delete(0,END)
    payment_method.delete(0,END)
    discount_code.delete(0,END)
    username.delete(0,END)

def write_to_csv(result):
    with open('customers.csv', 'a', newline='') as f: # a -> append
        w = csv.writer(f, dialect='excel')
        for records in result:
            w.writerow(records)

def grab_all_records():
    conn = sqlite3.connect(d_base)
    c = conn.cursor()
    c.execute('SELECT *,oid FROM customers')
    records = c.fetchall()
    conn.commit()
    conn.close()
    return records

def spreadsheet(window,records):
    Label(window, text="№").grid(row=1, column=0)
    for index, x in enumerate(records, 1):
        num = 1
        for y in x:
            Label(window, text=y).grid(row=index + 1, column=num)
            num += 1

def list_customers():
    list_customers_query = Tk()
    list_customers_query.title('Список клиентов')
    list_customers_query.iconbitmap('icon.ico')
    records = grab_all_records()
    spreadsheet(list_customers_query,records)
    csv_button = Button(list_customers_query, text='Экспорт в CSV', command=lambda: write_to_csv(result))
    csv_button.grid(row=0,column=0,columnspan=2)

def search_customers():
    search_customers = Tk()
    search_customers.title('Поиск клиентов')
    search_customers.iconbitmap('icon.ico')
    def search_now():
        selected = drop.get()
        param = None
        if selected == 'Фамилия': param = 'last_name'
        if selected == 'Имя': param = 'first_name'
        if selected == 'Эмейл': param = 'email'
        if selected == 'Телефон': param = 'phone'
        searched = search_box.get()
        conn = sqlite3.connect(d_base)
        c = conn.cursor()
        c.execute(f'SELECT *,oid FROM customers WHERE {param} LIKE \'%{searched}%\'')
        records = c.fetchall()
        conn.commit()
        conn.close()
        if not records:
            records = 'Ничего не найдено'
        spreadsheet(search_customers,records)
    search_box = Entry(search_customers)
    search_box.grid(row=0,column=2,padx=10,pady=10)
    search_box_label = Label(search_customers, text='Поиск по параметру: ').grid(row=0,column=0,padx=10,pady=10)
    search_btn = Button(search_customers, text='Поиск',command=search_now).grid(row=0,column=3,padx=10,pady=10)
    drop = ttk.Combobox(search_customers, value=['Фамилия','Имя','Эмейл','Телефон'])
    drop.current(0)
    drop.grid(row=0,column=1,padx=10,pady=10)





result = query()
submit_btn = Button(frame_for_database, text='Внести в базу',command=submit).grid(row=14,column=0,pady=10,padx=10)
clear_btn = Button(frame_for_database, text='Очистить поля',command=clear_fields).grid(row=14,column=1,pady=10,padx=10)

list_customers_btn = Button(frame_for_database, text='Отобразить список всех клиентов',command=list_customers).grid(row=15,column=0,pady=10,padx=10,sticky=W)
search_for_customers_btn = Button(frame_for_database, text='Поиск',command=search_customers).grid(row=15,column=1,pady=10,padx=10,sticky=W)


conn.commit()  #commit changes to database
conn.close()  #close connection

root.mainloop()