# database_manager.py

import sqlite3

DATABASE_NAME = "quiz_data.db"

def initialize_database():
    """Connects to the DB and creates the four required course tables."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        # Define table names based on your courses 
        course_tables = [
            "MKT_3400_500",
            "BMGT_3510_005",  
            "Course_C_Placeholder", 
            "Course_D_Placeholder"  
        ]
        
        for table_name in course_tables:
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY,
                    question_text TEXT NOT NULL,
                    option_a TEXT NOT NULL,
                    option_b TEXT NOT NULL,
                    option_c TEXT NOT NULL,
                    option_d TEXT NOT NULL,
                    correct_answer TEXT NOT NULL
                );
            """)
            print(f"Table '{table_name}' checked/created successfully.")
            
         

            if table_name == "MKT_3400_500":
                data = [
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
            
            elif table_name == "BMGT_3510_005":
                data = [
                    ("According to Ben Horowitz, the renowned technology entrepreneur and venture capitalist, ______ and genius are in his mind the two most critical characteristics of successful entrepreneurs.", "optimism", "resilience", "willpower", "waypower", "B"),
                    ("______ is defined as employees’ perceptions of formal and informal organizational policies, practices, procedures and routines:", "Organizational culture", "Job satisfaction", "Organizational climate", "Positive OB", "C"),
                    ("Pete and Dana are working on a project together... He sits both of them down to work through the issues. This reflects ______ justice.", "restorative", "distributive", "procedural", "interactional", "D"),
                    ("Which of the following statements is true?", "PERMA elements are positively related to good health...", "Well-being is a single, unique concept that is related to happiness.", "Employees' level of flourishing is related to organizational outcomes such as productivity and financial performance.", "Positive emotions 'happen to people'; they cannot be pursued proactively.", "C"),
                    ("Flourishing represents the extent to which our lives contain PERMA—", "positive emotions, enrichments, realism, meaning, and action.", "positive emotions, engagement, relationships, meaning, and achievement.", "position, equanimity, respect, money, and acceptance.", "peace, emotions, reflection, management, and action.", "B"),
                    ("Which of the following is an individual function of a group?", "coordinate interdepartmental efforts", "satisfy the person's need for affiliation", "implement complex decisions", "socialize newcomers", "B"),
                    ("Syndey takes over as CEO of Sandstorm Jeans... The remaining employees resist her ideas. This represent the ______ stage; it is a time of testing.", "norming", "conforming", "forming", "performing", "E"), # Note: E is used for the 5th option 'storming'
                    ("Rich is part of a newly formed work group... He still feels like he cannot trust them... Which of the following stages is Rich’s group currently in?", "norming", "forming", "storming", "performing", "B"),
                    ("As a manager, Haley has established a new work group... Two cliques have formed... Which of the following stages of group development process is Haley observing?", "storming", "forming", "performing", "norming", "A"),
                    ("As part of a work team in his office, it is Lawrence’s job to make photocopies... Which of the following task roles is Lawrence performing in his work team?", "coordinator", "orienter", "evaluator", "procedural technician", "D"),
                    ("During a group meeting, Nadia comments, ______. She is performing a maintenance role.", "\"What is the real issue here? We don't seem to be going anywhere.\"", "\"Let's accept and praise the various points of view.\"", "\"We can do this. We've met difficult goals before.\"", "\"Last week we decided to table this agenda item...\"", "B")
                ]
            
            # Execute data insertion if the table is empty
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            if cursor.fetchone()[0] == 0:
                for q, a, b, c, d, ans_key in data:
                    cursor.execute(f"""
                        INSERT INTO {table_name} 
                        (question_text, option_a, option_b, option_c, option_d, correct_answer) 
                        VALUES (?, ?, ?, ?, ?, ?);
                    """, (q, a, b, c, d, ans_key))
                print(f"Initial data inserted into {table_name}.")

        conn.commit()
        
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

def get_db_connection():
    """Returns a connection object to the database."""
    return sqlite3.connect(DATABASE_NAME)

if __name__ == '__main__':
    initialize_database()