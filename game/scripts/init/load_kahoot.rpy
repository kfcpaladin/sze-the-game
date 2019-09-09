default kahoot = load_kahoot_questions()
default themes.kahoot = load_kahoot_theme()

init -1 python:
    from views.kahoot import KahootViewController

    def load_kahoot_questions():
        from models.kahoot import Question, Answer

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
    
    def load_kahoot_theme():
        theme = object()
        theme.background        = Color((242, 242, 242))
        theme.font              = "Montserrat.ttf"
        
        theme.title_background  = Color((255, 255, 255))
        theme.title_text        = Color((51, 51, 51))

        theme.primary_accent    = Color((134, 75, 191)) # purple
        theme.secondary_accent  = Color((69, 162, 229)) # blue

        theme.red =     Color((226, 27, 60))
        theme.blue =    Color((18, 104, 205))
        theme.yellow =  Color((216, 158, 0))
        theme.green =   Color((42, 143, 13))

        theme.light_text = Color((255, 255, 255))
        theme.dark_text  = Color((51, 51, 51))

        return theme
