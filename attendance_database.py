import sqlite3
from datetime import datetime
import os

DB_PATH = "attendance.db"


def initialize_database():
    """Ensures the attendance table is created properly in the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create the table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            subject TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ Database and table verified successfully!")


def mark_attendance(name, subject):
    """Records attendance for a recognized face with the subject."""
    initialize_database()  # Ensure database and table exist

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    # Check if attendance is already marked for the same student, date, and subject
    cursor.execute("SELECT * FROM attendance WHERE name=? AND date=? AND subject=?", (name, date, subject))

    if cursor.fetchone() is None:  # If no entry found, insert new record
        cursor.execute("INSERT INTO attendance (name, date, time, subject) VALUES (?, ?, ?, ?)",
                       (name, date, time, subject))
        conn.commit()
        print(f"✅ Attendance marked for {name} - {subject} at {time}")
    else:
        print(f"⚠️ Attendance already recorded for {name} in {subject} class.")

    conn.close()


def fetch_attendance():
    """Retrieves and displays all attendance records."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance")
    records = cursor.fetchall()

    if records:
        print("\n📋 Attendance Records:")
        for row in records:
            print(row)
    else:
        print("❌ No attendance records found.")

    conn.close()


if __name__ == "__main__":
    initialize_database()
    fetch_attendance()  # Optional: Display attendance records
