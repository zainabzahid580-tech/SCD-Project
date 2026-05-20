# Refactored from legacy single-file code
import tkinter as tk
from tkinter import ttk, messagebox

class StudentAppView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Student Grade Calculator")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Math Marks:").grid(row=1, column=0, padx=5, pady=5)
        self.math_entry = tk.Entry(input_frame)
        self.math_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="English Marks:").grid(row=2, column=0, padx=5, pady=5)
        self.english_entry = tk.Entry(input_frame)
        self.english_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Science Marks:").grid(row=3, column=0, padx=5, pady=5)
        self.science_entry = tk.Entry(input_frame)
        self.science_entry.grid(row=3, column=1, padx=5, pady=5)

        add_btn = tk.Button(input_frame, text="Add Student", command=self.controller.add_student)
        add_btn.grid(row=4, column=0, columnspan=2, pady=10)

        columns = ('id', 'name', 'math', 'english', 'science', 'total', 'average', 'grade')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=90)
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        delete_btn = tk.Button(self, text="Delete Selected", command=self.controller.delete_student)
        delete_btn.pack(pady=5)

        self.highest_scorer_label = tk.Label(self, text="Highest Scorer: N/A", font=("Arial", 12, "bold"))
        self.highest_scorer_label.pack(pady=10)

    def get_inputs(self):
        return {
            'name': self.name_entry.get(),
            'math': self.math_entry.get(),
            'english': self.english_entry.get(),
            'science': self.science_entry.get()
        }

    def clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        self.math_entry.delete(0, tk.END)
        self.english_entry.delete(0, tk.END)
        self.science_entry.delete(0, tk.END)

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def show_info(self, message):
        messagebox.showinfo("Success", message)

    def populate_tree(self, rows):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in rows:
            self.tree.insert('', tk.END, values=row)

    def update_highest_scorer(self, text):
        self.highest_scorer_label.config(text=text)

    def get_selected_student_id(self):
        selected = self.tree.selection()
        if not selected:
            return None
        item = self.tree.item(selected[0])
        return item['values'][0]
