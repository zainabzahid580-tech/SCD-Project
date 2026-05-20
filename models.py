# Refactored from legacy single-file code
from db import get_connection

class Student:
    def __init__(self, name, math, english, science, id=None):
        self.id = id
        self.name = name
        self.math = float(math)
        self.english = float(english)
        self.science = float(science)
        
        if self.math < 0 or self.english < 0 or self.science < 0:
            raise ValueError("Marks cannot be negative")
        if self.math > 100 or self.english > 100 or self.science > 100:
            raise ValueError("Marks cannot be above 100")

    def calculate_total(self):
        return self.math + self.english + self.science

    def calculate_average(self):
        return self.calculate_total() / 3.0

    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        total = self.calculate_total()
        average = self.calculate_average()
        grade = self.calculate_grade()
        cursor.execute('''
            INSERT INTO students (name, math, english, science, total, average, grade)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (self.name, self.math, self.english, self.science, total, average, grade))
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()
        return self.id

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def delete(student_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        conn.commit()
        conn.close()
