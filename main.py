from student import *
from attendance import *
from marks import *

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Mark Attendance")
    print("7. View Attendance")
    print("8. Add Marks")
    print("9. View Marks")
    print("10. Student Report")
    print("11. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        mark_attendance()
    elif choice == "7":
        view_attendance()
    elif choice == "8":
        add_marks()
    elif choice == "9":
        view_marks()
    elif choice == "10":
        student_report()
    elif choice == "11":
        break
    else:
        print("Invalid choice")