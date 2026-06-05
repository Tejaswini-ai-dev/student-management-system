from db import get_connection

def mark_attendance():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO attendance(student_id,subject_id,date,status)
        VALUES (%s,%s,%s,%s)
    """, (
        input("Student ID: "),
        input("Subject ID: "),
        input("Date (YYYY-MM-DD): "),
        input("Status (Present/Absent): ")
    ))

    conn.commit()
    conn.close()
    print("Attendance marked")


def view_attendance():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM attendance")
    for i in cur.fetchall():
        print(i)

    conn.close()