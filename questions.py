# Importing modules and shortcuts from shortcuts.py
import html
import requests
import base64
from random import shuffle, randint
from shortcuts import wait, wait_long, clear, new_line

class Questions:

    # Ask for the desired number of questions and difficulty level, uses those parameters to pull questions from OpenTriviaDB
    def __init__(self):
        self.num_of_questions = int(input("How many questions do you want? "))
        new_line()
        self.difficulty_level = input("What difficulty do you want? (easy/medium/hard) ").lower().strip()
        if (self.difficulty_level != "hard") and (self.difficulty_level != "medium") and (self.difficulty_level != "easy"):
            self.difficulty_level = "hard"

    def new_questions(self):
        self.questions = requests.get("https://opentdb.com/api.php", params={"amount": self.num_of_questions, "difficulty": self.difficulty_level}).json()['results']
        for question in self.questions:
            question['type'] = html.unescape(question['type'])
            question['difficulty'] = html.unescape(question['difficulty'])
            question['category'] = html.unescape(question['category'])
            question['question'] = html.unescape(question['question'])
            question['correct_answer'] = html.unescape(question['correct_answer'])
            for n in range(0, len(question['incorrect_answers'])):
                question['incorrect_answers'][n] = html.unescape(question['incorrect_answers'][n])
        new_line()
        print("Creating questions...")
        wait()

    # Asks the current player a question
    def ask_questions(self):
        num_correct_questions = 0
        num_incorrect_questions = 0
        for n in range(0, len(self.questions)):
            clear()
            question = self.questions[n]['question']
            correct_answer = self.questions[n]['correct_answer']
            incorrect_answers = self.questions[n]['incorrect_answers']
            category = self.questions[n]['category']
            difficulty = self.questions[n]['difficulty']
            type = self.questions[n]['type']

            if type == "multiple":
                possible_answers = [correct_answer]
                possible_answers.extend(incorrect_answers)
                shuffle(possible_answers)
            else:
                possible_answers = ["True", "False"]

            print(f"Category: {category}\nDifficulty: {difficulty.upper()}")
            new_line()
            if type == "multiple":
                player_answer = input(f"{n + 1}. {question}\n\nA. {possible_answers[0]}\nB. {possible_answers[1]}\nC. {possible_answers[2]}\nD. {possible_answers[3]}\n\nAnswer: ")
            else:
                player_answer = input(f"{n + 1}. {question}\n\nTrue\nFalse\n\n")
            player_answer = player_answer.capitalize().strip()
            if not (player_answer == "A" or player_answer == "B" or player_answer == "C" or player_answer == "D" or player_answer == "True" or player_answer == "False"):
                if type == "multiple":
                    random = randint(0, 3)
                    if random == 0:
                        player_answer = "A"
                    elif random == 1:
                        player_answer = "B"
                    elif random == 2:
                        player_answer = "C"
                    elif random == 3:
                        player_answer = "D"
                else:
                    random = randint(0, 1)
                    if random == 0:
                        player_answer = "True"
                    elif random == 1:
                        player_answer = "False"

            new_line()
            if player_answer == "A" and correct_answer == possible_answers[0]:
                print(f"Correct, the answer was {player_answer}!")
                num_correct_questions += 1
            elif player_answer == "B" and correct_answer == possible_answers[1]:
                print(f"Correct, the answer was {player_answer}!")
                num_correct_questions += 1
            elif player_answer == "C" and correct_answer == possible_answers[2]:
                print(f"Correct, the answer was {player_answer}!")
                num_correct_questions += 1
            elif player_answer == "D" and correct_answer == possible_answers[3]:
                print(f"Correct, the answer was {player_answer}!")
                num_correct_questions += 1
            elif player_answer == "True" and correct_answer == possible_answers[0]:
                print(f"Correct, the answer was {player_answer.lower()}!")
                num_correct_questions += 1
            elif player_answer == "False" and correct_answer == possible_answers[1]:
                print(f"Correct, the answer was {player_answer.lower()}!")
                num_correct_questions += 1
            else:
                correct_letter = ""
                if correct_answer == possible_answers[0]:
                    if type == "multiple":
                        correct_letter = "A"
                    else:
                        correct_letter = "true"
                elif correct_answer == possible_answers[1]:
                    if type == "multiple":
                        correct_letter = "B"
                    else:
                        correct_letter = "false"
                elif correct_answer == possible_answers[2]:
                    correct_letter = "C"
                elif correct_answer == possible_answers[3]:
                    correct_letter = "D"
                num_incorrect_questions += 1
                print(f"Wrong, the answer was {correct_letter}.")
            wait_long()
        return {"correct_answers": num_correct_questions, "incorrect_answers": num_incorrect_questions}