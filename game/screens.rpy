# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .8

        has vbox

        add "logo.png"
        textbutton _("Start Game") action Start() xminimum 400
        null height 20
        textbutton _("Load Game") action ShowMenu("load")
        null height 20
        textbutton _("Preferences") action ShowMenu("preferences")
        null height 20
        textbutton _("Help") action Help()
        null height 20
        textbutton _("Quit") action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Stats") action ShowMenu("statsscreen")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Stats") action ShowMenu('statsscreen')
        textbutton _("kms") action ShowMenu('kms')
        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"



##############################################################################
screen kms():

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _('Kill myself?'):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action Start('deadrestart')
            textbutton _("No") action Return()

    # Right-click and escape answer "no".
    key "game_menu" action Return()

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"

###########################################################################
screen statsscreen():

    tag menu

    # Include the navigation.
    use navigation
    
    #columns in a three-wide grid
    grid 3 1:
        style_group "prefs"
        xfill True
        
        #left column
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Your stats")
                text "intelligence: [intelligence] points"
                if intelligence > 100:
                    text "You have surpassed even Justin Wu, dux of James Ruse"
                elif intelligence > 75:
                    text "Maybe you'll be able to impress Serena with your 99.95 ATAR"
                elif intelligence > 50:
                    text "A bit more hard work and you will truly ACE TRIALS"
                elif intelligence > 25:
                    text "At marginally above average intelligence"
                    text "You really shouldnt be celebrating yet"
                elif intelligence > -1:
                    text "With your remarkably average intelligence, your waifu will probably not be impressed"
                elif intelligence > -25:
                    text "You are a bit slow, should you even be in a selective school?"
                elif intelligence > -50:
                    text "Your test results are probably worse than Chao's tests for STDs"
                elif intelligence > -75:
                    text "It's astonishing how you made it to Fort Street. How many dicks did you have to suck to get here?"
                elif intelligence > -100:
                    text "With almost no brain activity, the fact that your nervous system still works is a scientific anomaly."
                    text "Hot tip: press the 'KMS' button"
                text " "
                text "charm: [charm] points"
                if charm > 100:
                    text "You slay harder than Hugh Hefner"
                    text "You slay just by looking. Gaze upon the world, your dominion"
                elif charm > 75:
                    text "With that level of charm, you have probably slayed every LG in Sydney by now"
                elif charm > 50:
                    text "You have surpassed even Chao in slaying ability; the teacher becomes the student"
                elif charm > 25:
                    text "You are just very slightly charming"
                elif charm > -1:
                    text "With such exceptionally average charm, its going to take a very long time for senpai to notice you."
                elif charm > -25:
                    text "With your charm, or lack thereof, there seems to be an invisible forcefield repelling girls from you"
                elif charm > -50:
                    text "With that much charm, you are often mistaken for a modern art piece"
                elif charm > -75:
                    text "The average gayness of every room you enter is increased by 100%, due to your charm"
                elif charm > -100:
                    text "You once tried to masturbate, your hand rejected you"
                text " "
                text "strength: [strength] points"
                if strength > 100:
                    text "You are Level S-Class 11th-dan Golden Jade Dragon Jedi Master Ninja Samurai Viking Knight Marshal Admiral"
                    text "You surpass saitama in skill"
                elif strength > 75:
                    text "With your combat propensity, you probably ended 300 spartans with a single one-inch punch."
                elif strength > 50:
                    text "Your skill in a fight would allow you to beat black-belt Aradhya and Jew-jitsu Steven."
                elif strength > 25:
                    text "With such strength, you can probs beat the average student."
                elif strength > -1:
                    text "At your level it is advised that you tactically retreat from your fights."
                elif strength > -25:
                    text "Your below average combat propensity suggests that you have a thing for being dominated."
                elif strength > -50:
                    text "At [strength] combat propensity, the only slaying you know is in Dungeons & Dragons..."
                elif strength > -75:
                    text "With that combat 'proficiency' pussies slays you."
                elif strength > -100:
                    text "Don't fight; you will get rekt so hard, you will be reincarnated as an abortion."
                text " "
                text "thirst: [thirst] points"
                if thirst > 100:
                    text "At a thirst of [thirst], you rival Tiddalik"
                elif thirst > 75:
                    text "You're so thirsty, sometimes moxham appears in your {s}dreams{/s} hallucinations"
                elif thirst > 50:
                    text "With that much thirst, like Roy, you are willing to partake in sexual activities with robots for water"
                elif thirst > 25:
                    text "Even a can of SOLO cannot crush your thirst of [thirst]"
                elif thirst > -1:
                    text "With this much thirstiness, you have the standard healthy desires of a teenage boy of your age."
                elif thirst > -25:
                    text "You have been oft compared to LiXu due to your lack of thirst"
                elif thirst > -50:
                    text "The only thing you drink is mountain dew when playing WoW"
                elif thirst > -75:
                    text "With your lack of desire for water, it is no surprise you have already taken a vow of celibacy."
                elif thirst > -100:
                    text "You elected to have a penectomy, your bladder being sufficient for your needs."
                text " "
                text "fort: [fort] points"
                if fort > 100:
                    text "You are the epitome of the fort, with a Fortianness of [fort]"
                    text "you are a proper protester, you call the police 'pig dogs' and you are part of an anarcho-Maoist-libertarian artist collective"
                elif fort > 75:
                    text "Michael Kirby looks up to you and your fortianness"
                elif fort > 50:
                    text "With that much Fortianness, you would be called in to give talks about social justice"
                    text "But you don't have any white priviledge to acknowledge and you are still straight (you think), cis-gendered scum"
                elif fort > 25:
                    text "With that much Fortianness, you probably can make it into the SRC if you were bothered"
                elif fort > -1:
                    text "At [fort] Fortianness, you are merely a generic student"
                elif fort > -25:
                    text "Your poor fortianness of [fort] suggests you might secretly be a James Ruse spy"
                elif fort > -50:
                    text "At [fort] fortianness, Moxham is willing to engage in the capitalist process of putting a bounty on your head to kill you"
                elif fort > -75:
                    text "With so little fortianness, you're probs a dirty, capitalist, bourgeois pig who might have underlying religious affiliations"
                elif fort > -100:
                    text "With so little fortian- how are you not just expelled at this point?"

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Friendship is magic")
                text "Serena: [rinfriendship] points"
                text "Willis: [kokfriendship] points"
                text "Fluitsma: [flufriendship] points"
                text "Rusali: [rusfriendship] points"
                text "Pragash: [prafriendship] points"
                text "Dean: [deafriendship] points"
                text "William: [wilfriendship] points"
                text "Chao: [chafriendship] points"
                text "Grant: [grafriendship] points"
                text "Moxham: [moxfriendship] points"
                text "Richard:[dikfriendship] points"
                text "Derek: [drkfriendship] points"
                text "Jittian:[jitfriendship] points"
                text "Roy: [royfriendship] points"
                text "Andrew: [leefriendship] points"
                text "Aradhya: [butfriendship] points"
                text "Steven: [dngfriendship] points"

        vbox:
            frame:
                style_group "pref"
                has vbox

                text "Slay the demon"

#########################################################################################################################
#timer bar

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 1 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=[Hide('countdown'), Jump(timer_jump)])
     # This is the timer bar.
     #timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])

    if time <= 5:
        #bar value time range timer_range xalign 0.5 yalign 0.1 xmaximum 600
        text str(time) xpos .9 ypos .5 color "#FF0000"
    else:
        #bar value time range timer_range xalign 0.5 yalign 0.1 xmaximum 600 at alpha_dissolve
        text str(time) xpos .9 ypos .5 at alpha_dissolve
    
########################################################################################################################
screen fortmap: #Preparing the imagemap
    imagemap:
        ground "map.png"
        hover "Map selected.png"
        idle "map unavailable.png"
        if "rowe" in allowedareas:
            hotspot (945, 85, 85, 75) clicked Return(1)
        if "kilgour" in allowedareas:
            hotspot (827, 175, 205, 37) clicked Return(2)
        if "rquad" in allowedareas:
            hotspot (840, 80, 100, 45) clicked Return(3)
        if "library" in allowedareas:
            hotspot (784, 123, 115, 33) clicked Return(4)
        if "gym" in allowedareas:
            hotspot (730, 104, 60, 83) clicked Return(5)
        if "food" in allowedareas:
            hotspot (650, 160, 90, 35) clicked Return(6)
        if "valley" in allowedareas:
            hotspot (350, 150, 250, 170) clicked Return(7)
        if "oval" in allowedareas:
            hotspot (320, 305, 350, 190) clicked Return(8)
        if "currycourts" in allowedareas:
            hotspot (225, 507, 203, 163) clicked Return(9)
        if "bcourts" in allowedareas:
            hotspot (500, 500, 200, 180) clicked Return(10)
        if "carpark" in allowedareas:
            hotspot (700, 480, 186, 202) clicked Return(11)
        if "fortstreet" in allowedareas:
            hotspot (890, 475, 72, 207) clicked Return(12)
        if "bridge" in allowedareas:
            hotspot (1225, 325, 126, 60) clicked Return(13)
        if "garden" in allowedareas:
            hotspot (1080, 240, 108, 119) clicked Return(14)
        if "wilkins" in allowedareas:
            hotspot (966, 273, 95, 77) clicked Return(15)
        if "quad" in allowedareas:
            hotspot (910, 320, 62, 56) clicked Return(16)
        if "cohen" in allowedareas:
            hotspot (755, 405, 133, 54) clicked Return(17)
        if "hall" in allowedareas:
            hotspot (800, 305, 102, 88) clicked Return(18)
        if "lquad" in allowedareas:
            hotspot (775, 245, 103, 55) clicked Return(19)
        if "lkilgour" in allowedareas:
            hotspot (660, 225, 117, 67) clicked Return(20)
        if "uqad" in allowedareas:
            hotspot (890, 220, 108, 56) clicked Return(21)

########################################################################################################################
# initialising inventory data structures

# player 


# objects in inventory = Items
init python:
    class Item(object):
        def __init__(self, name, amount, stat):
            self.name = name # name of item
            self.amount = amount
            self.stat = stat
            #more things about item
        # def use(self): # what happens when you use item
            

# inventory itself
init python:
    class Inventory(object):
        def __init__(self, name, max_items):
            self.inv = []  # initialise list to store items, first in is top of list
            self.name = name #name of inventory i.e. locker or bag
            self.max_items = max_items # maximum items it can hold, bag = 6, locker = infinte
            # sorts
            self.sort_by = self.sort_name #alphabetical
            self.sort_order = True #ascending, descending
            self.grid_view = True #grid or list
        
        def add(self, item, amount): #add an item +1
            self.inv.append(item)
            return ('success')
        
        def remove(self, item, amount=1): #remove an item -1
            self.inv.remove(item)
            return ('success')
        
        # sorts, figure out later
        def sort_name(self):
            self.inv.sort(key=lambda i: i[0].name, reverse=self.sort_order)
            
        def sort_qty(self):
            self.inv.sort(key=lambda i: i[1], reverse=self.sort_order)
                      
        def sort_value(self):
            self.inv.sort(key=lambda i: i[0].value, reverse=self.sort_order)

############################## inventory screens ##############################################
screen bag_button:
    textbutton "Open Bag" action [ Show("bag_screen"), Hide("bag_button")] align (0.95, 0.04)

screen bag_screen:
    modal True
    textbutton "Close Bag" action [ Hide("bag_screen"), Show("bag_button")] align (0.95, 0.04)
    frame:
        style_group "bagstyle"
        hbox:
            spacing 25
            vbox:
                align (0.1, 0.3)
                spacing 25
                
                text "Bag:"
                for item in inventory.inv:
                    text ("[item]")

screen locker_screen:
    modal True
    textbutton "Close Locker" action [ Hide("locker_screen")] align (0.5, 0.04)
    frame:
        style_group "lockstyle"
        vbox:
            align (0.1, 0.3)
            spacing 25
            
            text "Bag:"
            for item in inventory.inv:
                text ("[item]")

init -2: 
    ## STYLES ##
    # bag
    style bagstyle_frame:
        xalign 0.05
        yalign 0.3
    style bagstyle_label_text:
        size 30
    style bagstyle_label:
        xalign 0.5
    # lockers
    style lockstyle_frame:
        xalign 0.5
        yalign 0.5
    style lockstyle_label_text:
        size 30
    style lockstyle_label:
        xalign 0.5  
    style lockstyle_frame:
        xalign 0.5
        yalign 0.5
    # quests
    style queststyle_label_text:
        size 30    
    style queststyle_label:
        xalign 0.5  
