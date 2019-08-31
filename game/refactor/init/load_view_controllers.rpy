default view_controllers.achievements = AchievementViewController(achievements)
default view_controllers.left_diary_page = create_left_diary_page()
default view_controllers.right_diary_page = create_right_diary_page()

init -1 python:
    from refactor.views.achievements import AchievementViewController
    from refactor.util import Vector2D, Rect2D

    def create_left_diary_page():
        return Rect2D(right=625, bottom=570).add_offset(Vector2D(40, 95))

    def create_right_diary_page():
        return Rect2D(right=625, bottom=570).add_offset(Vector2D(720, 95))


