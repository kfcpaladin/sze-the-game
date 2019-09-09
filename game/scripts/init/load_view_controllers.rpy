init -1 python:
    from views.achievements import AchievementViewController
    from views.quests import QuestsViewController
    from views.popups import PopupsViewController
    from views.inventory import BagViewController
    from views.friends import FriendViewController
    from views.diary import DiaryViewController, DiaryPage
    from util.gametools import Vector2D, Rect2D

    def create_bag_view_controller(total_columns, total_rows):
        controller = BagViewController(total_rows, total_columns)
        return controller

    def create_friend_view_controller():
        controller = FriendViewController()
        return controller

    def create_diary_view_controller():
        diary = DiaryViewController()
        diary.append_page(DiaryPage("diary_bag", cleanup_screens=["bag_tooltip"]))
        diary.append_page(DiaryPage("diary_quests"))
        diary.append_page(DiaryPage("diary_achievements"))
        diary.append_page(DiaryPage("diary_statistics"))
        return diary

    def create_left_diary_page():
        return Rect2D(right=625, bottom=570).add_offset(Vector2D(40, 95))

    def create_right_diary_page():
        return Rect2D(right=625, bottom=570).add_offset(Vector2D(720, 95))

    def create_screen_rect():
        rect = Rect2D(bottom=768, right=1366)
        return rect

    