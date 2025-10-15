# File: admin_interface.py

import customtkinter as ctk
from tkinter import messagebox
import database_manager as db

class AdminApp(ctk.CTkToplevel):
    """The main window for the Administrator Panel."""
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Administrator Panel")
        self.geometry("850x600")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.selected_course = ctk.StringVar()
        self.question_list = []

        # --- Main Layout Configuration ---
        # The main content area (column 1) will expand, but the sidebar (column 0) will not.
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # --- Sidebar (Left Frame) for Controls ---
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsw")
        self.sidebar_frame.grid_rowconfigure(4, weight=1) # Pushes exit button to the bottom

        self.label_courses = ctk.CTkLabel(self.sidebar_frame, text="Select a Course:", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_courses.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.course_menu = ctk.CTkOptionMenu(self.sidebar_frame, variable=self.selected_course, command=self.load_questions_for_course)
        self.course_menu.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.btn_add_question = ctk.CTkButton(self.sidebar_frame, text="Add New Question", command=self.open_question_form)
        self.btn_add_question.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        
        self.btn_add_course = ctk.CTkButton(self.sidebar_frame, text="Add New Course", command=self.add_new_course)
        self.btn_add_course.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        
        self.btn_exit = ctk.CTkButton(self.sidebar_frame, text="Exit Admin Panel", command=self.on_closing)
        self.btn_exit.grid(row=5, column=0, padx=20, pady=20, sticky="s")


        # --- Main Content Area (Right Frame) for Questions ---
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        self.label_title = ctk.CTkLabel(self, text="Quiz Bowl Content Management", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_title.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

        # Create a scrollable frame to display the questions
        self.scrollable_frame = ctk.CTkScrollableFrame(self.main_frame, label_text="Questions")
        self.scrollable_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        self.load_courses()

    def load_courses(self):
        """Loads course names from the database into the dropdown menu."""
        courses = db.get_course_tables()
        if courses:
            self.course_menu.configure(values=courses)
            self.selected_course.set(courses[0])
            self.load_questions_for_course(courses[0])
        else:
            self.course_menu.configure(values=["No Courses Found"])
            self.selected_course.set("No Courses Found")
            # Clear any existing questions from the view
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()
            
    def add_new_course(self):
        """Opens a dialog to get a new course name and creates a table for it."""
        dialog = ctk.CTkInputDialog(text="Enter the name for the new course (e.g., 'MATH_101'):", title="Add New Course")
        new_course_name = dialog.get_input()
        
        # Check if the user provided a name and it's not already in the list
        if new_course_name and new_course_name not in self.course_menu.cget("values"):
            # The create_table_if_not_exists function in the DB manager will handle creation
            conn = db.connect_db()
            cursor = conn.cursor()
            db.create_table_if_not_exists(cursor, new_course_name)
            conn.close()
            
            messagebox.showinfo("Success", f"Course '{new_course_name}' added successfully.")
            self.load_courses() # Refresh the course list in the dropdown
        elif new_course_name:
            messagebox.showwarning("Duplicate", "A course with this name already exists.")

    def load_questions_for_course(self, course_name):
        """Fetches and displays all questions for the selected course."""
        # Clear any widgets currently in the scrollable frame
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        self.question_list = db.get_questions(course_name)

        if not self.question_list:
            no_q_label = ctk.CTkLabel(self.scrollable_frame, text="No questions found for this course.", font=ctk.CTkFont(size=14))
            no_q_label.pack(pady=20)
            return

        for i, question_row in enumerate(self.question_list):
            question = dict(question_row) # Convert the sqlite3.Row object to a dictionary
            q_id = question['id']
            q_text = question['question_text']
            
            # A frame for each question to hold the text and buttons
            q_frame = ctk.CTkFrame(self.scrollable_frame, fg_color=("gray85", "gray17"))
            q_frame.pack(fill="x", pady=5, padx=5)
            q_frame.grid_columnconfigure(0, weight=1)
            
            q_label = ctk.CTkLabel(q_frame, text=f"{i+1}. {q_text}", wraplength=500, justify="left")
            q_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
            
            btn_frame = ctk.CTkFrame(q_frame, fg_color="transparent")
            btn_frame.grid(row=0, column=1, padx=10, pady=5, sticky="e")

            edit_btn = ctk.CTkButton(btn_frame, text="Edit", width=60, command=lambda q=question: self.open_question_form(q))
            edit_btn.pack(side="left", padx=5)

            delete_btn = ctk.CTkButton(btn_frame, text="Delete", width=60, fg_color="#D32F2F", hover_color="#B71C1C", command=lambda q_id=q_id: self.delete_question(q_id))
            delete_btn.pack(side="left", padx=5)

    def open_question_form(self, question=None):
        """Opens the QuestionForm window to add a new question or edit an existing one."""
        if self.selected_course.get() == "No Courses Found":
            messagebox.showerror("Error", "Please add a course before adding questions.")
            return
        form_window = QuestionForm(self, question, self.selected_course.get())
        form_window.grab_set() # Make the form modal (disables interaction with the main admin window)

    def delete_question(self, question_id):
        """Deletes a question after user confirmation."""
        course = self.selected_course.get()
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to permanently delete this question?"):
            db.delete_question(course, question_id)
            messagebox.showinfo("Success", "Question deleted successfully.")
            self.load_questions_for_course(course) # Refresh the view

    def on_closing(self):
        """Handles the window closing event by showing the main login window again."""
        self.master.deiconify() # Re-shows the main login window
        self.destroy()

class QuestionForm(ctk.CTkToplevel):
    """A form window for adding or editing questions."""
    def __init__(self, master, question_data=None, course_name=None):
        super().__init__(master)
        self.master_app = master
        self.question_data = question_data
        self.course_name = course_name

        self.title("Edit Question" if question_data else "Add New Question")
        self.geometry("500x500")
        
        # --- Form Fields ---
        self.entries = {}
        fields = ["Question Text", "Option A", "Option B", "Option C", "Option D"]
        
        for i, field in enumerate(fields):
            label = ctk.CTkLabel(self, text=field + ":")
            label.grid(row=i, column=0, padx=20, pady=10, sticky="w")
            entry = ctk.CTkEntry(self, width=300)
            entry.grid(row=i, column=1, padx=20, pady=10, sticky="ew")
            self.entries[field.replace(" ", "_").lower()] = entry

        # --- Correct Answer Radio Buttons ---
        self.correct_answer_var = ctk.StringVar(value='A')
        correct_answer_label = ctk.CTkLabel(self, text="Correct Answer:")
        correct_answer_label.grid(row=len(fields), column=0, padx=20, pady=10, sticky="w")
        
        radio_frame = ctk.CTkFrame(self)
        radio_frame.grid(row=len(fields), column=1, padx=20, pady=10, sticky="w")
        
        options = ['A', 'B', 'C', 'D']
        for option in options:
            radio = ctk.CTkRadioButton(radio_frame, text=option, variable=self.correct_answer_var, value=option)
            radio.pack(side="left", padx=10)

        # If editing, populate the form fields with existing data
        if self.question_data:
            self.populate_form()
            
        # --- Save Button ---
        self.btn_save = ctk.CTkButton(self, text="Save Question", command=self.save_question)
        self.btn_save.grid(row=len(fields)+1, column=0, columnspan=2, padx=20, pady=20, sticky="ew")
        
    def populate_form(self):
        """Fills the form fields with data from an existing question for editing."""
        self.entries["question_text"].insert(0, self.question_data['question_text'])
        self.entries["option_a"].insert(0, self.question_data['option_a'])
        self.entries["option_b"].insert(0, self.question_data['option_b'])
        self.entries["option_c"].insert(0, self.question_data['option_c'])
        self.entries["option_d"].insert(0, self.question_data['option_d'])
        self.correct_answer_var.set(self.question_data['correct_answer'])

    def save_question(self):
        """Validates input, gathers data, and calls the appropriate database function."""
        data = {
            'question_text': self.entries["question_text"].get(),
            'option_a': self.entries["option_a"].get(),
            'option_b': self.entries["option_b"].get(),
            'option_c': self.entries["option_c"].get(),
            'option_d': self.entries["option_d"].get(),
            'correct_answer': self.correct_answer_var.get()
        }

        # Basic validation to ensure no fields are empty
        for key, value in data.items():
            if not value.strip():
                messagebox.showerror("Input Error", f"Field '{key.replace('_', ' ').title()}' cannot be empty.")
                return

        try:
            if self.question_data: # Editing an existing question
                question_id = self.question_data['id']
                db.update_question(self.course_name, question_id, data)
                messagebox.showinfo("Success", "Question updated successfully.")
            else: # Adding a new question
                db.add_question(self.course_name, data)
                messagebox.showinfo("Success", "Question added successfully.")
            
            self.master_app.load_questions_for_course(self.course_name) # Refresh the main view
            self.destroy() # Close the form
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred while saving: {e}")