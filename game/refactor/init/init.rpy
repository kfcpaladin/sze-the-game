default popups = PopupsManager()
default achievements = load_achievements(popups)

default view_controllers.achievements = AchievementViewController(achievements)
default view_controllers.popups = PopupsViewController(popups)
default view_controllers.left_diary_page = create_left_diary_page()
default view_controllers.right_diary_page = create_right_diary_page()

init -1 python:
    from refactor.models.popups import PopupsManager, Popup
    from refactor.views.achievements import AchievementViewController
    from refactor.views.popups import PopupsViewController
    from refactor.util import Vector2D, Rect2D

    class ShowScreen:
        def show_screen(self, screen, *args, **kwargs):
            renpy.show_screen(screen, *args, **kwargs)

    PopupsViewController.callback = ShowScreen()

    def create_left_diary_page():
        return Rect2D(right=625, bottom=570).add_offset(Vector2D(40, 95))

    def create_right_diary_page():
        return Rect2D(right=625, bottom=570).add_offset(Vector2D(720, 95))