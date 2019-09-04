import random

class Question(object):
    def __init__(self, description, image=None):
        self.description = description
        self.image = image
        self._answers = []

    @property
    def answers(self):
        return random.sample(self._answers, len(self._answers))

    def add_answer(self, answer):
        self._answers.append(answer)

