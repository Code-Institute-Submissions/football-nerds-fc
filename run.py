import random  # Random package imported so the sample method can be used
import json  # To import the .json file with the question prompts


class FootballQuizQuestion(object):
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


# To link the main run.py file to the external .json file with the prompts
questions_file = open("questions.json")
football_question_prompts = json.load(questions_file)

# Question objects - a list of questions to ask and their correct answers
# We'll be able to add as many questions as we want to it in the future
football_questions_and_answers = [
    FootballQuizQuestion(football_question_prompts[0]["question"], 1),
    FootballQuizQuestion(football_question_prompts[1]["question"], 2),
    FootballQuizQuestion(football_question_prompts[2]["question"], 3),
    FootballQuizQuestion(football_question_prompts[3]["question"], 1),
    FootballQuizQuestion(football_question_prompts[4]["question"], 2),
    FootballQuizQuestion(football_question_prompts[5]["question"], 3),
    FootballQuizQuestion(football_question_prompts[6]["question"], 1),
    FootballQuizQuestion(football_question_prompts[7]["question"], 2),
    FootballQuizQuestion(football_question_prompts[8]["question"], 3),
    FootballQuizQuestion(football_question_prompts[9]["question"], 1),
    FootballQuizQuestion(football_question_prompts[10]["question"], 2),
    FootballQuizQuestion(football_question_prompts[11]["question"], 3),
    FootballQuizQuestion(football_question_prompts[12]["question"], 1),
    FootballQuizQuestion(football_question_prompts[13]["question"], 2),
    FootballQuizQuestion(football_question_prompts[14]["question"], 3),
    FootballQuizQuestion(football_question_prompts[15]["question"], 1),
    FootballQuizQuestion(football_question_prompts[16]["question"], 2),
    FootballQuizQuestion(football_question_prompts[17]["question"], 3),
    FootballQuizQuestion(football_question_prompts[18]["question"], 1),
    FootballQuizQuestion(football_question_prompts[19]["question"], 2),
    FootballQuizQuestion(football_question_prompts[20]["question"], 3),
    FootballQuizQuestion(football_question_prompts[21]["question"], 1),
    FootballQuizQuestion(football_question_prompts[22]["question"], 2),
    FootballQuizQuestion(football_question_prompts[23]["question"], 3),
    FootballQuizQuestion(football_question_prompts[24]["question"], 1),
    FootballQuizQuestion(football_question_prompts[25]["question"], 2),
    FootballQuizQuestion(football_question_prompts[26]["question"], 3),
    FootballQuizQuestion(football_question_prompts[27]["question"], 1),
    FootballQuizQuestion(football_question_prompts[28]["question"], 2),
    FootballQuizQuestion(football_question_prompts[29]["question"], 3),
    FootballQuizQuestion(football_question_prompts[30]["question"], 1),
    FootballQuizQuestion(football_question_prompts[31]["question"], 2),
    FootballQuizQuestion(football_question_prompts[32]["question"], 3),
    FootballQuizQuestion(football_question_prompts[33]["question"], 1),
    FootballQuizQuestion(football_question_prompts[34]["question"], 2),
    FootballQuizQuestion(football_question_prompts[35]["question"], 3),
    FootballQuizQuestion(football_question_prompts[36]["question"], 1),
    FootballQuizQuestion(football_question_prompts[37]["question"], 2),
    FootballQuizQuestion(football_question_prompts[38]["question"], 3),
    FootballQuizQuestion(football_question_prompts[39]["question"], 1),
    FootballQuizQuestion(football_question_prompts[40]["question"], 2),
    FootballQuizQuestion(football_question_prompts[41]["question"], 3),
    FootballQuizQuestion(football_question_prompts[42]["question"], 1),
    FootballQuizQuestion(football_question_prompts[43]["question"], 2),
    FootballQuizQuestion(football_question_prompts[44]["question"], 3),
    FootballQuizQuestion(football_question_prompts[45]["question"], 1),
    FootballQuizQuestion(football_question_prompts[46]["question"], 2),
    FootballQuizQuestion(football_question_prompts[47]["question"], 3),
    FootballQuizQuestion(football_question_prompts[48]["question"], 1),
    FootballQuizQuestion(football_question_prompts[49]["question"], 2),
    FootballQuizQuestion(football_question_prompts[50]["question"], 3),
    FootballQuizQuestion(football_question_prompts[51]["question"], 1),
    FootballQuizQuestion(football_question_prompts[52]["question"], 2),
    FootballQuizQuestion(football_question_prompts[53]["question"], 3),
    FootballQuizQuestion(football_question_prompts[54]["question"], 1),
    FootballQuizQuestion(football_question_prompts[55]["question"], 2),
    FootballQuizQuestion(football_question_prompts[56]["question"], 3),
    FootballQuizQuestion(football_question_prompts[57]["question"], 1),
    FootballQuizQuestion(football_question_prompts[58]["question"], 2),
    FootballQuizQuestion(football_question_prompts[59]["question"], 3),
    FootballQuizQuestion(football_question_prompts[60]["question"], 1),
    FootballQuizQuestion(football_question_prompts[61]["question"], 2),
    FootballQuizQuestion(football_question_prompts[62]["question"], 3),
    FootballQuizQuestion(football_question_prompts[63]["question"], 1),
    FootballQuizQuestion(football_question_prompts[64]["question"], 2),
    FootballQuizQuestion(football_question_prompts[65]["question"], 3),
    FootballQuizQuestion(football_question_prompts[66]["question"], 1),
    FootballQuizQuestion(football_question_prompts[67]["question"], 2),
    FootballQuizQuestion(football_question_prompts[68]["question"], 3),
    FootballQuizQuestion(football_question_prompts[69]["question"], 1),
    FootballQuizQuestion(football_question_prompts[70]["question"], 2),
    FootballQuizQuestion(football_question_prompts[71]["question"], 3),
    FootballQuizQuestion(football_question_prompts[72]["question"], 1),
    FootballQuizQuestion(football_question_prompts[73]["question"], 2),
    FootballQuizQuestion(football_question_prompts[74]["question"], 3),
    FootballQuizQuestion(football_question_prompts[75]["question"], 1),
    FootballQuizQuestion(football_question_prompts[76]["question"], 2),
    FootballQuizQuestion(football_question_prompts[77]["question"], 3),
    FootballQuizQuestion(football_question_prompts[78]["question"], 1),
    FootballQuizQuestion(football_question_prompts[79]["question"], 2)
]


def run_football_quiz(sample):
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
    for football_question in sample:
        # While loop with try/except input validation
        while True:
            # Try block to test the code for input errors
            try:
                # Ask user a question and store answer in a variable
                # Represents the answer the user gave for the question
                # Input-to-integer to match answers on question objects list
                football_answer = int(input(football_question.prompt))
                # If statement to validate the user's input
                if football_answer in range(1, 4):
                    # A nested if statement - to check if the answer is right
                    if football_answer == football_question.answer:
                        # If true, increment score by 1 and inform user
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
            except ValueError:
                print("Please enter a number between 1 and 3.\n")
                continue
            break
    # At the end, print how the user did
    print("************************************************")
    print(f"*             You got {score}/{len(sample)} correct!            *")
    print("************************************************")
    print("*   YES! YOU'RE THE FOOTBALL NERD OF THE DAY!  *")
    print("************************************************\n")


# Main function
if __name__ == "__main__":
    # Sample method to get random sample list of questions from main list
    sample = random.sample(football_questions_and_answers, 10)
    # Welcome and "let's play" message for the user
    print("\n*********************************************************")
    print("*         Welcome to the Football Nerds FC quiz!        *")
    print("*********************************************************")
    print("*    Do you think you know everything about football?   *")
    print("*********************************************************")
    print("* Do you have what it takes to be a true football nerd? *")
    print("*********************************************************")
    print("*              Let's find out! Good luck!               *")
    print("*********************************************************\n")
    # Call the run_football_quiz function
    # Pass the list of question objects into it
    run_football_quiz(sample)
    # While loop to offer the user the option to play again
    # Also to validate the user's input
    while True:
        # Variable for user's input - a lower method is used to convert input
        # into lowercase so it matches the required y/n user input
        PLAY_AGAIN = str.lower(input("Play again (y/n)?\n"))
        # If statement to run game again or exit it, and to validate the data
        if PLAY_AGAIN == "y":
            sample = random.sample(football_questions_and_answers, 10)
            run_football_quiz(sample)
        elif PLAY_AGAIN == "n":
            # To exit the code safely
            raise SystemExit("\nThank you for playing!\n")
        else:
            print("Please enter 'y' or 'n'.\n")
            continue
