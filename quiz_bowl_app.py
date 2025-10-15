# File: quiz_bowl_app.py

import customtkinter as ctk
from tkinter import messagebox
import admin_interface
import student_interface
import database_manager as db

# Set the appearance and color the application
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue") # Options: "blue", "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Quiz Bowl Application Login")
        self.geometry("400x350")

        # Configure the grid to center the main frame
        self.grid_columnconfigure(0, weight=1)
        
        # Main Login Frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.label = ctk.CTkLabel(self.main_frame, text="Quiz Bowl Login", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.grid(row=0, column=0, padx=30, pady=(30, 15))

        # Student Button
        self.btn_student = ctk.CTkButton(self.main_frame, text="I am a Student", command=self.open_student_portal)
        self.btn_student.grid(row=1, column=0, padx=30, pady=15, sticky="ew")

        # Admin Login Section
        self.label_admin = ctk.CTkLabel(self.main_frame, text="Administrator Login")
        self.label_admin.grid(row=2, column=0, padx=30, pady=(20, 5))

        self.entry_password = ctk.CTkEntry(self.main_frame, placeholder_text="Password", show="*")
        self.entry_password.grid(row=3, column=0, padx=30, pady=5, sticky="ew")

        self.btn_admin_login = ctk.CTkButton(self.main_frame, text="Login as Admin", command=self.admin_login)
        self.btn_admin_login.grid(row=4, column=0, padx=30, pady=15, sticky="ew")

    def admin_login(self):
        """Checks the admin password and opens the admin interface."""
        password = self.entry_password.get()
        if password == "admin":
            self.withdraw() # Hide the login window
            admin_window = admin_interface.AdminApp(self)
            admin_window.focus()
        else:
            messagebox.showerror("Login Failed", "Incorrect password.")
            self.entry_password.delete(0, 'end')

    def open_student_portal(self):
        """Opens the student welcome screen."""
        self.withdraw() # Hide the login window
        student_window = student_interface.StudentWelcomeScreen(self)
        student_window.focus()

# This is the main execution block that runs when you start the program
if __name__ == "__main__":
    db.populate_initial_data()
    
    app = App()
    app.mainloop()