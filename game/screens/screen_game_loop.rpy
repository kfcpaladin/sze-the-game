# Game loop for updating things 
screen screen_game_loop(speed=0.5):
    timer speed:
        repeat True
        action [
            Function(gameLoop),
        ]

init python:
    def gameLoop():
        achievements.updateAchievements()
        quests.updateQuests()
