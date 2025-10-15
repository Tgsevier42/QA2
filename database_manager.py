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
            "Course_B_Placeholder",
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
                    # 1. Product (creating value)
                    ("Which element of the marketing mix is most relevant to the activity 'creating value'?", "place", "promotion", "price", "product", "D"),
                    # 2. Customer Value definition
                    ("________________ is 'the customers' perception of what they want to have happen...' (i.e., the consequences) in a specific-use situation, with the help of a product or service offering in order to accomplish a desired purpose or goal'.", "Value cocreation", "Marketing", "Ideas", "Customer value", "D"),
                    # 3. Place (convenience)
                    ("Mr. Harrison really likes his morning coffee, and he always stops at Starbucks because it is on the way to work. He is being influenced by the ______ element of the marketing mix.", "price", "product", "promotion", "place", "D"),
                    # 4. Exchange Condition
                    ("What condition is necessary for an exchange to occur?", "Low price", "Public display", "Both parties must be able to walk away from the deal at any time.", "All of the above", "C"),
                    # 5. Exchange Condition (Scenario)
                    ("Andi Littleton has inherited a Featherlite brand horse trailer... what condition is necessary for an exchange to occur between Littleton and a buyer?", "Her trailer should carry a low price.", "Littleton and her buyer must be able to walk away from the deal if desired.", "The trailer should be on display somewhere that people will see it.", "She needs to practice negotiating.", "B"),
                    # 6. Truth about Marketing
                    ("Which of the following is true of marketing?", "Marketing affects various stakeholders.", "Marketing plays no role in creating value.", "Marketing is about satisfying the company's needs and wants.", "Marketing requires place, product, promotion, and perception decisions.", "A"),
                    # 7. Exchange Definition
                    ("_____ is a key ingredient in the philosophy of marketing; it occurs when people give up something in order to receive something that they would rather have.", "Value", "Exchange", "None of the above", "Marketing", "B"),
                    # 8. Marketing Mix Focus (Promotion)
                    ("Which element of the marketing mix focuses on communicating the offering?", "Product", "Price", "Promotion", "Place", "C"),
                    # 9. Marketing Purpose
                    ("The fundamental purpose of marketing is to create **value** by developing a variety of offerings, including what?", "Goods and Services only", "Ideas, Goods, and Services", "Pricing Strategies", "Promotional Campaigns", "B"),
                    # 10. General Marketing Stakeholders (as a filler to meet 10+)
                    ("Marketing involves developing and communicating offerings that have value for:", "Consumers only", "Only the company and its customers", "The company, its customers, partners, and society at large", "Only business-to-business clients", "C")
                ]
                
                # Check if table is empty before inserting
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                if cursor.fetchone()[0] == 0:
                    for q, a, b, c, d, ans_key in data:
                        cursor.execute(f"""
                            INSERT INTO {table_name} 
                            (question_text, option_a, option_b, option_c, option_d, correct_answer) 
                            VALUES (?, ?, ?, ?, ?, ?);
                        """, (q, a, b, c, d, ans_key))
                    print(f"Initial data inserted into {table_name}.")
            
       

            # TODO: ADD DATA INSERTION LOGIC FOR YOUR NEXT THREE COURSES HERE

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