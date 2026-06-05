from db import get_connection

def add_student():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO students(name,email,phone,department,year,cgpa,admission_date)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (
        input("Name: "),
        input("Email: "),
        input("Phone: "),
        input("Department: "),
        input("Year: "),
        input("CGPA: "),
        input("Admission Date (YYYY-MM-DD): ")
    ))

    conn.commit()
    conn.close()
    print("Student added")


def view_students():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    for i in cur.fetchall():
        print(i)

    conn.close()


def search_student():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students WHERE student_id=%s",
                (input("Student ID: "),))

    print(cur.fetchone())
    conn.close()


def update_student():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE students
        SET phone=%s, cgpa=%s
        WHERE student_id=%s
    """, (
        input("New Phone: "),
        input("New CGPA: "),
        input("Student ID: ")
    ))

    conn.commit()
    conn.close()
    print("Updated")


def delete_student():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE student_id=%s",
                (input("Student ID: "),))

    conn.commit()
    conn.close()
    print("Deleted")


# ✅ FIXED STUDENT REPORT
def student_report():
    conn = get_connection()
    cur = conn.cursor()

    sid = input("Enter Student ID: ")

    cur.execute("""
        SELECT 
            s.name,
            sub.subject_name,
            m.marks,
            a.date,
            a.status
        FROM students s
        JOIN marks m ON s.student_id = m.student_id
        JOIN subjects sub ON m.subject_id = sub.subject_id
        LEFT JOIN attendance a 
            ON s.student_id = a.student_id 
            AND sub.subject_id = a.subject_id
        WHERE s.student_id = %s
    """, (sid,))

    rows = cur.fetchall()

    if not rows:
        print("No data found")
        return

    print("\n===== STUDENT REPORT =====")
    print("Name:", rows[0][0])

    for r in rows:
        print(f"{r[1]} | Marks: {r[2]} | Date: {r[3]} | Status: {r[4]}")

    conn.close()