import json
import os

from refactor.persistence import JSONImporter
from refactor.models.achievements import AchievementsManager

from .NotificationLoader import notification_loader

def load_achievements(filepath):
    achievements = AchievementsManager()
    with open(filepath, "r") as file: 
        achievements_data = json.load(file)
        for data in achievements_data:
            achievement = JSONImporter.visit("achievement", data)
            achievements.add_achievement(achievement)
    return achievements
        
def load_characters(filepath):
    characters = []
    with open(filepath, "r") as file:
        characters_data = json.load(file)
        for data in characters_data:
            character = JSONImporter.visit("character", data)
            characters.append(character)

    return characters

def load_notifications(folder, handlers):
    all_notifications = []
    for handler_id, file in handlers:
        filepath = os.path.join(folder, file)
        notifications = notification_loader.load(handler_id, filepath)
        all_notifications.extend(notifications)
    return all_notifications

def load_stat_messages(filepath):
    pass