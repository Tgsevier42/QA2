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
            ("Syndey takes over as CEO of Sandstorm Jeans... The remaining employees resist her ideas. This represent the ______ stage; it is a time of testing.", "norming", "storming", "forming", "performing", "B"),
            ("Rich is part of a newly formed work group... He still feels like he cannot trust them... Which of the following stages is Rich’s group currently in?", "norming", "forming", "storming", "performing", "B"),
            ("As a manager, Haley has established a new work group... Two cliques have formed... Which of the following stages of group development process is Haley observing?", "storming", "forming", "performing", "norming", "A"),
            ("As part of a work team in his office, it is Lawrence’s job to make photocopies... Which of the following task roles is Lawrence performing in his work team?", "coordinator", "orienter", "evaluator", "procedural technician", "D"),
            ("During a group meeting, Nadia comments, ______. She is performing a maintenance role.", "\"What is the real issue here? We don't seem to be going anywhere.\"", "\"Let's accept and praise the various points of view.\"", "\"We can do this. We've met difficult goals before.\"", "\"Last week we decided to table this agenda item...\"", "B")
        ]
        cursor.executemany(f"INSERT INTO {bmgt_table} (question_text, option_a, option_b, option_c, option_d, correct_answer) VALUES (?, ?, ?, ?, ?, ?)", bmgt_questions)
    
    # --- Course 3: ECON-3610-003 ---
    econ_table = "ECON_3610_003"
    create_table_if_not_exists(cursor, econ_table)
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

    # --- Add your last course here when you have the data ---
    # create_table_if_not_exists(cursor, "Course_D_Placeholder")

    conn.commit()
    conn.close()
    print("Database initialization check complete.")