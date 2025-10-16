# File: student_interface.py

import customtkinter as ctk
import database_manager as db
import random

class StudentWelcomeScreen(ctk.CTkToplevel):
    """The initial screen for students to select which quiz they want to take."""
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Welcome, Student!")
        self.geometry("400x300")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.label_welcome = ctk.CTkLabel(self, text="Select a Quiz to Begin", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_welcome.pack(pady=20)

        self.course_menu = ctk.CTkOptionMenu(self, values=["Loading courses..."], command=self.course_selected)
        self.course_menu.pack(pady=10, padx=40, fill="x")

        self.btn_start = ctk.CTkButton(self, text="Start Quiz", command=self.start_quiz, state="disabled")
        self.btn_start.pack(pady=20)
        
        self.btn_back = ctk.CTkButton(self, text="Back to Login", command=self.on_closing)
        self.btn_back.pack(pady=10)

        self.load_courses()

    def load_courses(self):
        """Fetches course names from the database and populates the dropdown menu."""
        courses = db.get_course_tables()
        if courses:
            # The dropdown will show user-friendly names, not the raw table names.
            # Example: "MKT_3400_500" becomes "MKT 3400 500"
            formatted_courses = [c.replace('_', ' ') for c in courses]
            self.course_menu.configure(values=formatted_courses)
            self.course_menu.set("Select a course...") # Set default text
        else:
            self.course_menu.configure(values=["No quizzes available"])
            self.course_menu.set("No quizzes available")

    def course_selected(self, selected_course):
        """Enables the start button once a valid course has been selected."""
        if selected_course != "Select a course...":
            self.btn_start.configure(state="normal")
            
    def start_quiz(self):
        """Starts the quiz for the selected course."""
        selected_course = self.course_menu.get()
        if selected_course in ("Select a course...", "No quizzes available"):
            return # Do nothing if a valid course isn't selected

        # Convert the user-friendly name back to the database table name format.
        table_name = selected_course.replace(' ', '_')
        
        self.withdraw() # Hide the welcome screen.
        quiz_window = QuizScreen(self, table_name) # Open the quiz screen.
        quiz_window.grab_set()

    def on_closing(self):
        """Handles the window closing event by showing the main login window again."""
        self.master.deiconify() # Re-shows the main login window.
        self.destroy()

class QuizScreen(ctk.CTkToplevel):
    """The main window where the student takes the quiz."""
    def __init__(self, master, course_name):
        super().__init__(master)
        self.master_welcome = master
        self.course_name = course_name
        self.score = 0
        self.question_index = 0

        self.title(f"{course_name.replace('_', ' ')} Quiz")
        self.geometry("600x450")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Load and shuffle questions for the selected course.
        self.questions = db.get_questions(self.course_name)
        if not self.questions:
            self.display_no_questions()
            return # Stop initialization if there are no questions.
            
        random.shuffle(self.questions)

        # --- UI Elements ---
        self.question_label = ctk.CTkLabel(self, text="Question appears here", font=ctk.CTkFont(size=16), wraplength=550)
        self.question_label.pack(pady=(20, 10))

        self.radio_var = ctk.StringVar(value=None)
        self.option_buttons = []
        for i in range(4):
            # The value for each button is set to 'A', 'B', 'C', or 'D'.
            btn = ctk.CTkRadioButton(self, text=f"Option {i+1}", variable=self.radio_var, value=chr(65+i))
            btn.pack(anchor="w", padx=50, pady=5)
            self.option_buttons.append(btn)
        
        self.feedback_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=14))
        self.feedback_label.pack(pady=10)
        
        self.submit_button = ctk.CTkButton(self, text="Submit Answer", command=self.submit_answer)
        self.submit_button.pack(pady=20)
        
        self.score_label = ctk.CTkLabel(self, text="Score: 0/0", font=ctk.CTkFont(size=12))
        self.score_label.pack(side="bottom", pady=10)

        self.display_question()

    def display_question(self):
        """Loads the next question data into the UI elements."""
        self.feedback_label.configure(text="") # Clear previous feedback.
        self.radio_var.set(None) # Deselect radio buttons.
        self.submit_button.configure(text="Submit Answer", command=self.submit_answer, state="normal")
        
        # Enable all radio buttons for the new question.
        for btn in self.option_buttons:
            btn.configure(state="normal")
        
        question_data = dict(self.questions[self.question_index])
        self.correct_answer = question_data['correct_answer']
        
        self.question_label.configure(text=f"{self.question_index + 1}. {question_data['question_text']}")
        self.option_buttons[0].configure(text=question_data['option_a'])
        self.option_buttons[1].configure(text=question_data['option_b'])
        self.option_buttons[2].configure(text=question_data['option_c'])
        self.option_buttons[3].configure(text=question_data['option_d'])
        
        self.update_score_label()

    def submit_answer(self):
        """Checks the selected answer and provides immediate feedback."""
        selected_answer = self.radio_var.get()
        if not selected_answer:
            self.feedback_label.configure(text="Please select an answer.", text_color="orange")
            return

        # Disable radio buttons after submitting.
        for btn in self.option_buttons:
            btn.configure(state="disabled")

        if selected_answer == self.correct_answer:
            self.score += 1
            self.feedback_label.configure(text="Correct!", text_color="#2ECC71") # Green
        else:
            self.feedback_label.configure(text=f"Incorrect. The correct answer was {self.correct_answer}.", text_color="#E74C3C") # Red
        
        self.update_score_label(answered=True)
        self.submit_button.configure(text="Next Question", command=self.next_question)
        
    def next_question(self):
        """Moves to the next question or ends the quiz if all questions are answered."""
        self.question_index += 1
        if self.question_index < len(self.questions):
            self.display_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        """Clears the window and displays the user's final score."""
        for widget in self.winfo_children():
            widget.destroy()
        
        final_percentage = (self.score / len(self.questions)) * 100
        
        final_message = ctk.CTkLabel(self, 
            text=f"Quiz Complete!\n\nYour final score is: {self.score} out of {len(self.questions)} ({final_percentage:.1f}%)", 
            font=ctk.CTkFont(size=20)
        )
        final_message.pack(expand=True, pady=30)
        
        close_button = ctk.CTkButton(self, text="Return to Menu", command=self.on_closing)
        close_button.pack(pady=20)
        
    def update_score_label(self, answered=False):
        """Updates the score display at the bottom of the window."""
        total_qs_answered = self.question_index + 1 if answered else self.question_index
        self.score_label.configure(text=f"Score: {self.score}/{total_qs_answered}")

    def display_no_questions(self):
        """Displays a message if a selected course has no questions."""
        label = ctk.CTkLabel(self, text="This quiz has no questions yet.\nPlease ask an administrator to add some.", font=ctk.CTkFont(size=16))
        label.pack(expand=True, padx=20, pady=20)
        close_button = ctk.CTkButton(self, text="Go Back", command=self.on_closing)
        close_button.pack(pady=20)

    def on_closing(self):
        """Handles closing the quiz window and shows the welcome screen again."""
        self.master_welcome.deiconify() # Re-shows the student welcome screen.
        self.destroy()