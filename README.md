# Python Quiz Bowl Application

This project is a comprehensive **Quiz Bowl application** developed in Python.  
It features a modern GUI built with **CustomTkinter**, a **SQLite** database for content management, and separate, feature-rich interfaces for **administrators** and **students**.

---

## Features

### Dual Interface
- Separate, intuitive GUIs for administrators and students.

### Student Portal 🧑‍🎓
- Select a quiz from a list of available courses.
- Take quizzes with randomized multiple-choice questions.
- Receive immediate feedback on answers (“Correct!” or “Incorrect”).
- View a final score and percentage upon completion.

### Administrator Panel 🧑‍💼
- Password-protected access (**password:** `admin`).
- View all questions for any course.
- Add new questions to any course.
- Edit question text and answers.
- Delete questions from a course.
- Create entirely new quiz courses on the fly.

### Database Backend
- Uses SQLite for a lightweight, file-based database (`quiz_data.db`).
- A robust manager (`database_manager.py`) handles all data operations safely.

---

## For Students

1. On the login screen, click **"I am a Student."**
2. On the **"Welcome, Student!"** screen, open the dropdown to see available quizzes.
3. Select a quiz.
4. Click **"Start Quiz."**
5. For each question:
   - Select an answer and click **"Submit Answer."** You’ll see if it’s correct.
   - Click **"Next Question."** to proceed.
6. At the end, view your **final score and percentage.**

---

## For Administrators

1. On the login screen, type the password **`admin`**.
2. Click **"Login as Admin."** You will enter the **Administrator Panel.**
3. **View Questions:** Select a course from the dropdown on the left.
4. **Add a Question:** Select a course, then click **"Add New Question."**
5. **Edit or Delete a Question:** Use the **Edit** or **Delete** button next to a listed question.
6. **Add a New Course:** Click **"Add New Course"** and enter a name.
