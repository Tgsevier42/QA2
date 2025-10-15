# File: database_manager.py

import sqlite3
import os

# Use the database name you chose
DATABASE_NAME = "quiz_data.db"

def connect_db():
    """Establishes a connection to the SQLite database and creates it if it doesn't exist."""
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_table_if_not_exists(cursor, table_name):
    """A helper function to create a single table."""
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_text TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_answer TEXT NOT NULL CHECK(correct_answer IN ('A', 'B', 'C', 'D'))
        );
    """)

def populate_initial_data():
    """Creates all tables and populates them with your questions ONLY if they are empty."""
    conn = connect_db()
    cursor = conn.cursor()

    # --- Course 1: MKT_3400_500 ---
    mkt_table = "MKT_3400_500"
    create_table_if_not_exists(cursor, mkt_table)
    cursor.execute(f"SELECT COUNT(id) FROM {mkt_table}")
    if cursor.fetchone()[0] == 0:
        print(f"Table '{mkt_table}' is empty. Populating with initial data...")
        mkt_questions = [
            ("Which element of the marketing mix is most relevant to the activity 'creating value'?", "place", "promotion", "price", "product", "D"),
            ("________________ is 'the customers' perception of what they want to have happen...' (i.e., the consequences) in a specific-use situation, with the help of a product or service offering in order to accomplish a desired purpose or goal'.", "Value cocreation", "Marketing", "Ideas", "Customer value", "D"),
            ("Mr. Harrison really likes his morning coffee, and he always stops at Starbucks because it is on the way to work. He is being influenced by the ______ element of the marketing mix.", "price", "product", "promotion", "place", "D"),
            ("What condition is necessary for an exchange to occur?", "Low price", "Public display", "Both parties must be able to walk away from the deal at any time.", "All of the above", "C"),
            ("Andi Littleton has inherited a Featherlite brand horse trailer... what condition is necessary for an exchange to occur between Littleton and a buyer?", "Her trailer should carry a low price.", "Littleton and her buyer must be able to walk away from the deal if desired.", "The trailer should be on display somewhere that people will see it.", "She needs to practice negotiating.", "B"),
            ("Which of the following is true of marketing?", "Marketing affects various stakeholders.", "Marketing plays no role in creating value.", "Marketing is about satisfying the company's needs and wants.", "Marketing requires place, product, promotion, and perception decisions.", "A"),
            ("_____ is a key ingredient in the philosophy of marketing; it occurs when people give up something in order to receive something that they would rather have.", "Value", "Exchange", "None of the above", "Marketing", "B"),
            ("Which element of the marketing mix focuses on communicating the offering?", "Product", "Price", "Promotion", "Place", "C"),
            ("The fundamental purpose of marketing is to create **value** by developing a variety of offerings, including what?", "Goods and Services only", "Ideas, Goods, and Services", "Pricing Strategies", "Promotional Campaigns", "B"),
            ("Marketing involves developing and communicating offerings that have value for:", "Consumers only", "Only the company and its customers", "The company, its customers, partners, and society at large", "Only business-to-business clients", "C")
        ]
        cursor.executemany(f"INSERT INTO {mkt_table} (question_text, option_a, option_b, option_c, option_d, correct_answer) VALUES (?, ?, ?, ?, ?, ?)", mkt_questions)

    # --- Course 2: BMGT_3510_005 ---
    bmgt_table = "BMGT_3510_005"
    create_table_if_not_exists(cursor, bmgt_table)
    cursor.execute(f"SELECT COUNT(id) FROM {bmgt_table}")
    if cursor.fetchone()[0] == 0:
        print(f"Table '{bmgt_table}' is empty. Populating with initial data...")
        bmgt_questions = [
            ("According to Ben Horowitz, the renowned technology entrepreneur and venture capitalist, ______ and genius are in his mind the two most critical characteristics of successful entrepreneurs.", "optimism", "resilience", "willpower", "waypower", "B"),
            ("______ is defined as employees’ perceptions of formal and informal organizational policies, practices, procedures and routines:", "Organizational culture", "Job satisfaction", "Organizational climate", "Positive OB", "C"),
            ("Pete and Dana are working on a project together... He sits both of them down to work through the issues. This reflects ______ justice.", "restorative", "distributive", "procedural", "interactional", "D"),
            ("Which of the following statements is true?", "PERMA elements are positively related to good health...", "Well-being is a single, unique concept that is related to happiness.", "Employees' level of flourishing is related to organizational outcomes such as productivity and financial performance.", "Positive emotions 'happen to people'; they cannot be pursued proactively.", "C"),
            ("Flourishing represents the extent to which our lives contain PERMA—", "positive emotions, enrichments, realism, meaning, and action.", "positive emotions, engagement, relationships, meaning, and achievement.", "position, equanimity, respect, money, and acceptance.", "peace, emotions, reflection, management, and action.", "B"),
            ("Which of the following is an individual function of a group?", "coordinate interdepartmental efforts", "satisfy the person's need for affiliation", "implement complex decisions", "socialize newcomers", "B"),
            # CORRECTED QUESTION: Changed answer from 'E' to a valid option. "Storming" is the testing stage.
            ("Syndey takes over as CEO of Sandstorm Jeans... The remaining employees resist her ideas. This represent the ______ stage; it is a time of testing.", "norming", "storming", "forming", "performing", "B"),
            ("Rich is part of a newly formed work group... He still feels like he cannot trust them... Which of the following stages is Rich’s group currently in?", "norming", "forming", "storming", "performing", "B"),
            ("As a manager, Haley has established a new work group... Two cliques have formed... Which of the following stages of group development process is Haley observing?", "storming", "forming", "performing", "norming", "A"),
            ("As part of a work team in his office, it is Lawrence’s job to make photocopies... Which of the following task roles is Lawrence performing in his work team?", "coordinator", "orienter", "evaluator", "procedural technician", "D"),
            ("During a group meeting, Nadia comments, ______. She is performing a maintenance role.", "\"What is the real issue here? We don't seem to be going anywhere.\"", "\"Let's accept and praise the various points of view.\"", "\"We can do this. We've met difficult goals before.\"", "\"Last week we decided to table this agenda item...\"", "B")
        ]
        cursor.executemany(f"INSERT INTO {bmgt_table} (question_text, option_a, option_b, option_c, option_d, correct_answer) VALUES (?, ?, ?, ?, ?, ?)", bmgt_questions)

    # --- Add your other two courses here when you have the data ---
    # create_table_if_not_exists(cursor, "Course_C_Placeholder")
    # create_table_if_not_exists(cursor, "Course_D_Placeholder")

    conn.commit()
    conn.close()
    print("Database initialization check complete.")

### --- Functions for the Admin and Student Interfaces --- ###

def get_course_tables():
    """Retrieves a list of all course table names from the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()
    return tables

def add_question(table_name, question_data):
    """Adds a new question to a specific course table."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(f"""
            INSERT INTO {table_name} (question_text, option_a, option_b, option_c, option_d, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            question_data['question_text'], question_data['option_a'], question_data['option_b'],
            question_data['option_c'], question_data['option_d'], question_data['correct_answer']
        ))
        conn.commit()
    finally:
        conn.close()

def get_questions(table_name):
    """Fetches all questions from a specific course table."""
    conn = connect_db()
    # This makes the cursor return dictionary-like rows, which can be useful
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    questions = cursor.fetchall()
    conn.close()
    return questions
    
def update_question(table_name, question_id, new_data):
    """Updates an existing question in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(f"""
            UPDATE {table_name} SET
            question_text = ?, option_a = ?, option_b = ?, option_c = ?, option_d = ?, correct_answer = ?
            WHERE id = ?
        """, (
            new_data['question_text'], new_data['option_a'], new_data['option_b'],
            new_data['option_c'], new_data['option_d'], new_data['correct_answer'], question_id
        ))
        conn.commit()
    finally:
        conn.close()

def delete_question(table_name, question_id):
    """Deletes a question from the database."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (question_id,))
        conn.commit()
    finally:
        conn.close()

# This part runs the setup function when you execute the script directly
if __name__ == '__main__':
    populate_initial_data()