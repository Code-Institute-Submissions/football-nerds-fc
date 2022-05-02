class FootballQuizQuestion:
    """
    Model a real-world entity - in this case, and
    because it's a quiz, it's a data type/class for a
    question.
    Stores the question's prompt and the answer, all
    the information we need to create a question.
    """
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
