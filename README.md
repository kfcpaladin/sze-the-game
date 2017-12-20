# Optimised Sze the Game

This version of "Sze the Game" aims to improve the syntax of the code, to make scripting in the renpy language much easier and more maintainable. 

## Changes

1. Restructures the /game directory so that it is easier to manage  
2. Introduces subclasses to the ADVCharacter used in master/nub to offer specialisation
3. Uses an updated renpy engine *(20/12/2017)*

## Game directory layout

| Folder        | Description                                                       |
| ------------- | ----------------------------------------------------------------- |
| **classes**   | Stores python scripts containing the classes                      |
| **images**    | Stores the images declared by default in renpy                    |
| **instances** | Stores pythons scripts which initialise all the instances         |
| **music**     | Custom directory declarable through options.rpy in /game/scripts  |
| **scripts**   | Where you place renpy scripts not related to story                |
| **story**     | Specialised directory used to store all the narratives            |

## New classes and instances
### Class descriptions

| Class             | Description                                                                       |
| ----------------- | --------------------------------------------------------------------------------- |
| **ADVCharacter**  | Subclass of renpy's default object, and returned in Character(...) *(deprecated)* |
| **MainCharacter** | Subclass of renpy's ADVCharacter, and supports multiple attributes                |
| **Friend**        | Subclass of renpy's ADVCharacter and has loss() and gain() methods for friendship |
| **Game**          | Unique object used to store all the game variables, and includes debugger         |

### Instances

| Class             | Instance names  |
| ----------------- | --------------- |
| **MainCharacter** | sze             |
| **Friend**        | ale, bil, but, cha, dea, dik, dng, drk, flu, gra, jit, kok, lee, mox, pra, rin, roy, rus, slm, tod, wil, wiy |
| **Game**          | game            |

### Usage inside renpy script

For friends, you would previously you would do **call rusgainloss from _label** in order to increment or decrement the friendship of a character. Using the new class methods you can instead do **$ rus.gain()** or **$ rus.loss()**

For sze, his attributes were stored in global python variables, and his messages were stored in a series of if, elif and else statements. You can now perform the following:

* **setting attributes**: $ sze.setAttributes(*dict*)
* **accessing attributes**: $ sze.strength, $ sze.intellect, *etc*
* **setting tutorial messages**: $ sze.setTutorials(*dict*)
* **setting introductory attribute messages**: $ sze.setAttributeIntroMessages(*dict*)
* **setting attribute status messages**: $ sze.setAttributeMessages(*dict*)

For more information check out [**game/instances/**](https://github.com/kfcpaladin/sze-the-game/tree/orphan/game/instances) to see how all of this is implemented

## Updated renpy engine

**Bugs that were fixed**:
* Able to use the *call* function without needing the *from* sub-statement

**Features that were added**:


