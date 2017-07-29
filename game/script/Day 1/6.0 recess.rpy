label recess1:
    "As you leave assembly hall you see a shadow fleeting across Kilgour Quad"
    jit "\"Sup sze, How was assembly? Should've jigged with me, I never get caught\""
    "It is now recess, which has unfortunately been cut short to 10 minutes to due an extended assembly"
    sze "Hmm, what should I do today for recess"
    call screen fortmap
    if _return == 1:
        "Rowe"
    elif _return == 2:
        "Kilgour"
    elif _return == 3:
        "R Quad"
    elif _return == 4:
        "Library"
    elif _return == 5:
        "Gym"
    elif _return == 6:
        "Food"
    elif _return == 7:
        "Valley"
    elif _return == 8:
        "Oval"
    elif _return == 9:
        "Curry courts"
    elif _return == 10:
        "B-Courts"
    elif _return == 11:
        "Carpark"
    elif _return == 12:
        "Fort Street"
    elif _return == 13:
        "Bridge"
    elif _return == 14:
        "Place"
    elif _return == 15:
        "Wilkins"
    elif _return == 16:
        "Fountain Quad"
    elif _return == 17:
        "Cohen"
    elif _return == 18:
        "Hall"
    elif _return == 19:
        "Lower Kilgour Quad"
    elif _return == 20:
        "Lower Kilgour"
    elif _return == 21:
        "Upper Kilgour Quad"