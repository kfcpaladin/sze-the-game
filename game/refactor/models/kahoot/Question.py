import random

class Question(object):
    def __init__(self, description):
        self.description = description
        self._answers = []

    @property
    def answers(self):
        return random.sample(self._answers, len(self._answers))

    def add_answer(self, answer):
        self._answers.append(answer)

