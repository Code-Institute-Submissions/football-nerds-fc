class FootballQuizQuestion:
    """
    Model a real-world entity - in this case, and
    because it's a quiz, it's a data type/class for a
    question.
    Stores the question's prompt and the answer, its
    attributes - all the information we need to create
    a question.
    """
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


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
