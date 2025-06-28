#student management system

import mysql.connector as mc
mydb=mc.connect(host='localhost',user='root',passwd='',database='student_details')
my_cursor=mydb.cursor()

#create class :

def create_class():
    table_name=input("Enter the class name : ")
    num_of_column=int(input("Enter the no. of columns : "))

    columns=[]

    for i in range(num_of_column):
       col_name=input("Enter the name of the column : ")
       col_type=input("Enter the type of the column : ")
       columns.append(col_name + " " + col_type)

    full_col=','.join(columns) #joining all columns to the table

    query1 = "CREATE TABLE IF NOT EXISTS '" + table_name + "' (" + full_col + ")"
    my_cursor.execute(query1)
    mydb.commit()
    print("Class created successfully.")
    
#delete(drop) class(table) :

def delete_class():
    table_name=input("Enter the class name : ")
    query2="DROP TABLE '"+ table_name

    my_cursor.execute(query2)
    mydb.commit()
    print("Class  details deleted successfully.")

#modify class :

def modify_class():
    table_name = input("Enter the class (table) name to modify: ")
    
    print("\nWhat would you like to do?")
    print("1. Add a new column")
    print("2. Remove a column")
    print("3. Rename a column")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        col_name = input("Enter the name of the new column: ")
        col_type = input("Enter the data type of the new column (e.g., VARCHAR(50), INT): ")
        query = "ALTER TABLE `" + table_name + "` ADD COLUMN " + col_name + " " + col_type

    elif choice == '2':
        col_name = input("Enter the name of the column to remove: ")
        query = "ALTER TABLE `" + table_name + "` DROP COLUMN " + col_name

    elif choice == '3':
        old_name = input("Enter the current column name: ")
        new_name = input("Enter the new column name: ")
        new_type = input("Enter the data type (same or updated): ")
        query = "ALTER TABLE `" + table_name + "` CHANGE COLUMN " + old_name + " " + new_name + " " + new_type

    else:
        print("Invalid choice!")
        return

    try:
        my_cursor.execute(query)
        mydb.commit()
        print("Table modified successfully.")
    except mc.Error as err:
        print("Error:", err)


#view classes :

def view_classes():
    query3='SHOW TABLES IN student_details ;'
    my_cursor.execute(query3)
    result = my_cursor.fetchall()
    print("\n   List of classes:")
    print("________________________")
    if result:
        for table in result:
          print(table[0])
    else:
        print("\n***  No classes(tables) in the database  ***")

 

#add student :

def add_student():
    table_name = input("Enter the table name to insert data into: ")

    my_cursor.execute('DESCRIBE '+ table_name)
    col_info=my_cursor.fetchall()

    columns=[]
    values=[]

    for col in col_info:
     col_name = col[0]
     col_type = col[1]
     is_nullable = col[2]
     is_key = col[3]
     default_value = col[4]
     extra = col[5]

     if "auto_increment" in extra:
        continue  # Skip auto-increment columns like 'id'

     user_input = input("Enter value for '" + col_name + "' (" + col_type + "): ")
     columns.append(col_name)
     values.append(user_input)

    values_str = ", ".join(["%s"] * len(values))
    columns_str = ", ".join(columns)
    query4 = "INSERT INTO '" + table_name + "' (" + columns_str + ") VALUES (" + values_str + ")"

    my_cursor.execute(query4,values)
    mydb.commit()
    print("Student details added successfully.")
    

#delete student :

def delete_student():
    table_name = input("Enter the table name to delete data from: ")
    admition_no=input("Enter the admition no. of student to be deleted : ")
    query5="DELETE FROM '"+ table_name +"' WHERE  admition_no=%s"

    my_cursor.execute(query5,(admition_no,))
    mydb.commit()
    print("Student  details deleted successfully.")
    

#update student :

def update_student():
    table_name=input("Enter the name of the table ")
    
    my_cursor.execute("DESCRIBE " + table_name)
    columns_info = my_cursor.fetchall()
    for i in columns_info:
        print(i)

    column = input("Enter the column name to update: ")
    admition_no = input("Enter the admission number of the student: ")
    new_value = input("Enter the new value: ")

    query6 = "UPDATE '" + table_name + "' SET " + column + " = %s WHERE admition_no = %s"
    my_cursor.execute(query6, (new_value, admition_no))
    mydb.commit()
    print("Student details updated successfully.")

#view student details :
def view_student():
    table_name=input("Enter the table name : ")
    query7="SELECT * FROM '"+ table_name
    my_cursor.execute(query7)

    result=my_cursor.fetchall()

    if result:
        print("\n                    Student Records                   ")
        print("________________________________________________________")
        for row in result:
            print(row)
    else:
        print("\n***  No student exist with the these info  ***")


#search student details :

def search_student():
    table_name=input("Enter the table name : ")
    admition_no=input("Enter the admiiton no. of the student :")

    query8 ="SELECT * FROM '"+ table_name +"' WHERE admition_no = %s"
    my_cursor.execute(query8,(admition_no,))

    result=my_cursor.fetchone()

    if result:
        print("Student details : \n",result)
    else:
        print("\n***  No student exist with the these info  ***")

    

while (True):
    print(" _____________________________________ ")
    print("|      STUDENT MANAGEMENT SYSTEM      |")
    print("|_____________________________________|")
    print('|_____________________________________|')
    print('|   1 . CREATE CLASS                  |')
    print('|   2 . DELETE CLASS                  |')
    print('|   3 . MODIFY CLASS                  |')
    print('|   4 . VIEW CLASS DETAILS            |')
    print('|   5 . ADD  STUDENT DETAILS          |')
    print('|   6 . DELETE  STUDENT DETAILS       |')
    print('|   7 . UPDATE  STUDENT DETAILS       |')
    print('|   8 . VIEW  STUDENT DETAILS         |')
    print('|   9 . SEARCH  STUDENT DETAILs       |')
    print('|   10. EXIT                          |')
    print('|_____________________________________|')

    choice=int(input("\nEnter your choice : "))


    if(choice == 1):
        create_class()
    elif(choice == 2):
        delete_class()
    elif(choice == 3):
        modify_class()
    elif(choice == 4):
        view_classes()
    elif(choice == 5):
        add_student()
    elif(choice == 6):
        delete_student()
    elif(choice == 7):
        update_student()
    elif(choice == 8):
        view_student()
    elif(choice == 9):
        search_student()
    elif(choice == 10):
        print("EXITING")
        break
    else:
        print("Invalid choice !!")

mydb.close()
