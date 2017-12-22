############################## inventory screens ##############################################

# currently inefficent, can probably optimise
screen bag_button:
    textbutton "Open Bag" action [ Show("bag_screen"), Hide("bag_button")] align (0.95, 0.04)

screen bag_screen:
    modal True
    textbutton "Close Bag" action [ Hide("bag_screen"), Show("bag_button")] align (0.95, 0.04)
    frame:
        style_group "bagstyle"
        vbox:
            spacing 25
            vbox:
                use inventory_view
                #text "Bag:"
                #for item in inventory.inv:
                    #text ("[item]")
screen inventory_view(inventory=inventory):
    tag menu
    use navigation # Include the navigation.
    frame:
        style_group "bagstyle"
        area (0, 0, 500, 50)
        label _("Bag")
    frame:
        style_group "bagstyle"
        hbox:
            spacing 25
            vbox:
                side "c r":
                    style_group "bagstyle"
                    area (0, 0, 250, 500)
                    vpgrid id ("vp"+inventory.name):
                        draggable True
                        mousewheel True
                        xsize 250 ysize 475
                        cols 1 spacing 25
                        for item in inventory.inv:
                            $ name = item.name
                            $ desc = item.desc
                            # Create an item element in the list
                            frame:
                                if item.used:
                                    background Solid("#009933")
                                else:
                                    background Solid("#e6ac00") 
                                hbox:
                                    if item.icon:
                                        $ icon = item.icon
                                        $ hover_icon = im.Sepia(icon)
                                        imagebutton:
                                            idle icon
                                            hover hover_icon
                                            action [
                                                Show("bag_button"), 
                                                Hide("bag_screen"),
                                                Play ("sound", "sfx/vpunch.ogg"),
                                                Function(item.toggle, inventory.who),
                                            ]
                                            hovered [ 
                                                Play("sound", "sfx/8d82b5_Final_Fantasy_XI_Menu_Selection_Sound_Effect.ogg"),
                                                Show("gui_tooltip",item=item) 
                                            ]
                                            unhovered Hide("gui_tooltip")
                                    text name

                        #if len(inventory.inv) == 0:
                            #add Null(height=100,width=100)
                    vbar value YScrollValue("vp"+inventory.name)
    # Yo dean this is just for stats, debugging mostly
    vbox:
        spacing 0
        area (750, 100, 1300, 650)
        xsize 550
        frame:
            has vbox
            $ person = inventory.who
            text "{b}" + "Stats of {0}".format(unicode.title(person.name)) + "{/b}"
            for attribute in person.attributes:
                text "{b}" + "{0}: ".format(attribute) + "{/b}" + "{0}".format(getattr(person, attribute))
            
        #hbox:
            #area (0, 0, 200, 200)

screen gui_tooltip(item=False):
    if item:
        vbox:
            xoffset 350
            yalign 0.3
            spacing 0
            frame:
                has vbox
                text "{b}Description: {/b}" + item.desc
                text "{b}Statistics{/b}"
                for stat, value in item.stat.iteritems():
                    if value > 0:
                        text "+{0} {1}".format(value, stat)
                    else:
                        text "{0} {1}".format(value, stat)
                text "{b}Equipped: {/b}" + "{0}".format(item.used)


screen locker_screen:
    modal True
    textbutton "Close Locker" action [ Hide("locker_screen")] align (0.5, 0.04)
    frame:
        style_group "lockstyle"

        vbox:
            align (0.1, 0.3)
            spacing 25

            text "Lockers: and this shouldn't be the same as the bag, need to change..."
            for item in inventory.inv:
                $ name = item.name
                text name

init -2:
    ## STYLES ##
    # bag
    style bagstyle_frame:
        xalign 0.05
        yalign 0.35
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
    style queststyle_frame:
        xalign 0.5
        yalign 0.5
    style queststyle_label_text:
        size 30
    style queststyle_label:
        xalign 0.5
