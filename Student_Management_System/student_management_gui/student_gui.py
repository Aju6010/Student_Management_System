#student management system with Tkinter frontend
import mysql.connector as mc
import tkinter as tk
from tkinter import messagebox, simpledialog

# MySQL Connection
mydb = mc.connect(host='localhost', user='root', passwd='', database='student_details')
my_cursor = mydb.cursor()

# GUI setup
root = tk.Tk()
root.title("Student Management System")
root.geometry("400x500")

def create_class():
    table_name = simpledialog.askstring("Input", "Enter class name:")
    num_cols = simpledialog.askinteger("Input", "Enter number of columns:")

    columns = []
    for _ in range(num_cols):
        col_name = simpledialog.askstring("Column", "Enter column name:")
        col_type = simpledialog.askstring("Type", "Enter column type (e.g., VARCHAR(50), INT):")
        columns.append(col_name + " " + col_type)

    full_col = ', '.join(columns)
    query = "CREATE TABLE IF NOT EXISTS `" + table_name + "` (" + full_col + ")"
    try:
        my_cursor.execute(query)
        mydb.commit()
        messagebox.showinfo("Success", "Class created successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_class():
    table_name = simpledialog.askstring("Input", "Enter class name to delete:")
    query = "DROP TABLE `" + table_name + "`"
    try:
        my_cursor.execute(query)
        mydb.commit()
        messagebox.showinfo("Success", "Class deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def modify_class():
    table_name = simpledialog.askstring("Input", "Enter table name to modify:")
    choice = simpledialog.askinteger("Modify", "1. Add Column\n2. Drop Column\n3. Rename Column")

    if choice == 1:
        col = simpledialog.askstring("New Column", "Enter column name:")
        col_type = simpledialog.askstring("Type", "Enter column type:")
        query = "ALTER TABLE `" + table_name + "` ADD COLUMN " + col + " " + col_type
    elif choice == 2:
        col = simpledialog.askstring("Column", "Enter column to drop:")
        query = "ALTER TABLE `" + table_name + "` DROP COLUMN " + col
    elif choice == 3:
        old = simpledialog.askstring("Old Column", "Enter current column name:")
        new = simpledialog.askstring("New Column", "Enter new column name:")
        typ = simpledialog.askstring("Type", "Enter column type:")
        query = "ALTER TABLE `" + table_name + "` CHANGE COLUMN " + old + " " + new + " " + typ
    else:
        return

    try:
        my_cursor.execute(query)
        mydb.commit()
        messagebox.showinfo("Success", "Table modified.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def view_classes():
    query = "SHOW TABLES"
    my_cursor.execute(query)
    tables = my_cursor.fetchall()
    result = "\n".join([table[0] for table in tables])
    messagebox.showinfo("Tables", result if result else "No classes found.")

def add_student():
    table = simpledialog.askstring("Table", "Enter table name:")
    my_cursor.execute("DESCRIBE " + table)
    cols = my_cursor.fetchall()

    col_names = []
    values = []
    for col in cols:
        if "auto_increment" in col[5]:
            continue
        val = simpledialog.askstring("Input", f"Enter {col[0]} ({col[1]}):")
        col_names.append(col[0])
        values.append(val)

    col_str = ", ".join(col_names)
    val_str = ", ".join(["%s"] * len(values))
    query = "INSERT INTO `" + table + "` (" + col_str + ") VALUES (" + val_str + ")"
    try:
        my_cursor.execute(query, tuple(values))
        mydb.commit()
        messagebox.showinfo("Success", "Student added.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_student():
    table = simpledialog.askstring("Table", "Enter table name:")
    adm_no = simpledialog.askstring("Admission No", "Enter admission number:")
    query = "DELETE FROM `" + table + "` WHERE admition_no = %s"
    try:
        my_cursor.execute(query, (adm_no,))
        mydb.commit()
        messagebox.showinfo("Success", "Student deleted.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_student():
    table = simpledialog.askstring("Table", "Enter table name:")
    my_cursor.execute("DESCRIBE " + table)
    cols = my_cursor.fetchall()
    cols = [col[0] for col in cols]
    column = simpledialog.askstring("Column", f"Available columns: {cols}\nEnter column to update:")
    adm_no = simpledialog.askstring("Admission No", "Enter admission number:")
    new_val = simpledialog.askstring("New Value", "Enter new value:")
    query = "UPDATE `" + table + "` SET " + column + " = %s WHERE admition_no = %s"
    try:
        my_cursor.execute(query, (new_val, adm_no))
        mydb.commit()
        messagebox.showinfo("Success", "Student updated.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def view_student():
    table = simpledialog.askstring("Table", "Enter table name:")
    query = "SELECT * FROM `" + table + "`"
    try:
        my_cursor.execute(query)
        rows = my_cursor.fetchall()
        msg = "\n".join(str(row) for row in rows)
        messagebox.showinfo("Student Details", msg if msg else "No records found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_student():
    table = simpledialog.askstring("Table", "Enter table name:")
    adm_no = simpledialog.askstring("Admission No", "Enter admission number:")
    query = "SELECT * FROM `" + table + "` WHERE admition_no = %s"
    try:
        my_cursor.execute(query, (adm_no,))
        row = my_cursor.fetchone()
        messagebox.showinfo("Result", str(row) if row else "Student not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Buttons
buttons = [
    ("Create Class", create_class),
    ("Delete Class", delete_class),
    ("Modify Class", modify_class),
    ("View Classes", view_classes),
    ("Add Student", add_student),
    ("Delete Student", delete_student),
    ("Update Student", update_student),
    ("View Students", view_student),
    ("Search Student", search_student),
    ("Exit", root.quit)
]

for (text, command) in buttons:
    tk.Button(root, text=text, width=30, height=2, command=command).pack(pady=5)

root.mainloop()
mydb.close()

