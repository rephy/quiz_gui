import requests
import html

class Questions:

    def __init__(self):
        self.questions = requests.get(url="https://opentdb.com/api.php", params={"type": "boolean", "amount": 2 ** 64}).json()['results']

    def get_question(self):
        question = self.questions[0]
        self.questions = self.questions[1:]

        question['category'] = html.unescape(question['category'])
        question['question'] = html.unescape(question['question'])

        return question