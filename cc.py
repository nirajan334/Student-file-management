#Project 
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Nepal collage of information technology studedn record")

#Defining What Buttons And Entry Fields Do
def add_student():
    name = name_entry.get()
    age = age_entry.get()
    address = address_entry.get()
    faculty = faculty_entry.get()
    phnumber = ph_number_entry.get()
    student_tree.insert("", tk.END, values=(name,age,address,faculty,phnumber))
    clear_entries()
    
def clear_entries():
    name_entry.delete(0,tk.END)
    age_entry.delete(0,tk.END)
    address_entry.delete(0, tk.END)
    faculty_entry.delete(0, tk.END)
    ph_number_entry.delete(0, tk.END)
    


def save_records_to_file():
    with open ('file2.txt', 'w') as f:
        for item in student_tree.get_children():
            values = student_tree.item(item, 'values')
            f.write(f"Name:{values[0]}, Age:{values[1]}, Address: {values[2]}, Faculty:{values[3]}, Ph_Number:{values[4]}\n")


def update_student():
    selected_item = student_tree.selection()
    if selected_item:
        name = name_entry.get()
        age = age_entry.get()
        address = address_entry.get()
        faculty = faculty_entry.get()
        phnumber = ph_number_entry.get()
        student_tree.item(selected_item, values=(name, age, address,faculty,phnumber))
        clear_entries()
        

def delete_student():
    selected_item = student_tree.selection()
    if selected_item:
        student_tree.delete(selected_item)

#Creating Labels
name_label = tk.Label(root, text="Name", font=('Times New Roman', 12))
age_label = tk.Label(root, text="Age", font=('Times New Roman', 12))
address_label = tk.Label(root, text= "Address", font=('Times New Roman', 12))
faculty_label = tk.Label(root, text="Faculty", font=('Times New Roman', 12))
ph_number_label = tk.Label(root, text="Ph_Number", font=('Times New Roman', 12))
clg_name = tk.Label(root, text="Nepal College of Information And Technology", font=('MS Sans Serif',14))

#Creating Entry Field
name_entry = tk.Entry(root, borderwidth=5, bg='cyan')
age_entry = tk.Entry(root, borderwidth=5, bg='cyan')
address_entry = tk.Entry(root, borderwidth=5, bg='cyan')
faculty_entry = tk.Entry(root, borderwidth=5, bg='cyan')
ph_number_entry = tk.Entry(root, borderwidth=5, bg='cyan')


#Setting up TreeView
columns = ("Name", "Age", "Address", "Faculty", "Ph_Number")
student_tree = ttk.Treeview(root, columns=columns, show="headings")


#defining Column headings
student_tree.heading("Name", text="Name")
student_tree.heading("Age", text="Age")
student_tree.heading("Address", text="Address")
student_tree.heading("Faculty", text="Faculty")
student_tree.heading("Ph_Number", text="Ph_Number")



#Setting column width
student_tree.column("Name", width=200)
student_tree.column("Age", width=50)
student_tree.column("Address", width = 150)
student_tree.column("Faculty", width= 100)
student_tree.column("Ph_Number", width= 100)


#Creating Buttons
add_button = tk.Button(root, text="Add Student", command= add_student, borderwidth=4)
clear_button = tk.Button(root, text = "Clear Entries", command=clear_entries, borderwidth=4)

save_button = tk.Button(root, text="Save Entries", command=save_records_to_file, borderwidth=4)

update_button = tk.Button(root, text="Update Student", command=update_student, borderwidth=4)
delete_button = tk.Button(root, text="Delete Student", command=delete_student, borderwidth=4)

#label grid
clg_name.grid(row = 0,column=0, columnspan=2,pady=20, ipadx=20)
name_label.grid(row=1, column=0, padx=10, pady=5)
age_label.grid(row=2, column=0, padx=10, pady=5)
address_label.grid(row=3, column=0, padx=10, pady=5)
faculty_label.grid(row=4, column=0, padx=10, pady=5)
ph_number_label.grid(row=5, column=0, padx=10, pady=5)

#entry grid
name_entry.grid(row=1, column=1, padx=10, pady=5)
age_entry.grid(row=2, column=1, padx=10, pady=5)
address_entry.grid(row=3, column=1, padx=10, pady=5)
faculty_entry.grid(row=4, column=1, padx=10, pady=5)
ph_number_entry.grid(row=5, column=1, padx=10, pady=5)

#Button grid
add_button.grid(row=6 , column=0, pady=10)
clear_button.grid(row=7, column=1, pady=10)
student_tree.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
update_button.grid(row=6, column=1, pady=10)
delete_button.grid(row=7, column=0, pady=5)
save_button.grid(row=9, column=0, columnspan=2, pady=5)


root.mainloop()