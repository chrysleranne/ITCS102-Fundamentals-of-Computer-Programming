import os
print("DLL STUDENT SYSTEM INFORMATION")
print("========================================")

while True:
    print("SELECT FROM FOLLOWING OPTIONS")
    print("A - Add Student")
    print("B - Search Student")
    print("C - Edit Student Info")
    print("D - Delete Student Record")
    print("E - Print All Student Info")
    print("F - Export Data")
    print("G - Exit System")

    choice = input("Input your choice --> ")

    if choice == 'a':
        print("ADD STUDENT RECORD")

        student_id = input("Input Student ID number --> ")
        first_name = input("Input student first name --> ").upper()
        last_name = input("Input student last name --> ")
        course = input("Input student course --> ")
        section = input("Input student section --> ")
        email = ("Input student email --> ")

        stud_record[student_id] = [first_name, last_name, course, section, email ]
        print("DATA SAVED SUCCESFULLY")