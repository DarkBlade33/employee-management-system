from tkinter import ttk, messagebox
import tkinter as tk
from tkinter.font import BOLD
from databaseMod import databaseClass


db = databaseClass("employeeData.db")

root = tk.Tk()
root.title("Employee Management System")
root.config(bg="#B0C4DE")
root.state("zoomed")

 
idVar = tk.StringVar()
nameVar = tk.StringVar() 
emailVar = tk.StringVar()
phoneVar = tk.StringVar()  


# mainFrame covers entire window 

mainFrame = tk.Frame(root, bg = "#B0C4DE")
mainFrame.pack(expand="True", fill="both")

mainFrame.rowconfigure(0, weight=1)
mainFrame.rowconfigure(1, weight=1)
mainFrame.rowconfigure(2, weight=1)
mainFrame.rowconfigure(3, weight=1)

mainFrame.columnconfigure(0, weight=1)

heading = tk.Label(mainFrame, text = "Employee Management System", font=("Times New Roman", 20, "bold","underline"), bg = "#B0C4DE")
heading.grid(row=0)


# data entry frame

entryFrame = tk.Frame(mainFrame, bg = "#B0C4DE")
entryFrame.grid(row=1)

id = tk.Label(entryFrame, text = "ID : ", font=("Calibri", 16, "bold"), bg = "#B0C4DE")
id.grid(row=0, column=0, sticky="e")

txtid = tk.Entry(entryFrame, textvariable=idVar, font=("Calibri", 16), width=25)
txtid.grid(row=0, column=1, padx=10, pady=10, sticky="w")

name = tk.Label(entryFrame, text = "Name : ", font=("Calibri", 16, "bold"), bg = "#B0C4DE")
name.grid(row=0, column=2, sticky="e")

txtname = tk.Entry(entryFrame, textvariable=nameVar, font=("Calibri", 16), width=25)
txtname.grid(row=0, column=3, padx=10, pady=10, sticky="w")

email = tk.Label(entryFrame, text = "Email : ", font=("Calibri", 16, "bold"), bg = "#B0C4DE")
email.grid(row=1, column=0, sticky="e")

txtemail = tk.Entry(entryFrame, textvariable=emailVar, font=("Calibri", 16), width=25)
txtemail.grid(row=1, column=1, padx=10, pady=10, sticky="w")

phone = tk.Label(entryFrame, text = "Phone number : ", font=("Calibri", 16, "bold"), bg = "#B0C4DE")
phone.grid(row=1, column=2, sticky="e")

txtphone = tk.Entry(entryFrame, textvariable=phoneVar, font=("Calibri", 16), width=25)
txtphone.grid(row=1, column=3, padx=10, pady=10, sticky="w")


# Functions 

def clear_tv_table():
    """Clear all the data that was previously present in the data display table (treeview widget)"""
    for item in table.get_children():
      table.delete(item) 

def clear_entries():
    """Clears all the entered data"""
    idVar.set("")
    nameVar.set("") 
    emailVar.set("")
    phoneVar.set("")

def get_record(event):
    """Gets the data from the particular row selected in table"""
    selected_row = table.focus()
    global rowData
    rowData = table.item(selected_row, "values")
    global id1 
    id1 = int(rowData[0])
    idVar.set(rowData[0])
    nameVar.set(rowData[1]) 
    emailVar.set(rowData[2])
    phoneVar.set(rowData[3])

def get_data():
    """Gets all the data from the database and adds it to the data display table"""
    for row in db.fetch():
        table.insert(parent="", index="end", value=row)

def add_employee():
    if idVar.get() == "" or nameVar.get() == "" or emailVar.get() == "" or phoneVar.get() == "" :
        messagebox.showerror(title = "Error", message = "Enter complete details")
    else:
        db.insert(int(idVar.get()), nameVar.get(), emailVar.get(), int(phoneVar.get()))
    clear_entries()
    clear_tv_table()
    get_data()
    messagebox.showinfo(title = "Messsage", message = "Employee added successfully")
    
def del_employee():
    db.delete(int(rowData[0]))
    clear_entries()
    clear_tv_table()
    get_data()

def update():
    if table.focus():
        if idVar.get() == "" or nameVar.get() == "" or emailVar.get() == "" or phoneVar.get() == "" :
            messagebox.showerror(title = "Error", message = "Enter complete details")
            
        else:
            db.update(int(idVar.get()), nameVar.get(), emailVar.get(), int(phoneVar.get()), id1)
        clear_entries()
        clear_tv_table()
        get_data()
    else:
        messagebox.showerror(title = "Error", message = "Select record to update first")


#buttons frame

buttonFrame = tk.Frame(mainFrame, bg = "#B0C4DE")
buttonFrame.grid(row=2)

buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

addButton = tk.Button(buttonFrame, text="Add new employee", font=("Calibri", 16,BOLD), width=20, bg="black", fg="white", command=add_employee)
addButton.grid(row=0, column=0, padx=10, pady=10)

delButton = tk.Button(buttonFrame, text="Delete employee", font=("Calibri", 16,"bold"), width=20, bg="black", fg="white", command=del_employee)
delButton.grid(row=0, column=1, padx=10, pady=10)

updateButton = tk.Button(buttonFrame, text="Update details", font=("Calibri", 16, "bold"), width=20, bg="black", fg="white", command=update)
updateButton.grid(row=0, column=2, padx=10, pady=10)


# data display table

tableFrame = tk.Frame(mainFrame)
tableFrame.grid(row=3)

# making a scrollbar

tableScrollbar = tk.Scrollbar(tableFrame)
tableScrollbar.pack(side="right", fill="y")

table = ttk.Treeview(tableFrame, columns=(1,2,3,4), show="headings", yscrollcommand=tableScrollbar.set) 

tableScrollbar.configure(command=table.yview)

table.heading(1, text = "ID")
table.heading(2, text = "Name")
table.heading(3, text = "Email")
table.heading(4, text = "Phone no.")

table.column(1, width ="50", anchor="center")
table.column(2, width ="110", anchor="w")
table.column(3, width ="180", anchor="w")
table.column(4, width ="130", anchor="w")

tableStyle = ttk.Style(table)
tableStyle.theme_use('clam')
tableStyle.configure("Treeview", rowheight = 40, font=14)

table.bind("<ButtonRelease-1>", get_record)
table.pack()

clear_tv_table()
get_data()


root.mainloop()
