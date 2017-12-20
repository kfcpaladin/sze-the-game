# Optimised Sze the Game

This version of "Sze the Game" aims to improve the syntax of the code, to make scripting in the renpy language much easier and more maintainable. This branch makes the following modifications to the version of the game in master and nub:

1. Restructures the /game directory so that it is easier to manage:
...* classes:   Stores python scripts containing the classes 
...* images:    Stores the images declared by default in renpy
...* instances: Stores pythons scripts which initialise all the instances
...* music:     Custom directory declarable through options.rpy in /game/scripts
...* scripts:   Where you place renpy scripts not related to story
...* story:     Specialised directory used to store all the narratives

2. Introduces