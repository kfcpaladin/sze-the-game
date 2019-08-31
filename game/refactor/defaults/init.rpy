init -1 python:
    from refactor.defaults.loaders import *
    from refactor.models.characters.notifications.AttributeNotificationSystem import AttributeNotification

    AttributeNotification.message_callback = [lambda msg: renpy.say(adv, msg)]
    
    initial_data_dir = "./game/refactor/defaults/"
    achievements = load_achievements(initial_data_dir+"achievements.json")
    characters = load_characters(initial_data_dir+"characters.json")
    sze = characters[0]

    notification_handlers = [
        ("tutorial_message", "tutorial_messages.json"),
        ("attribute_change_message", "attribute_change_messages.json"),
        ("priority_attribute_message", "attribute_value_messages.json")
    ]

    for notification in load_notifications(initial_data_dir+"notifications/sze", notification_handlers):
        sze.add_notification(notification)
    

    # Buffered data relies on other data being loaded before hand
    # TODO: What happens if buffered data relies on other buffered data?
    # Perhaps keep cycling through the buffer until it is consumed, and if not raise error
    JSONImporter.parse_buffered_data()                


