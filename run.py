import random # Random package imported so the sample method can be used
import json # To import the .json file with the question prompts


class FootballQuizQuestion (object):
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
    "The fastest goal scored in Premier League history came in 7.69 seconds. Who scored it?\n1) Shane Long\n2) Steven Gerrard\n3) Frank Lampard\n\n",
    "There have been two World Cup trophies. What was the name of the first?\n1) Henri Delaunay Trophy\n2) Jules Rimet Trophy\n3) Larry O'Brien Trophy\n\n",
    "Which country won the first ever World Cup in 1930?\n1) Italy\n2) Germany\n3) Uruguay\n\n",
    "Which country has won the most World Cups?\n1) Brazil\n2) Italy\n3) Germany\n\n",
    "Three countries have won the World Cup twice. Can you name them?\n1) Brazil, Italy and Germany\n2) Argentina, France and Uruguay\n3) England, Spain and Portugal\n\n",
    "Which country has appeared in three World Cup finals, but never won the competition?\n1) Portugal\n2) Hungary\n3) Netherlands\n\n",
    "The 2026 World Cup will be hosted across three different countries. Can you name them?\n1) United States, Canada and Mexico\n2) Brazil, Argentina and Colombia\n3) Japan, China and South Korea\n\n",
    "In which World Cup did Diego Maradona score his infamous 'Hand of God' goal?\n1) Spain 1982\n2) Mexico 1986\n3) Italy 1990\n\n",
    "The record number of World Cup goals is 16, scored by who?\n1) Pele\n2) Ronaldo\n3) Miroslav Klose\n\n",
    "Three people have won the World Cup as a player and as a coach. Mario Zagallo, Didier Deschamps and... can you name the third?\n1) Franz Beckenbauer\n2) Giovanni Trapattoni\n3) Joachim Low\n\n",
    "Two English players have won the World Cup Golden Boot. Who are they?\n1) Alan Shearer and Ian Wright\n2) Gary Lineker and Harry Kane\n3) Peter Beardsley and Teddy Sheringham\n\n",
    "Which Swedish footballer once had a clause inserted into his Premier League contract that prohibited him from travelling into space?\n1) Freddie Ljungberg\n2) Anders Limpar\n3) Stefan Schwarz\n\n",
    "Which Ballon d'Or-winning footballer had a galaxy named after them in 2015?\n1) Cristiano Ronaldo\n2) Lionel Messi\n3) Neymar\n\n",
    "Can you name the former Germany international who went on to become a professional wrestler in the WWE?\n1) Jens Jeremies\n2) Tim Wiese\n3) Stefan Kuntz\n\n",
    "Which former England internationals reached number 12 in the UK Singles Chart with the 1987 song 'Diamond Lights'?\n1) Paul Gascoigne and Peter Bearsdley\n2) Gary Lineker and John Barnes\n3) Chris Waddle and Glenn Hoddle\n\n",
    "The England Euro 1996 song 'Three Lions' was a hit by which comedy double act?\n1) David Baddiel and Frank Skinner\n2) Ren and Stimpy\n3) Amateur Transplants\n\n",
    "Which former Tottenham manager has competed in the Dakar Rally?\n1) Nuno Espirito Santo\n2) Andre Villas-Boas\n3) Jose Mourinho\n\n",
    "What was the name of the hotel Jose Mourinho lived in when he managed Manchester United?\n1) Hotel California\n2) The Savoy Hotel\n3) The Lowry Hotel\n\n",
    "Which Spanish club's nickname is 'Los Colchoneros', which translates to English as 'The Mattress Makers'?\n1) Atletico Madrid\n2) Real Madrid\n3) Barcelona\n\n",
    "English rock star Elton John was twice the owner of which football club?\n1) Crystal Palace\n2) Watford\n3) Queens Park Rangers\n\n",
    "Rangers tried to sign which superstar after Alex McLeish was alerted to his ability through the popular video game Football Manager?\n1) Neymar\n2) Cristiano Ronaldo\n3) Lionel Messi\n\n",
    "Messi has spent his entire professional career at Barcelona, but what was his schoolboy team?\n1) Newell's Old Boys\n2) River Plate\n3) Boca Juniors\n\n",
    "Which Portuguese team did Cristiano Ronaldo play for before signing for Manchester United?\n1) Benfica\n2) Sporting\n3) Porto\n\n",
    "Cristiano Ronaldo is synonymous with the No. 7, but what other number did he wear at Real Madrid?\n1) No. 11\n2) No. 10\n3) No. 9\n\n",
    "Messi famously retired from international duty in which year before reversing his decision?\n1) 2016\n2) 2017\n3) 2018\n\n",
    "Cristiano Ronaldo exclaims which word when celebrating a goal?\n1) No!\n2) Si!\n3) Quizas!\n\n",
    "Messi wore the No. 30 at the start of his Barca career and is now No. 10. What other number has he worn for the club?\n1) No. 9\n2) No. 29\n3) No. 19\n\n",
    "Which Portuguese island off the coast of Africa, which also shares its name with a cake, is Cristiano Ronaldo from?\n1) Madeira\n2) Azores\n3) Canarias\n\n",
    "Messi has won a record number of Ballon d'Or awards – how many?\n1) 5\n2) 6\n3) 7\n\n",
    "Cristiano Ronaldo helped Portugal win the European Championship in which year?\n1) 2008\n2) 2012\n3) 2016\n\n",
    "Which German multinational sportswear company is Messi an ambassador for?\n1) Adidas\n2) Nike\n3) Puma\n\n",
    "Which club has won the most Champions League titles?\n1) Bayern Munich\n2) Real Madrid\n3) Barcelona\n\n",
    "Who is the only player to win the Champions League with three different clubs?\n1) Frank Rijkaard\n2) Edgar Davids\n3) Clarence Seedorf\n\n",
    "Three people have won the Champions League a record three times as manager. Who are they?\n1) Bob Paisley, Carlo Ancelotti and Zinedine Zidane\n2) Pep Guardiola, Jose Mourinho and Luiz Felipe Scolari\n3) Arrigo Sacchi, Fabio Capello and Ottmar Hitzfeld\n\n",
    "In which season was the European Cup rebranded as the Champions League?\n1) 1991-92\n2) 1992-93\n3) 1993-94\n\n",
    "Which team was the first from the UK to win the European Cup?\n1) Aberdeen\n2) Rangers\n3) Celtic\n\n",
    "The Champions League has been won only once by a team from Romania. Can you name them?\n1) Steaua Bucharest\n2) Dinamo Bucharest\n3) Rapid Bucharest\n\n",
    "Liverpool have won six Champions Leagues and Manchester United have won three, but who are England's third most successful team in the competition, with two titles?\n1) Arsenal\n2) Nottingham Forest\n3) Chelsea\n\n",
    "Who is the Champions League's top goalscorer of all time?\n1) Neymar\n2) Lionel Messi\n3) Cristiano Ronaldo\n\n",
    "Which player holds the record for most Champions League winners' medals?\n1) Francisco Gento\n2) Cristiano Ronaldo\n3) Lionel Messi\n\n",
    "Which outfield player appeared in the Champions League final in three different decades?\n1) Mark Hughes\n2) Ryan Giggs\n3) Peter Schmeichel\n\n",
    "In which year was the first European Championship held?\n1) 1968\n2) 1964\n3) 1960\n\n",
    "With three titles each, which two teams have won the most European Championships?\n1) Germany and Spain\n2) Italy and France\n3) Portugal and England\n\n",
    "What is the name of the European Championship trophy?\n1) Larry O’Brien Trophy\n2) Henri Delaunay Trophy\n3) Jules Rimet Trophy\n\n",
    "With nine goals, who scored the most goals in a single European Championship tournament?\n1) Eusebio\n2) Cristiano Ronaldo\n3) Michel Platini\n\n",
    "The Euro 2000 final between France and Italy was decided by a Golden Goal. Which player scored the goal?\n1) David Trezeguet\n2) Christophe Dugarry\n3) Thierry Henry\n\n",
    "England's all-time leading European Championship goalscorer has a tally of seven goals. Can you name the player?\n1) Peter Beardsley\n2) Alan Shearer\n3) Teddy Sheringham\n\n",
    "Which one of the following three teams has not won the European Championship: Denmark, Belgium or Greece?\n1) Denmark\n2) Greece\n3) Belgium\n\n",
    "Denmark notably won Euro 1992, despite the fact that they did not initially qualify. Which team did they replace?\n1) Yugoslavia\n2) Italy\n3) Soviet Union\n\n",
    "In which year did the European Championship expand from 16 teams to 24 teams?\n1) Euro 2012\n2) Euro 2016\n3) Euro 2020\n\n",
    "Only one person has won the European Championship as a player and as manager. Can you name him?\n1) Giovanni Trapattoni\n2) Franz Beckenbauer\n3) Berti Vogts\n\n",
    "I made my international debut for Brazil in 1993 and scored in the game. I played in two World Cup finals and my club career saw me play in Brazil, Italy, Angola, Spain, Greece and Uzbekistan.\n1) Rivaldo\n2) Ronaldinho Gaucho\n3) Ronaldo\n\n",
    "I've played in Germany, Italy, Austria and France. I have won the Serie A and scored the first ever Golden Goal in international football.\n1) Kaka\n2) Oliver Bierhoff\n3) Romario\n\n",
    "I have played in the Conference, League Two, League One, Championship, Premier League, UEFA Cup, Champions League and the World Cup.\n1) Denis Irwin\n2) Terry Phelan\n3) Steve Finnan\n\n",
    "I was the first Liverpool player to win the Ballon d'Or. I scored 40 goals for my country and have played in England and Spain.\n1) Michael Owen\n2) Robbie Fowler\n3) Steve McManaman\n\n",
    "I was originally a striker before becoming a defender. I played 11 seasons for the same club before managing them. I've won two Bundesliga titles and a Champions League.\n1) Joachim Low\n2) Jurgen Klopp\n3) Berti Vogts\n\n",
    "I have played for Chelsea and spent time playing in Turkey. I've been crowned African Footballer of the Year four times and the Africa Cup of Nations twice.\n1) Michael Essien\n2) Didier Drogba\n3) Samuel Eto'o\n\n",
    "I have won league titles in Italy, Germany, Portugal and Austria. I also won the European Cup both as a player and as a manager.\n1) Giovanni Trapattoni\n2) Carlo Ancelotti\n3) Fernando Santos\n\n",
    "I am the manager who first named David Beckham as England captain.\n1) Bobby Robson\n2) Peter Taylor\n3) Sven-Goran Eriksson\n\n",
    "I've won the World Cup and European Championship at international level and I won the Champions League on two occasions as a manager of two different clubs.\n1) Franz Beckenbauer\n2) Berti Vogts\n3) Jupp Heynckes\n\n",
    "I've worn numbers 7, 17, 28 and 9 in my career, playing my football across, England, Spain, Italy and Portugal.\n1) Cristiano Ronaldo\n2) Luis Figo\n3) Paulo Futre\n\n",
    "In what league is the concept of a 'Designated Player' a feature?\n1) Canadian Premier League\n2) Major League Soccer\n3) Liga MX\n\n",
    "Manchester United famously wear red, but what colours did they wear before adopting red?\n1) Black and white\n2) Blue and black\n3) Green and gold\n\n",
    "Which club is associated with the 'Galacticos'?\n1) Real Madrid\n2) Atletico Madrid\n3) Barcelona\n\n",
    "Which manager was famously said to have given players the 'Hairdryer Treatment'?\n1) Nigel Clough\n2) Alex Ferguson\n3) Roy Keane\n\n",
    "Which club is sometimes referred to as 'FC Hollywood'?\n1) Real Madrid\n2) Liverpool\n3) Bayern Munich\n\n",
    "In English football, what is 'St. Totteringham's Day'?\n1) The date on which it is mathematically impossible for Tottenham to finish above Arsenal\n2) The date on which it is mathematically impossible for Arsenal to finish above Tottenham\n3) The date on which it is mathematically impossible for Tottenham to finish above Chelsea\n\n",
    "After Juventus, Milan and Inter Milan, with nine Scudettos, which team has won the most Serie A titles?\n1) Napoli\n2) Genoa\n3) Parma\n\n",
    "In Spanish football, what is the 'Pichichi'?\n1) The award given to the best goalkeeper\n2) The award given to the best player\n3) The award given to the top goalscorer\n\n",
    "In the video game 'FIFA 20', team Piemonte Calcio represents which real-life club?\n1) Juventus\n2) Milan\n3) Inter Milan\n\n",
    "Which MLS franchise team does David Beckham own?\n1) New York Red Bulls\n2) Inter Miami\n3) Orlando City\n\n"
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
    FootballQuizQuestion(football_question_prompts[9], 1),
    FootballQuizQuestion(football_question_prompts[10], 2),
    FootballQuizQuestion(football_question_prompts[11], 3),
    FootballQuizQuestion(football_question_prompts[12], 1),
    FootballQuizQuestion(football_question_prompts[13], 2),
    FootballQuizQuestion(football_question_prompts[14], 3),
    FootballQuizQuestion(football_question_prompts[15], 1),
    FootballQuizQuestion(football_question_prompts[16], 2),
    FootballQuizQuestion(football_question_prompts[17], 3),
    FootballQuizQuestion(football_question_prompts[18], 1),
    FootballQuizQuestion(football_question_prompts[19], 2),
    FootballQuizQuestion(football_question_prompts[20], 3),
    FootballQuizQuestion(football_question_prompts[21], 1),
    FootballQuizQuestion(football_question_prompts[22], 2),
    FootballQuizQuestion(football_question_prompts[23], 3),
    FootballQuizQuestion(football_question_prompts[24], 1),
    FootballQuizQuestion(football_question_prompts[25], 2),
    FootballQuizQuestion(football_question_prompts[26], 3),
    FootballQuizQuestion(football_question_prompts[27], 1),
    FootballQuizQuestion(football_question_prompts[28], 2),
    FootballQuizQuestion(football_question_prompts[29], 3),
    FootballQuizQuestion(football_question_prompts[30], 1),
    FootballQuizQuestion(football_question_prompts[31], 2),
    FootballQuizQuestion(football_question_prompts[32], 3),
    FootballQuizQuestion(football_question_prompts[33], 1),
    FootballQuizQuestion(football_question_prompts[34], 2),
    FootballQuizQuestion(football_question_prompts[35], 3),
    FootballQuizQuestion(football_question_prompts[36], 1),
    FootballQuizQuestion(football_question_prompts[37], 2),
    FootballQuizQuestion(football_question_prompts[38], 3),
    FootballQuizQuestion(football_question_prompts[39], 1),
    FootballQuizQuestion(football_question_prompts[40], 2),
    FootballQuizQuestion(football_question_prompts[41], 3),
    FootballQuizQuestion(football_question_prompts[42], 1),
    FootballQuizQuestion(football_question_prompts[43], 2),
    FootballQuizQuestion(football_question_prompts[44], 3),
    FootballQuizQuestion(football_question_prompts[45], 1),
    FootballQuizQuestion(football_question_prompts[46], 2),
    FootballQuizQuestion(football_question_prompts[47], 3),
    FootballQuizQuestion(football_question_prompts[48], 1),
    FootballQuizQuestion(football_question_prompts[49], 2),
    FootballQuizQuestion(football_question_prompts[50], 3),
    FootballQuizQuestion(football_question_prompts[51], 1),
    FootballQuizQuestion(football_question_prompts[52], 2),
    FootballQuizQuestion(football_question_prompts[53], 3),
    FootballQuizQuestion(football_question_prompts[54], 1),
    FootballQuizQuestion(football_question_prompts[55], 2),
    FootballQuizQuestion(football_question_prompts[56], 3),
    FootballQuizQuestion(football_question_prompts[57], 1),
    FootballQuizQuestion(football_question_prompts[58], 2),
    FootballQuizQuestion(football_question_prompts[59], 3),
    FootballQuizQuestion(football_question_prompts[60], 1),
    FootballQuizQuestion(football_question_prompts[61], 2),
    FootballQuizQuestion(football_question_prompts[62], 3),
    FootballQuizQuestion(football_question_prompts[63], 1),
    FootballQuizQuestion(football_question_prompts[64], 2),
    FootballQuizQuestion(football_question_prompts[65], 3),
    FootballQuizQuestion(football_question_prompts[66], 1),
    FootballQuizQuestion(football_question_prompts[67], 2),
    FootballQuizQuestion(football_question_prompts[68], 3),
    FootballQuizQuestion(football_question_prompts[69], 1),
    FootballQuizQuestion(football_question_prompts[70], 2),
    FootballQuizQuestion(football_question_prompts[71], 3),
    FootballQuizQuestion(football_question_prompts[72], 1),
    FootballQuizQuestion(football_question_prompts[73], 2),
    FootballQuizQuestion(football_question_prompts[74], 3),
    FootballQuizQuestion(football_question_prompts[75], 1),
    FootballQuizQuestion(football_question_prompts[76], 2),
    FootballQuizQuestion(football_question_prompts[77], 3),
    FootballQuizQuestion(football_question_prompts[78], 1),
    FootballQuizQuestion(football_question_prompts[79], 2)
]

# Sample method to get a random sample list of 10 questions from the main list
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


# Call the run_football_quiz function
# Pass the list of question objects into it
run_football_quiz(sample)

# While loop to offer the user the option to play again
# Also to validate the user's input
while True:
    # Variable for user's input - a lower method is used to convert input
    # into lowercase so it matches the required y/n user input
    play_again = str.lower(input("Play again (y/n)?\n"))
    # If statement to run the game again or exit it, and to validate the data
    if play_again == "y":
        sample = random.sample(football_questions_and_answers, 10)
        run_football_quiz(sample)
    elif play_again == "n":
        # To exit the code safely
        raise SystemExit("\nThank you for playing!\n")
    else:
        print("Please enter 'y' or 'n'.\n")
        continue
