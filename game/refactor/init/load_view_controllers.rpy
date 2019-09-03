init -1 python:
    from refactor.views.achievements import AchievementViewController
    from refactor.views.quests import QuestsViewController
    from refactor.views.popups import PopupsViewController
    from refactor.views.inventory import BagViewController
    from refactor.views.friends import FriendViewController
    from refactor.views.diary import DiaryViewController, DiaryPage
    from refactor.util.gametools import Vector2D, Rect2D

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
    
    def create_gunshot_suicide_view_controller():
        from refactor.models.suicides.gunshot import GunshotSuicide, Gun, Head
        gun = Gun(
            width=200,
            height=150,
            bullet_velocity=50,
            round_size=20)
        
        head = Head(width=200, height=300)
        head.position = Vector2D(200, 200)

        bounding_box = Rect2D(right=config.screen_width, bottom=config.screen_height)

        gunshot_suicide = GunshotSuicide(bounding_box, head, gun)

        controller = GunshotSuicideViewController(gunshot_suicide)

        return controller