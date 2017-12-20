# Optimised Sze the Game

This version of "Sze the Game" aims to improve the syntax of the code, to make scripting in the renpy language much easier and more maintainable. 
Since this is essentially a new version of the game, don't attempt to merge it with any of the other branches.

**Autotest**: [*Click here for the Travis autotest*](https://travis-ci.org/kfcpaladin/sze-the-game/branches)

## Changes

1. Restructures the /game directory so that it is easier to manage  
2. Introduces subclasses to the ADVCharacter used in master/nub to offer specialisation
3. Uses an updated renpy engine *(20/12/2017)*
4. Added redirectable music directory

## Game directory layout

| Folder                                                                              | Description                                                       |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| [classes](https://github.com/kfcpaladin/sze-the-game/tree/orphan/game/classes)      | Stores python scripts containing the classes                      |
| [images](https://github.com/kfcpaladin/sze-the-game/tree/orphan/game/images)        | Stores the images declared by default in renpy                    |
| [instances](https://github.com/kfcpaladin/sze-the-game/tree/orphan/game/instances)  | Stores pythons scripts which initialise all the instances         |
| [music](https://github.com/kfcpaladin/sze-the-game/tree/orphan/game/music)          | Custom directory declarable through options.rpy in /game/scripts  |
| [scripts](https://github.com/kfcpaladin/sze-the-game/tree/orphan/game/scripts)      | Where you place renpy scripts not related to story                |
| [story](https://github.com/kfcpaladin/sze-the-game/tree/orphan/game/story)          | Specialised directory used to store all the narratives            |

## New classes and instances
### Class descriptions

| Class                                                                                                   | Description                                                                       |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [ADVCharacter](https://github.com/kfcpaladin/sze-the-game/tree/orphan/renpy/character.py#L583)          | Subclass of renpy's default object, and returned in Character(...) *(deprecated)* |
| [MainCharacter](https://github.com/kfcpaladin/sze-the-game/tree/orphan/game/classes/MainCharacter.rpy)  | Subclass of renpy's ADVCharacter, and supports multiple attributes                |
| [Friend](https://github.com/kfcpaladin/sze-the-game/tree/orphan/game/classes/Friend.rpy)                | Subclass of renpy's ADVCharacter and has loss() and gain() methods for friendship |
| [Game](https://github.com/kfcpaladin/sze-the-game/tree/orphan/game/classes/Game.rpy)                    | Unique object used to store all the game variables, and includes debugger         |

### Instances

| Class         | Instance names  |
| ------------- | --------------- |
| MainCharacter | [sze](https://github.com/kfcpaladin/sze-the-game/tree/orphan/game/instances/sze.rpy)  |
| Friend        | [ale, bil, but, cha, dea, dik, dng, drk, flu, gra, jit, kok, lee, mox, pra, rin, roy, rus, slm, tod, wil, wiy](https://github.com/kfcpaladin/sze-the-game/tree/orphan/game/instances/friends.rpy) |
| Game          | [game](https://github.com/kfcpaladin/sze-the-game/tree/orphan/game/instances/game.rpy)|

### Usage inside renpy script

#### Friends
Previously you would do **call rusgainloss from _label** in order to increment or decrement the friendship of a character. Using the new class methods you can instead do **$ rus.gain()** or **$ rus.loss()**

#### Arthur Sze
Previously his attributes were stored in global python variables, and his messages were stored in a series of if, elif and else statements. You can now perform the following:

* **setting attributes**: $ sze.setAttributes(*dict*)
* **accessing attributes**: $ sze.strength, $ sze.intellect, *etc*
* **setting tutorial messages**: $ sze.setTutorials(*dict*)
* **setting introductory attribute messages**: $ sze.setAttributeIntroMessages(*dict*)
* **setting attribute status messages**: $ sze.setAttributeMessages(*dict*)

#### Game
The master/nub branches used global variables to keep track of game states, such as *moxcounter*, *metderek*, *etc*. Now this is consolidated inside a game object, which also has a debugging method to preview the game state during execution. 

* **setting gamestate varaible**: $ game = Game(*dict*)
* **accessing gamestate variable**: $ game.moxCounter, $ game.timeTravelCounter, *etc*
* **debug the current gamestate**: $ game.describe() *(information is printed to console)*

*Note*: For more information check out [**game/instances/**](https://github.com/kfcpaladin/sze-the-game/tree/orphan/game/instances) to see how all of this is implemented

## Updated renpy engine

**Bugs that were fixed**:
* Able to use the *call* function without needing the *from* sub-statement

**Features that were added**:


## Configurable music directory

Previously you were not able to define the directory in which all your audio files were. As a result, you either had to directly enter the full path of the audio file when playing it or keep it in game/.
Using the new **playmusic()** and **stopmusic()** functions you should be able to play music from a user defined directory stored in **musicdir**

*Note*: The settings for audio are located in [game/scripts/sound.rpy](https://github.com/kfcpaladin/sze-the-game/blob/orphan/game/scripts/sound.rpy)


