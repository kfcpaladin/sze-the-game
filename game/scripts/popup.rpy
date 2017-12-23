# Used to manage popups
python early:
    def popup(messages, **options):
        if type(messages) in [str, unicode, basestring]:
            messages = [messages]
        elif type(messages) is not list:
            raise TypeError("Popup message should be list or string, not {0}".format(type(messages)))
        renpy.show_screen("popup", messages, **options)
        renpy.say(adv, "")
