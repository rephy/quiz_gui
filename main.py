import json
import os

from prettytable import PrettyTable

import easygui

from GUI import Gui
from questions import Questions

current_score = 0
high_score = 0

name = easygui.enterbox("What is your name?", title="Your Name")

try:
    scores_file = open("scores.json", "r")
except FileNotFoundError:
    scores_file = open("scores.json", "r")
    scores_file.close()

    scores_file = open("scores.json", "w")
    scores_file.write("{}")
    scores_file.close()

try:
    scores_file = open("scores.json", "r")
    current_data = json.load(scores_file)
    current_score = current_data[name]
except KeyError:
    scores_file.close()

    scores_file = open("scores.json", "w")
    current_data.update({name: current_score})
    json.dump(current_data, scores_file, indent=4)

    scores_file.close()

with open("scores.json", "r") as scores_file:
    current_data = json.load(scores_file)
    scores = [score for (name, score) in current_data.items()]
    for score in scores:
        if score > high_score:
            high_score = score

questions = Questions()

def update_score_displays():
    global current_score
    gui.score_display.config(text=f"Score: {current_score}")
    gui.high_score_display.config(text=f"High Score: {high_score}")

def update_score_data():
    scores_file = open("scores.json", "r")
    scores = json.load(scores_file)
    scores_file.close()

    scores_file = open("scores.json", "w")
    scores.update({name: current_score})
    json.dump(scores, scores_file, indent=4)

    scores_file.close()

def change_high_score():
    global current_score
    global high_score
    if current_score > high_score:
        high_score = current_score

def check_false():
    global current_score
    global high_score
    global question

    if question['correct_answer'] == 'False':
        current_score += 1
        change_high_score()
        gui.display_correct()
    else:
        gui.display_wrong('True')

    update_score_displays()
    question = questions.get_question()

    gui.window.after(5000, gui.change_question, question['question'])

def check_true():
    global current_score
    global high_score
    global question

    if question['correct_answer'] == 'True':
        current_score += 1
        change_high_score()
        gui.display_correct()
    else:
        gui.display_wrong('False')

    update_score_displays()
    question = questions.get_question()

    gui.window.after(5000, gui.change_question, question['question'])

def player_list():
    list = PrettyTable()
    list.field_names = ["Place", "Name", "Score"]

    with open("scores.json", "r") as scores_file:
        data = dict(json.load(scores_file))
        data = sorted(data.items(), key=lambda x: x[1], reverse=True)

    place = 1

    for (name, score) in data:
        list.add_row([place, name, score])
        place += 1

    gui.player_list(list)

change_high_score()

gui = Gui(current_score, high_score)

question = questions.get_question()
gui.change_question(question['question'])

gui.false_button.config(command=check_false)
gui.true_button.config(command=check_true)
gui.players_button.config(command=player_list)

gui.window.mainloop()
update_score_data()