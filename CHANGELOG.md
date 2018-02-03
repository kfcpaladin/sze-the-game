# Change log

Any major changes or bug fixes you make to the game should be noted in this change log. 
The standard format for a changelog is the date as a title, followed by bullet points of the changes that were made.

**20/12/2017**
* Completed initial draft of new version
* Fixed incorrect variable names that occurred during conversion to new format
* Added a readme
* Changed implementation of configurable music directories to preserve core renpy files so that Travis autotest can be done
* Added playmusic() and stopmusic() functions to replace *play music* and *stop music* so that directory of audio files can be configurable

**21/12/2017**
* Added a change log
* Increased the complexity of the Friend class to add support for multiple attributes and messages
* Created a new directory for sfx files
* Added support for sfx files
* Included vpunch.ogg and hpunch.ogg in game/sfx for fight scenes
* Added stopsfx() to stop sfx sounds on the "sound" channel
* Added more features to the Valley easter egg
* Added the WIP inventory system to the game
* Started adding quest support

**22/12/2017**
* Broke down the large screens.rpy file into multiple .rpy files and stored them under scripts/
* Made massive changes to the quest system, and features 4 distinct quest branches *(unavailable, available, ongoing, completed)*
* Made massive changes to the quest screen, and can now accept available quests, and complete ongoing quests
* Finished the kahoot gamemode in */game/scripts/countdown.rpy*
* Added temporary placeholder dialogue for "econ1"

**23/12/2017**
* Made massive changes to the inventory system, now it uses the diary as the background
* Added support for 5x5 grid as the inventory system
* Change inventory.rpy to bag.rpy since a bag and locker will have significantly different layouts
* Items can now be equipped and unequipped, and will provide stats
* Added the greatest item in the history of the future of man

**24/12/2017**
* Added pong to the game

**10/01/2018**
* Added custom floating Arthur head cursor

**16/01/2018**
* Added stat screen for attributes and friends
* Added achievement system
* Added achievement screen
* Change kms screen to interactive gun suicide
* Fixed pong physics and added custom physics timescale for smoother gameplay
* Fixed incorrect image dimensions
* Added better minigame support to the developer console page
* Made significant changes to pong game, including a new Pong class for better abstraction
* Integrated all pages of the diary into the diary button available during gameplay
* Restructed the game/images/ folder for better expandability in the future

**17/01/2018**
* Added icons to quests and achievements
* Restructured audio and image directories to make it easier to classify images
* Now uses loadImage(...) and loadAudio(...) to load assets in

**19/01/2018**
* Overhauled the inventory screen by adding hovering tooltips, and statistics screen
* Added statistics screen to the quest and achievements pages
* Made significant overhaul to the popup system, including adding a PopUp class
* Popups now support icons, and have a better aesthetic
* Added a logCache() function to show the status of the file caches
* Added autosave function to the game

**22/01/2018**
* Fixed path issues regarding windows and os.sep = "\\" instead of "/"
* Move extraneous classes to game/classes including Vector.rpy, AttrDict.rpy, CodeSequence.rpy, Colours.rpy
* Added developer unlock code, which is "godmode"

**24/01/2018**
* Made gun in kms screen shoot bullets
* Added Todd quest line
* Finished 7.0 english.rpy story file

**27/01/2018**
* Added AdvancedColour class, for support with colour mixing, inversion and alpha changes

**28/01/2018**
* Added a RainbowColour class and ChangingRainbowColour class for rainbow styled UI
* Made autosave and developer unlocks use the new ChangingRainbowClass
* Added rainbowText(...) text formatter to create rainbow styled text

**1/02/2018**
* Added sizeText(...) to allow for text size to change between a min and max
* Added formatting support to rainbowText() and sizeText() to allow for {tag} to be used
* Added examples in the diary intro sequence, and the demonstration Todd quest
* Made the initialisation of classes more discrete at a default of -10
* Removed roadmap from base game since it is not complete

**2/02/2018**
* Changed the pong minigame to use the renpy.Displayable class, which offers significant performance increases
