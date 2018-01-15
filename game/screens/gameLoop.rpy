# Game loop for updating things 
screen gameLoop(speed=2):
    timer speed:
        repeat True
        action [
            Function(gameLoop),
        ]

init python:
    def gameLoop():
        achievements.updateAchievements()
