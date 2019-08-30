init -1 python:
    import json
    from refactor.persistence import JSONImporter
    from refactor.models.achievements import AchievementsManager


    def load_achievements():
        achievements = []
        with open("./game/refactor/defaults/achievements.json", "r") as file: 
            achievements_data = json.load(file)
            for data in achievements_data:
                achievement = JSONImporter.visit("achievement", data)
                achievements.append(achievement)
        return achievements
            
    def load_characters():
        characters = []
        with open("./game/refactor/defaults/characters.json", "r") as file:
            characters_data = json.load(file)
            for data in characters_data:
                character = JSONImporter.visit("character", data)
                characters.append(character)
        return characters

    achievements = AchievementsManager()
    for achievement in load_achievements():
        achievements.add_achievement(achievement)

    characters = load_characters()
    sze = characters[0]
    

    


    # Buffered data relies on other data being loaded before hand
    # TODO: What happens if buffered data relies on other buffered data?
    # Perhaps keep cycling through the buffer until it is consumed, and if not raise error
    JSONImporter.parse_buffered_data()                


