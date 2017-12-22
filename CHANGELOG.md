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