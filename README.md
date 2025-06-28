# Student Management System

A project by **Aju Eldo**

## 📌 Overview

- A Python + MySQL-based system to manage student data.
- Comes with **two versions**:
  - **CLI Version**: Command-line based using text input.
  - **GUI Version**: Built with Tkinter for a user-friendly interface.
- The database used is **`student_details`**, and all operations are stored in real MySQL tables.

## 🛠 Features

- **Dynamic Table Management**:
  - Create user-defined tables (classes) with custom column names and types.
  - Modify existing tables by adding, renaming, or removing columns.
  - Delete entire class tables if no longer needed.

- **Student Data Management**:
  - Add new student records with full details.
  - Update existing student information.
  - Delete student records using admission number.
  - View all student records in a table.
  - Search for a specific student by admission number.

- **Extensible Design**:
  - Not limited to student management — can be extended to employees, products, etc.
  - Table and column names are completely user-defined.

## 📁 Project Structure

Student-Management-System/
│
├── cli-version/
│ └── student_cli.py
│ └── README.md
│
├── gui-version/
│ └── student_gui.py
│ └── README.md
│
└── README.md (this file)

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Install dependencies:
   ```bash
   pip install mysql-connector-python tk
3. Ensure MySQL server is running and the student_details database exists.
4. Run either:
    CLI: python student_cli.py
    GUI: python student_gui.py

## 🌱 Future Possibilities

- Add login/authentication.
- Generate printable reports (e.g., marksheets).
- Extend for employee or inventory management.
- Build a web version using Flask or Django.
