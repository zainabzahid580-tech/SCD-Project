import unittest
import sqlite3
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import Student
from db import init_db

class TestStudentModel(unittest.TestCase):
    def setUp(self):
        init_db()
        conn = sqlite3.connect('grades.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM students')
        conn.commit()
        conn.close()

    def test_adding_student(self):
        student = Student("John Doe", 90, 80, 70)
        student_id = student.save()
        self.assertIsNotNone(student_id)
        
        rows = Student.get_all()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1], "John Doe")

    def test_deleting_student(self):
        student = Student("Jane Doe", 90, 90, 90)
        student_id = student.save()
        
        Student.delete(student_id)
        rows = Student.get_all()
        self.assertEqual(len(rows), 0)

    def test_grade_calculation(self):
        student_b = Student("User B", 85, 85, 85)
        self.assertEqual(student_b.calculate_grade(), 'B')
        
        student_a = Student("User A", 95, 95, 95)
        self.assertEqual(student_a.calculate_grade(), 'A')

    def test_invalid_marks(self):
        with self.assertRaises(ValueError):
            Student("Test", -5, 50, 50)
            
        with self.assertRaises(ValueError):
            Student("Test", 105, 50, 50)

    def test_getting_all_students(self):
        Student("Student 1", 50, 50, 50).save()
        Student("Student 2", 60, 60, 60).save()
        
        rows = Student.get_all()
        self.assertEqual(len(rows), 2)

if __name__ == '__main__':
    unittest.main()
