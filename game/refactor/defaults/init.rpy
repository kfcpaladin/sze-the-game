init -1 python:
    from refactor.defaults.loading import *
    from refactor.models.characters.notifications.AttributeNotificationSystem import AttributeNotification

    AttributeNotification.message_callback = [lambda msg: renpy.say(adv, msg)]
    
    initial_data_dir = "./game/refactor/defaults/"
    achievements = load_achievements(initial_data_dir+"achievements.json")
    characters = load_characters(initial_data_dir+"characters.json")
    sze = characters[0]
    

    # Buffered data relies on other data being loaded before hand
    # TODO: What happens if buffered data relies on other buffered data?
    # Perhaps keep cycling through the buffer until it is consumed, and if not raise error
    JSONImporter.parse_buffered_data()                


