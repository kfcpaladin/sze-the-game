init python:
    import json
    from refactor.persistence import JSONImporter
    from refactor.models.achievements import AchievementsManager

    achievements = AchievementsManager()

    def load_data():
        def load_achievements():
            with open("./game/refactor/defaults/achievements.json", "r") as file: 
                achievements_data = json.load(file)
                for data in achievements_data:
                    achievement = JSONImporter.visit("achievement", data)
                    achievements.add_achievement(achievement)
                


        load_achievements()
    
    load_data()

    # Buffered data relies on other data being loaded before hand
    # TODO: What happens if buffered data relies on other buffered data?
    # Perhaps keep cycling through the buffer until it is consumed, and if not raise error
    JSONImporter.parse_buffered_data()                

