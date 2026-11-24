import os
from connection import get_connection

def insert_student():
    conn = get_connection()

    # object of conn cursor to execute SQL commands
    cursor = conn.cursor()

    name = input("Enter student name: ")
    subject = input("Enter student subject: ")
    score = int(input("Enter student score: "))

    cursor.execute('''
        INSERT INTO STUDENT (name, subject, score)
        VALUES (%s, %s, %s)''', (name, subject, score))

    conn.commit() #save
    print("Student inserted successfully.")

def view_students():
    conn = get_connection()

    cursor = conn.cursor()

    #query = 'SELECT * FROM STUDENT'
    #cursor.execute(query)

    cursor.execute('SELECT * FROM STUDENT')
    conn.commit() #save

    records = cursor.fetchall()

    
    for student in records:
       # print(student)
       print(f"ID: {student[0]}")
       print(f"Name: {student[1]}")
       print(f"Subject: {student[2]}")
       print(f"Score: {student[3]}")
       print("-----------------------------")    

def view_specific_student():
    conn = get_connection()

    cursor = conn.cursor()

    id = int(input("Enter student ID: "))

    query = 'SELECT * FROM STUDENT WHERE id = %s'
    value = (id)

    cursor.execute(query, value)
    #cursor.execute('SELECT * FROM STUDENT WHERE id = %s', (id,))
    conn.commit() #save

    record = cursor.fetchall()
    print(record)

def update_student():
    conn = get_connection()
    cursor = conn.cursor()

    id = int(input("Enter id :"))
    name = input("Enter name :")
    subject = input("Enter subject :")
    score = int(input("Enter score :"))

    query = 'UPDATE STUDENT SET name = %s, subject = %s, score = %s WHERE id = %s'
    value = (name, subject, score, id)

    cursor.execute(query, value)
    conn.commit()

    print("Student updated successfully.")

   # if cursor.rowcount > 0:
   #    print("Student updated successfully.")
   #else:
   #   print("No student found with the given ID.")   

def delete_student():
    conn = get_connection()
    cursor = conn.cursor()

    student_id = int(input("Enter student ID to delete: "))

    query = 'DELETE FROM STUDENT WHERE id = %s'
    #value = (student_id,)

    cursor.execute(query, (student_id,))

    #cursor.execute('DELETE FROM STUDENT WHERE id = %s', (student_id,)) 


    # if cursor.rowcount > 0:
    #   print("Student deleted successfully.")

    #if cursor.rowcount == 0:
    #  print("No student found with the given ID.")

    if cursor.rowcount >= 1:
        print("Student deleted successfully.")

    else:
        print("No student found with the given ID.")    

    conn.commit()

menu = """

    Menu:
    
1. Insert Student
2. View Students    
3. View Specific Student
4. Update Student
5. Delete Student


"""    

status = True

while status:

    print(menu)
    choice = input("Enter your choice: ")

    if choice == '1':
        insert_student()

    elif choice == '2':
        view_students()

    elif choice == '3':
        view_specific_student()    

    elif choice == '4':
        update_student()

    elif choice == '5':
        delete_student()
    else:
        print("Invalid choice. Please try again.")          