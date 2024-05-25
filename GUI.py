from tkinter import *

class Gui:

    def __init__(self, current_score, high_score):
        self.window = Tk()
        self.window.minsize(width=600, height=600)
        self.window.config(padx=30, pady=30)
        self.window.title('Quizzler - by Raphael Manayon')

        self.score_display = Label(text=f"Score: {current_score}")
        self.score_display.config(padx=570/4, pady=30)
        self.score_display.grid(column=0, row=0, columnspan=1)

        self.high_score_display = Label(text=f"High Score: {high_score}")
        self.high_score_display.config(padx=570/4, pady=30)
        self.high_score_display.grid(column=1, row=0, columnspan=1)

        self.card = Canvas(width=500, height=300)
        self.question = self.card.create_text(250, 150, text=f"Question", fill="black", width = 470)
        self.card.config(bg="white")
        self.card.grid(column=0, row=1, columnspan=2)

        self.false_button = Button(text="False")
        self.false_button.grid(column=0, row=2)

        self.true_button = Button(text="True")
        self.true_button.grid(column=1, row=2)

        self.players_button = Button(text="List of All Players")
        self.players_button.grid(column=0, row=3, columnspan=2)

    def change_question(self, new_question):
        self.card.itemconfig(self.question, text=new_question)

    def display_correct(self):
        self.change_question("Correct!")

    def display_wrong(self, actual_answer):
        self.change_question(f"Wrong, the actual answer is {actual_answer.lower()}.")

    def player_list(self, list):
        self.list_window = Tk()
        self.list_window.geometry("300x300")
        self.list_window.title("Player List")
        label = Label(self.list_window, text=list)
        label.pack()

        self.list_window.mainloop()