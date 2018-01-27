# Optimised Sze the Game

This version of "Sze the Game" aims to improve the syntax of the code, to make scripting in the renpy language much easier and more maintainable. 
Since this is essentially a new version of the game, don't attempt to merge it with any of the other branches.

**Autotest**: [*Click here for the Travis autotest*](https://travis-ci.org/kfcpaladin/sze-the-game/branches)

**Changelog**: [*Any changes should be noted in the changelog*](./CHANGELOG.md)

## Changes

1. Restructures the /game directory so that it is easier to manage  
2. Introduces subclasses to the ADVCharacter used in master/nub to offer specialisation
3. Uses an updated renpy engine to [*renpy-6.99.13*](https://www.renpy.org/dl/6.99.13/)
4. Added redirectable audio subdirectories for better global audio classification (*allows for better classification*)
5. Added redirectable image subdirectories for better global image classification (*allows for better classification*)
6. Added achievements, quests, inventory, items, statistics screen, and a diary
7. Added minigames, including *pong, kahoot*
8. Added complex popup system with smooth transitions

## Game directory layout

| Folder                         | Description                                                       |
| ------------------------------ | ----------------------------------------------------------------- |
| [audio](./game/audio)          | Stores all audio files, and is customisable                       |
| [classes](./game/classes)      | Stores python scripts containing the classes                      |
| [images](./game/images)        | Stores the images declared by default in renpy                    |
| [instances](./game/instances)  | Stores pythons scripts which initialise all the instances         |
| [minigames](./game/minigames)  | Stores all minigames used inside the game                         |
| [screens](./game/screens)      | Folder dedicated for gui renpy script files                       |
| [scripts](./game/scripts)      | Where you place renpy scripts not related to story                |
| [story](./game/story)          | Specialised directory used to store all the narratives            |

## New classes and instances
### Class descriptions

| Class                                              | Description                                                                       |
| -------------------------------------------------- | --------------------------------------------------------------------------------- |
| [ADVCharacter](./renpy/character.py#L583)          | Subclass of renpy's default object, and returned in Character(...) *(deprecated)* |
| [Achievements](./game/classes/Achievement.rpy)     | Used to store, add and update achievements in realtime using the gameloop         |
| [AdvancedColour](./game/classes/Colours.rpy)       | Allow for making of hex code colours using RGB, and a selection of default colours|
| [AttrDict](./game/classes/AttrDict.rpy)            | Used as a wrapped for the python dict, allowing for access like JSON object       |
| [Bullet](./game/classes/Bullet.rpy)                | Used by the kmsGun screen for the gun projectiles                                 |
| [CodeSequence](./game/classes/CodeSequence.rpy)    | Used for easter eggs, where things can be unlocked using a code sequence          |
| [Diary](./game/classes/Diary.rpy)                  | Class used to store and manage all diary pages                                    |
| [Friend](./game/classes/Friend.rpy)                | Subclass of renpy's ADVCharacter and has loss() and gain() methods for friendship |
| [Game](./game/classes/Game.rpy)                    | Unique object used to store all the game variables, and includes debugger         |
| [Inventory](./game/classes/Inventory.rpy)          | Used as a manager of **Item** instances, and communicated with inventory screen   |
| [Item](./game/classes/Item.rpy)                    | Stores information about an item, most notably statistic changes to a character   |
| [MainCharacter](./game/classes/MainCharacter.rpy)  | Subclass of renpy's ADVCharacter, and supports multiple attributes                |
| [PopUp](./game/classes/PopUp.rpy)                  | Stores all popups, and manages their lifetime                                     |
| [Quest](./game/classes/Quest.rpy)                  | Used to store, add and push quests as the game progress                           |
| [Vector](./game/classes/Vector.rpy)                | Used by pong, and various game screens, for position and sizes of objects         |

### Instances

| Class         | Instance names  |
| ------------- | --------------- |
| Achievements  | [achievements](./game/instances/achievements.rpy) |
| AdvancedColour| [colour](./game/instances/colour.rpy) |
| Diary         | [diary](./game/instances/diary.rpy)   |
| Friend        | [ale, bil, but, cha, dea, dik, dng, drk, flu, gra, jit, kok, lee, mox, pra, rin, roy, rus, slm, tod, wil, wiy](./game/instances/friends.rpy) |
| Game          | [game](./game/instances/game.rpy)     |
| Inventory     | [bag](./game/instances/inventory.rpy) |
| Item          | [{itemList}](./game/instances/items.rpy)|
| MainCharacter | [sze](./game/instances/sze.rpy)       |
| PopUp         | [popupList](./games/instances/popup.rpy) |
| Quest         | [quests](./game/instances/quests.rpy) |

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

#### Diary
The Diary class is used to keep track and store information about the current diary configuration. 
In the future, more complex behaviour can be added to the diary, such as page lockouts and conditional unlocking of pages.

* **Initialising a diary**: $ diary = Diary(*dict*)

#### Quest
This is a class used to store the relevant quests used throughout the story. 
It will contain methods to add and remove quests, and will be used as the backend for a frontend gui written in renpy.

* **Adding a quest**: $ quests.addQuests(*dict* or *list*)
* **Removing a quest**: $ quests.completeQuest(*index*)
* **Debugging current quests**: $ quests.debugQuests()  *(information is printed to console)*  

#### Achievement
Class that is similar to the Quest class, but is designed specifically for an achievement system.
It contains methods to add achievements, and to check all achievements to see if their requirements have been met.

* **Adding an achievement**: $ achievements.addAchievements(*dict* or *list*)
* **Updating all quests**: $ achievements.updateAchievements()
* **Debugging all achievements**: $ achievements.debugAchievements()  *(information is printed to console)*

#### Inventory
This will be intended to be used to store **Item** instances, and manage them during the game.
The **inventory** screen will communicate with the inventory instance, to display and equip particular
items that are selected

#### Item
Possesses information about an item, including its *statistics*, *icon*, and *etc*.

* **Equiping an item**: $ item.equip()
* **Unequpping an item**: $ item.unequip()

#### PopUp
Stores and manages all messages for the popup system

* **Adding a popup**: $ popupList.add(*string* or *dict* or *list*)
* **Clearing all popups**: $ popupList.clear()

*Note*: For more information check out [**game/instances/**](./game/instances) to see how all of this is implemented

## Updated renpy engine

**Bugs that were fixed**:
* Able to use the *call* function without needing the *from* sub-statement

**Features that were added**:


## Configurable music directory

| Sound type            | Channel | Description                                                                   |
| --------------------- | ------- | ----------------------------------------------------------------------------- |
| [Music](./game/music) | music   | Plays music from configured directory. Loops by default.                      |
| [SFX](./game/sfx)     | sound   | Plays sfx sounds from selected directory. Doesn't loop and cannot be stopped. |

Previously you were not able to define the directory in which all your audio files were. As a result, you either had to directly enter the full path of the audio file when playing it or keep it in game.

Using the new **playmusic()** and **stopmusic()** functions you should be able to play music from a user defined directory stored in **musicdir**.
For special effect sounds, use **playsfx()** to play a short audio clip and **stopsfx()** to stop it.

*Note*: The settings for audio are located in [**game/scripts/sound.rpy**](./game/scripts/sound.rpy)

## Multiple screens

| Screen name                                                   | Description                                                                       |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [screen_achievement](./game/screens/screen_achievement.rpy)   | Used to display all achievements                                                  |
| [screen_bag](./game/screens/screen_bag.rpy)                   | Used for the bag inventory                                                        |
| [screen_barGraph](./game/screens/screen_barGraph.rpy)         | A frame containing a bar graph, used by all statistics screens                    |
| [screen_default](./game/screens/screen_default.rpy)           | The default configuration file for all renpy menus (*customizable*)               |
| [screen_developer](./game/screens/screen_developer.rpy)       | Houses the developer page which allows access to all labels, times and minigames  |
| [screen_diary](./game/screens/screen_diary.rpy)               | Contains all diary screens, and selects most recent diary screen                  |
| [screen_float_menu](./game/screens/screen_float_menu.rpy)     | A menu that is present to access the diary and suicide screen                     |
| [screen_fortmap](./game/screens/screen_fortmap.rpy)           | Has a map of the school used to navigate to different locations                   |
| [screen_game_loop](./game/screens/screen_game_loop.rpy)       | Updates every few seconds, and calls the gameLoop function                        |
| [screen_kms](./game/screens/screen_kms.rpy)                   | Arthur uses this to kill himself                                                  |
| [screen_popup](./game/screens/screen_popup.rpy)               | Will display a popup message/s, useful for achievements and quest unlocks         |
| [screen_quests](./game/screens/screen_quests.rpy)             | Shows the available and completed quests, and allows user to start quests         |
| [screen_quickmenu](./game/screens/screen_quickmenu.rpy)       | Configures the bottom menu that is present during normal interaction              |
| [screen_roadmap](./game/screens/screen_roadmap.rpy)           | Will be used to display a graph of choices made by the user                       |
| [screen_szeclicker.rpy](./game/screens/screen_szeclicker.rpy) | *A cookie clicker minigame?*                                                      |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [screen_pong](./game/minigames/pong/screen_pong.rpy)          | Main screen used for the pong minigame                                            |
| [screen_kahoot](./game/minigames/kahoot/screen_kahoot.rpy)    | Main screen used for the kahoot minigame (*in development*)                       |

*Note*: For more information about the structure and implementation of screens, check out [**game/screens/**](./game/screens)

## Minigames

| Minigame name                       | Description                                           |
| ----------------------------------- | ----------------------------------------------------- |
| [Pong](./game/minigames/pong)       | This will be played in the tennis courts, rowe, etc   |
| [Kahoot](./game/minigames/kahoot)   | This will play kahoot                                 |
