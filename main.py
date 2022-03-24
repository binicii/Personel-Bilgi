from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("Employee.db")
root = Tk()
root.title("Personel Özlük Sistemi")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

name = StringVar()
age = StringVar()
surname = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()
tc = StringVar()
city = StringVar()

entries_frame = Frame(root, bg="#46244C")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Personel Özlük Bilgileri", font=("Calibri", 18, "bold"), bg="#46244C", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

lblName = Label(entries_frame, text="Ad", font=("Calibri", 16), bg="#46244C", fg="white")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblAge = Label(entries_frame, text="Doğum Tarihi", font=("Calibri", 16), bg="#46244C", fg="white")
lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtAge = Entry(entries_frame, textvariable=age, font=("Calibri", 16), width=30)
txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lblSurname = Label(entries_frame, text="Soyad", font=("Calibri", 16), bg="#46244C", fg="white")
lblSurname.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtSurname = Entry(entries_frame, textvariable=surname, font=("Calibri", 16), width=30)
txtSurname.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#46244C", fg="white")
lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblGender = Label(entries_frame, text="Cinsiyet", font=("Calibri", 16), bg="#46244C", fg="white")
lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ("Erkek", "Kadın")
comboGender.grid(row=3, column=1, padx=10, sticky="w")

lblContact = Label(entries_frame, text="Telefon", font=("Calibri", 16), bg="#46244C", fg="white")
lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
txtContact.grid(row=3, column=3, padx=10, sticky="w")

lblTc = Label(entries_frame, text="TC", font=("Calibri", 16), bg="#46244C", fg="white")
lblTc.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtTc = Entry(entries_frame, textvariable=tc, width=30,  font=("Calibri", 16))
txtTc.grid(row=4, column=1, columnspan=4, padx=10, sticky="w")

lblCity = Label(entries_frame, text="Memleket", font=("Calibri", 16), bg="#46244C", fg="white")
lblCity.grid(row=4, column=2, padx=10, pady=10, sticky="w")
comboCity = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=city, state="readonly")
comboCity['values'] = ("Bursa", "Van","Adana",  "Mersin", "Elazığ", "İstanbul", "Ankara", "izmir", "Antalya", "Düzce", "Erzurum", "Samsun", "Ordu", "Sinop", "Gaziantep")
comboCity.grid(row=4, column=3, padx=10, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    surname.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    tc.set(row[7])
    city.set(row[8])

    #txtTc.delete(1.0, END)
    #txtTc.insert(END, row[7])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtSurname.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtTc.get() == "" or comboCity.get() == "":
            #txtTc.get(1.0, END) == "":

        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(txtName.get(),txtAge.get(), txtSurname.get() , txtEmail.get() ,comboGender.get(), txtContact.get(), txtTc.get(), comboCity.get())
            #txtTc.get(1.0, END)

    messagebox.showinfo("Başarılı", "Kayıt Eklendi")
    clearAll()
    dispalyAll()



def update_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtSurname.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtTc.get() == "" or comboCity.get() == "":
            #txtTc.get(1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtName.get(), txtAge.get(), txtSurname.get(), txtEmail.get(), comboGender.get(), txtContact.get(), txtTc.get(), comboCity.get())
             # txtTc.get( 1.0, END))
    messagebox.showinfo("Başarılı", "Kayıt Güncellendi")
    clearAll()
    dispalyAll()


def delete_employee():
    db.remove(row[0])
    clearAll()
    dispalyAll()


def clearAll():
    name.set("")
    age.set("")
    surname.set("")
    gender.set("")
    email.set("")
    contact.set("")
    tc.set("")
    city.set("")
    #txtTc.delete(1.0, END)


btn_frame = Frame(entries_frame, bg="#46244C")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_employee, text="Kaydet", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#F190B7", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_employee, text="Güncelle", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_employee, text="Sil", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Temizle", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)

tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=350, width=1500, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 13),
                rowheight=50)  
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13))  
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8,9), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=2)
tv.heading("2", text="Ad")
tv.column("2", width=2)
tv.heading("3", text="Doğum Tarihi")
tv.column("3", width=2)
tv.heading("4", text="Soyad")
tv.column("4", width=2)
tv.heading("5", text="Email")
tv.column("5", width=3)
tv.heading("6", text="Cinsiyet")
tv.column("6", width=3)
tv.heading("7", text="Telefon")
tv.column("7", width=3)
tv.heading("8", text="TC")
tv.column("8", width=3)
tv.heading("9", text="Memleket")
tv.column("9", width=3)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()
