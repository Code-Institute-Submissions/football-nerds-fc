class FootballQuizQuestion:
    """
    Model a real-world entity - in this case, and because it's a quiz,
    it's a data type/class for a question.
    """
    def __init__(self, prompt, answer):
        """
        Stores the question's prompt and the answer, its attributes - all the
        information we need to create a question.
        """
        self.prompt = prompt
        self.answer = answer


# Question prompts
football_question_prompts = [
    "Which player scored the fastest hat-trick in the Premier League?\n1) Sadio Mane\n2) Alan Shearer\n3) Ian Wright\n\n",
    "Which player, with 653 games, has made the most Premier League appearances?\n1) Peter Shilton\n2) Gareth Barry\n3) John Barnes\n\n",
    "Three players share the record for most Premier League red cards (8). Who are they?\n1) Vinnie Jones, Joey Barton and Roy Keane\n2) Dennis Wise, Paolo Di Canio and Paul Gascoigne\n3) Patrick Vieira, Richard Dunne and Duncan Ferguson\n\n",
    "With 260 goals, who is the Premier League's all-time top scorer?\n1) Alan Shearer\n2) Ian Wright\n3) Ian Rush\n\n",
    "When was the inaugural Premier League season?\n1) 1991-92\n2) 1992-93\n3) 1993-94\n\n",
    "Which team won the first Premier League title?\n1) Arsenal\n2) Leeds United\n3) Manchester United\n\n",
    "With 202 clean sheets, which goalkeeper has the best record in the Premier League?\n1) Petr Cech\n2) David Seaman\n3) Peter Schmeichel\n\n",
    "How many clubs competed in the inaugural Premier League season?\n1) 18\n2) 22\n3) 20\n\n",
    "Which three players shared the Premier League Golden Boot in 2018-19?\n1) Sergio Aguero, Jamie Vardy and Harry Kane\n2) Raheem Sterling, Eden Hazard and Callum Wilson\n3) Pierre-Emerick Aubameyang, Mohamed Salah and Sadio Mane\n\n",
    "The fastest goal scored in Premier League history came in 7.69 seconds. Who scored it?\n1) Shane Long\n2) Steven Gerrard\n3) Frank Lampard\n\n"
]

# Question objects - a list of questions to ask and their correct answers
# We'll be able to add as many questions as we want to it in the future
football_questions_and_answers = [
    FootballQuizQuestion(football_question_prompts[0], 1),
    FootballQuizQuestion(football_question_prompts[1], 2),
    FootballQuizQuestion(football_question_prompts[2], 3),
    FootballQuizQuestion(football_question_prompts[3], 1),
    FootballQuizQuestion(football_question_prompts[4], 2),
    FootballQuizQuestion(football_question_prompts[5], 3),
    FootballQuizQuestion(football_question_prompts[6], 1),
    FootballQuizQuestion(football_question_prompts[7], 2),
    FootballQuizQuestion(football_question_prompts[8], 3),
    FootballQuizQuestion(football_question_prompts[9], 1)
]


def run_football_quiz(football_questions_and_answers):
    """
    Function to run the test - asks the user the questions and checks if he/she
    got the answer right.
    Contains one parameter - the list of question objects we want to ask the
    user - we want to loop through each question, ask it to the user, get the
    user's answer and check if it's right.
    """
    # A variable called score
    # To keep track of how the user is doing through the test
    score = 0
    # A for loop - to loop through all the questions on the list of questions
    # For each of those, we want to do something
    for football_question in football_questions_and_answers:
        # While loop with try/except input validation
        while True:
            # Try block to test the code for input errors
            try:
                # To ask the user a question and store the answer inside of a variable
                # It'll represent the answer that the user gave for the question
                # Input turns into an integer to match answers on question objects list
                football_answer = int(input(football_question.prompt))
                # If statement to validate the user's input
                if football_answer in range(1, 3):
                    # A nested if statement - to check if the answer is right
                    if football_answer == football_question.answer:
                        # If true, increment the score variable by 1 and inform user
                        print("Correct!\n")
                        score += 1
                        # If not true, inform user of wrong answer provided
                    else:
                        print("Incorrect! And this was an easy one! Focus!\n")
                # Close outer if statement - prompt user to enter valid input
                else:
                    print("Please enter a number between 1 and 3.\n")
                    continue
            # Except block handles input errors
            except:
                print("Please enter a number between 1 and 3.\n")
                continue
            break
    # At the end, we print how the user did
    print(f"You got {score}/{len(football_questions_and_answers)} correct!")


# Call the run_football_quiz function
# Pass the list of question objects into it
run_football_quiz(football_questions_and_answers)
