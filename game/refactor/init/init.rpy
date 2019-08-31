default achievements = load_achievements()
default view_controllers.achievements = AchievementViewController(achievements)

init -1 python:
    from refactor.views.achievements import AchievementViewController
    from refactor.models.characters import MainCharacter

