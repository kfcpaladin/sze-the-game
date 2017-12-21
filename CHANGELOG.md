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
