default kahoot = load_kahoot_questions()

init -1 python:
    def load_kahoot_questions():
        from refactor.models.kahoot import Question, Answer

        kahoot = {}

        question = Question(description="Which country has the longest uninterrupted economic growth?")
        question.add_answer(Answer("Australia", 1))
        question.add_answer(Answer("US", 1))
        question.add_answer(Answer("China", 1))
        question.add_answer(Answer("Uganda", 1))
        kahoot["econ1"] = question

        question = Question(description="What is the optimal cash rate?") 
        question.add_answer(Answer("-5%", 0))
        question.add_answer(Answer("1%", 0))
        question.add_answer(Answer("2-3%", 1))
        question.add_answer(Answer("10%", 0))
        kahoot["econ2"] = question

        question = Question(description="What is objectively the greatest graph?")
        question.add_answer(Answer("Keynesian Cross", 1))
        question.add_answer(Answer("Sub-Saharan African Curve", 0))
        question.add_answer(Answer("PPC Cross", 0))
        question.add_answer(Answer("Supply and Demand Model", 0))
        kahoot["econ3"] = question

        question = Question(description="Which nation is Australia's 4th largest trade partner in terms of volume?")
        question.add_answer(Answer("China", 0))
        question.add_answer(Answer("US", 0))
        question.add_answer(Answer("New Zealand", 0))
        question.add_answer(Answer("Korea", 1))
        kahoot["econ4"] = question

        return kahoot
