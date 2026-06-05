from db import get_connection

def add_marks():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO marks(student_id,subject_id,marks)
        VALUES (%s,%s,%s)
    """, (
        input("Student ID: "),
        input("Subject ID: "),
        input("Marks: ")
    ))

    conn.commit()
    conn.close()
    print("Marks added")


def view_marks():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM marks")
    for i in cur.fetchall():
        print(i)

    conn.close()