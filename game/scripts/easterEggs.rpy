init python:
    def easterEggValley(friend):
        if not isinstance(friend, Friend):
            raise TypeError("Expected a Friend for easterEggValley, instead got {0}".format(type(friend)))
        while True:
            try:
                total = renpy.input("How friendly do you want to be with {0}?".format(friend.name))
                total = int(total)
            except:
                continue
            else:
                if type(total) not in (int, float):
                    continue
                break
        if(total >= 0):
            friend.gain(total)
        else:
            friend.loss(-total)
