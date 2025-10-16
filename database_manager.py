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
    # Sanitize table name to prevent SQL injection issues with dynamic table names
    safe_table_name = "".join(c for c in table_name if c.isalnum() or c == '_')
    if not safe_table_name:
        raise ValueError("Invalid table name provided.")
        
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {safe_table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_text TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_answer TEXT NOT NULL CHECK(correct_answer IN ('A', 'B', 'C', 'D'))
        );
    """)
    return safe_table_name

def populate_initial_data():
    """Creates all tables and populates them with your questions ONLY if they are empty."""
    conn = connect_db()
    cursor = conn.cursor()

    # --- Course 1: MKT_3400_500 ---
    mkt_table = create_table_if_not_exists(cursor, "MKT_3400_500")
    cursor.execute(f"SELECT COUNT(id) FROM {mkt_table}")
    if cursor.fetchone()[0] == 0:
        print(f"Table '{mkt_table}' is empty. Populating with initial data...")
        mkt_questions = [
            ("Which element of the marketing mix is most relevant to the activity 'creating value'?", "place", "promotion", "price", "product", "D"),
            ("________________ is 'the customers' perception of what they want to have happen...' in a specific-use situation...", "Value cocreation", "Marketing", "Ideas", "Customer value", "D"),
            ("Mr. Harrison really likes his morning coffee... he always stops at Starbucks because it is on the way to work...", "price", "product", "promotion", "place", "D"),
            ("What condition is necessary for an exchange to occur?", "Low price", "Public display", "Both parties must be able to walk away...", "All of the above", "C"),
            ("Andi Littleton has inherited a Featherlite brand horse trailer... what condition is necessary for an exchange to occur...?", "Her trailer should carry a low price.", "Littleton and her buyer must be able to walk away...", "The trailer should be on display...", "She needs to practice negotiating.", "B"),
            ("Which of the following is true of marketing?", "Marketing affects various stakeholders.", "Marketing plays no role in creating value.", "Marketing is about satisfying the company's needs...", "Marketing requires place, product, promotion, and perception...", "A"),
            ("_____ is a key ingredient in the philosophy of marketing; it occurs when people give up something to receive something...", "Value", "Exchange", "None of the above", "Marketing", "B"),
            ("Which element of the marketing mix focuses on communicating the offering?", "Product", "Price", "Promotion", "Place", "C"),
            ("The fundamental purpose of marketing is to create **value** by developing a variety of offerings, including what?", "Goods and Services only", "Ideas, Goods, and Services", "Pricing Strategies", "Promotional Campaigns", "B"),
            ("Marketing involves developing and communicating offerings that have value for:", "Consumers only", "Only the company and its customers", "The company, its customers, partners, and society at large", "Only business-to-business clients", "C")
        ]
        cursor.executemany(f"INSERT INTO {mkt_table} (question_text, option_a, option_b, option_c, option_d, correct_answer) VALUES (?, ?, ?, ?, ?, ?)", mkt_questions)

    # --- Course 2: BMGT_3510_005 ---
    bmgt_table = create_table_if_not_exists(cursor, "BMGT_3510_005")
    cursor.execute(f"SELECT COUNT(id) FROM {bmgt_table}")
    if cursor.fetchone()[0] == 0:
        print(f"Table '{bmgt_table}' is empty. Populating with initial data...")
        bmgt_questions = [
            ("According to Ben Horowitz...______ and genius are...the two most critical characteristics of successful entrepreneurs.", "optimism", "resilience", "willpower", "waypower", "B"),
            ("______ is defined as employees’ perceptions of formal and informal organizational policies, practices, procedures and routines:", "Organizational culture", "Job satisfaction", "Organizational climate", "Positive OB", "C"),
            ("Pete and Dana are working on a project together... He sits both of them down to work through the issues. This reflects ______ justice.", "restorative", "distributive", "procedural", "interactional", "D"),
            ("Which of the following statements is true?", "PERMA elements are positively related to good health...", "Well-being is a single, unique concept...", "Employees' level of flourishing is related to organizational outcomes...", "Positive emotions 'happen to people'...", "C"),
            ("Flourishing represents the extent to which our lives contain PERMA—", "positive emotions, enrichments, realism...", "positive emotions, engagement, relationships...", "position, equanimity, respect...", "peace, emotions, reflection...", "B"),
            ("Which of the following is an individual function of a group?", "coordinate interdepartmental efforts", "satisfy the person's need for affiliation", "implement complex decisions", "socialize newcomers", "B"),
            ("Syndey takes over as CEO... The remaining employees resist her ideas. This represent the ______ stage; it is a time of testing.", "norming", "storming", "forming", "performing", "B"),
            ("Rich is part of a newly formed work group... He still feels like he cannot trust them... Which of the following stages is Rich’s group currently in?", "norming", "forming", "storming", "performing", "B"),
            ("As a manager, Haley has established a new work group... Two cliques have formed... Which of the following stages is Haley observing?", "storming", "forming", "performing", "norming", "A"),
            ("As part of a work team in his office, it is Lawrence’s job to make photocopies... Which task role is Lawrence performing?", "coordinator", "orienter", "evaluator", "procedural technician", "D"),
            ("During a group meeting, Nadia comments, ______. She is performing a maintenance role.", "\"What is the real issue here?...\"", "\"Let's accept and praise the various points of view.\"", "\"We can do this. We've met difficult goals before.\"", "\"Last week we decided to table this...\"", "B")
        ]
        cursor.executemany(f"INSERT INTO {bmgt_table} (question_text, option_a, option_b, option_c, option_d, correct_answer) VALUES (?, ?, ?, ?, ?, ?)", bmgt_questions)
    
    # --- Course 3: ECON_3610_003 ---
    econ_table = create_table_if_not_exists(cursor, "ECON_3610_003")
    cursor.execute(f"SELECT COUNT(id) FROM {econ_table}")
    if cursor.fetchone()[0] == 0:
        print(f"Table '{econ_table}' is empty. Populating with initial data...")
        econ_questions = [
            ("Which of the following best defines a population in statistics?", "A small subset of individuals selected for study", "All possible individuals or observations of interest", "The number of people in a sample", "The method of selecting participants", "B"),
            ("A sample is best described as:", "The entire group a researcher wants to study", "A numerical summary of a population", "A portion of the population used to make inferences", "A qualitative variable", "C"),
            ("Which of the following is a qualitative (categorical) variable?", "Height in inches", "Number of siblings", "Type of car (SUV, sedan, truck)", "Age in years", "C"),
            ("The mean, median, and mode are all:", "Measures of spread", "Measures of central tendency", "Probability distributions", "Types of samples", "B"),
            ("Which measure of spread is most affected by extreme values (outliers)?", "Range", "Interquartile range", "Standard deviation", "Median", "A"),
            ("If two events A and B are independent, this means:", "They cannot happen at the same time", "P(A and B) = P(A) + P(B)", "P(A and B) = P(A) × P(B)", "P(A | B) = 0", "C"),
            ("Which probability distribution is most appropriate for modeling the number of customers arriving at a store per hour?", "Normal distribution", "Binomial distribution", "Poisson distribution", "Uniform distribution", "C"),
            ("In a normal distribution, approximately what percent of data falls within one standard deviation of the mean?", "34%", "50%", "68%", "95%", "C"),
            ("When constructing a confidence interval, the “margin of error” represents:", "The sample size", "The average of the data", "The range of the population", "How far the estimate may be from the true parameter", "D"),
            ("In single-sample hypothesis testing, the null hypothesis (H₀) typically states that:", "There is a significant difference", "The sample mean equals the claimed population mean", "The sample size is too small", "The test statistic is greater than 2", "B")
        ]
        cursor.executemany(f"INSERT INTO {econ_table} (question_text, option_a, option_b, option_c, option_d, correct_answer) VALUES (?, ?, ?, ?, ?, ?)", econ_questions)
        
    # --- Course 4: DS_3860_001 ---
    ds_table = create_table_if_not_exists(cursor, "DS_3860_001")
    cursor.execute(f"SELECT COUNT(id) FROM {ds_table}")
    if cursor.fetchone()[0] == 0:
        print(f"Table '{ds_table}' is empty. Populating with initial data...")
        ds_questions = [
            ("In a relational database, a primary key is:", "A field that allows duplicate values", "A field that uniquely identifies each record in a table", "A foreign key in another table", "An attribute that must be null", "B"),
            ("Which of the following best describes a foreign key?", "A key that can only be used in one table", "A key used to enforce referential integrity between tables", "A randomly generated identifier", "A key that prevents duplicate entries", "B"),
            ("Which relational algebra operation returns only the shared tuples that appear in both relations?", "Union", "Intersection", "Difference", "Product", "B"),
            ("The Cartesian Product in relational algebra:", "Combines tables based on matching values", "Returns only common rows", "Pairs every row of one table with every row of another", "Eliminates duplicate rows", "C"),
            ("In an ER diagram, a diamond symbol typically represents:", "An entity", "An attribute", "A relationship", "A primary key", "C"),
            ("Which of the following is a weak entity?", "An entity that has its own primary key", "An entity that depends on another entity for identification", "An entity with no attributes", "An entity that cannot participate in relationships", "B"),
            ("The relational algebra operation σ (sigma) is used for:", "Projection (choosing columns)", "Selection (choosing rows based on a condition)", "Joining two tables", "Sorting rows", "B"),
            ("In an ER model, a multivalued attribute is shown as:", "An oval", "A double oval", "A rectangle", "A dashed line", "B"),
            ("Which of the following is TRUE about 1-to-many (1:M) relationships?", "Each record in Table A matches exactly one record in Table B", "Each record in Table A may match many in Table B", "Each record in Table B may match many in Table A", "Records cannot be related", "B"),
            ("Which relational algebra operation is typically used to combine related data from two tables using a matching attribute?", "Join", "Union", "Difference", "Rename", "A")
        ]
        cursor.executemany(f"INSERT INTO {ds_table} (question_text, option_a, option_b, option_c, option_d, correct_answer) VALUES (?, ?, ?, ?, ?, ?)", ds_questions)

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
    safe_table_name = "".join(c for c in table_name if c.isalnum() or c == '_')
    try:
        cursor.execute(f"""
            INSERT INTO {safe_table_name} (question_text, option_a, option_b, option_c, option_d, correct_answer)
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
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    safe_table_name = "".join(c for c in table_name if c.isalnum() or c == '_')
    cursor.execute(f"SELECT * FROM {safe_table_name}")
    questions = cursor.fetchall()
    conn.close()
    return questions
    
def update_question(table_name, question_id, new_data):
    """Updates an existing question in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    safe_table_name = "".join(c for c in table_name if c.isalnum() or c == '_')
    try:
        cursor.execute(f"""
            UPDATE {safe_table_name} SET
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
    safe_table_name = "".join(c for c in table_name if c.isalnum() or c == '_')
    try:
        cursor.execute(f"DELETE FROM {safe_table_name} WHERE id = ?", (question_id,))
        conn.commit()
    finally:
        conn.close()

# This part runs the setup function when you execute the script directly
if __name__ == '__main__':
    populate_initial_data()