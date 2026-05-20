# Refactored from legacy single-file code
import sqlite3
from models import Student

class AppController:
    def __init__(self):
        self.view = None

    def set_view(self, view):
        self.view = view
        self.refresh_data()

    def add_student(self):
        inputs = self.view.get_inputs()
        name = inputs['name'].strip()
        math_str = inputs['math']
        english_str = inputs['english']
        science_str = inputs['science']

        if not name:
            self.view.show_error("Name cannot be empty.")
            return

        try:
            student = Student(name, math_str, english_str, science_str)
            student.save()
            self.view.show_info("Student added successfully!")
            self.view.clear_inputs()
            self.refresh_data()
        except ValueError as e:
            if "could not convert" in str(e).lower() or "invalid literal" in str(e).lower():
                self.view.show_error("Marks must be valid numbers (no letters).")
            else:
                self.view.show_error(str(e))
        except sqlite3.Error as e:
            self.view.show_error(f"Database error: {e}")
        except Exception as e:
            self.view.show_error(f"An unexpected error occurred: {e}")

    def delete_student(self):
        student_id = self.view.get_selected_student_id()
        if student_id is None:
            self.view.show_error("Please select a student to delete.")
            return
        
        try:
            Student.delete(student_id)
            self.view.show_info("Student deleted successfully!")
            self.refresh_data()
        except sqlite3.Error as e:
            self.view.show_error(f"Database error: {e}")

    def refresh_data(self):
        try:
            rows = Student.get_all()
            self.view.populate_tree(rows)
            
            if rows:
                highest_scorer = max(rows, key=lambda x: x[6])
                self.view.update_highest_scorer(f"Highest Scorer: {highest_scorer[1]} ({highest_scorer[6]:.2f})")
            else:
                self.view.update_highest_scorer("Highest Scorer: N/A")
        except sqlite3.Error as e:
            self.view.show_error(f"Database error: {e}")
