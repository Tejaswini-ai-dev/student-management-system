import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="Tejasvee",
        password="Teja@1234",
        database="student_management"
    )