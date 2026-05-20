# Student Grade Calculator

A simple, beginner-friendly desktop application built with Python, Tkinter, and SQLite. This application allows users to enter student marks, calculate their total, average, and grade, and store the records in a database.

## System Evolution (Lehman's Law)
This application represents an E-type system according to Lehman's Laws of Software Evolution. It operates in a real-world environment and must be continually adapted to remain useful. As educational grading policies change, or if new subjects are added to the curriculum, this software will need to evolve and be updated to satisfy the new requirements.

## Features
- Enter student name and marks for Math, English, and Science.
- Automatically calculates total, average, and letter grade (A/B/C/D/F).
- View all students in a data table.
- View the highest scorer dynamically.
- Delete student records.
- Exception handling for invalid inputs.

## Prerequisites
- Python 3.x
- No external libraries are required (Tkinter and SQLite3 are built-in).

## How to Run
1. Clone or download the repository.
2. Open a terminal and navigate to the `StudentGradeCalculator` directory.
3. Run the application using the following command:
   ```bash
   python main.py
   ```

## How to Run Tests
To automatically run all unit tests, execute:
```bash
python run_tests.py
```
