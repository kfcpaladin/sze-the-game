default popups = PopupsManager()
default achievements = load_achievements(popups)
default quests = load_quests(popups)

default view_controllers.achievements = AchievementViewController(achievements)
default view_controllers.quests = QuestsViewController(quests)
default view_controllers.popups = PopupsViewController(popups)
default view_controllers.bag = create_bag_view_controller(5, 5) 
default view_controllers.left_diary_page = create_left_diary_page()
default view_controllers.right_diary_page = create_right_diary_page()

init -1 python:
    from refactor.models.popups import PopupsManager, Popup
    from refactor.views.achievements import AchievementViewController
    from refactor.views.quests import QuestsViewController
    from refactor.views.popups import PopupsViewController
    from refactor.views.inventory import BagViewController
    from refactor.util import Vector2D, Rect2D
    from refactor.util import RenpyCallbacks

    class ConcreteRenpyCallbacks(RenpyCallbacks):
        def __init__(self):
            RenpyCallbacks.__init__(self)

        def show_screen(self, screen, *args, **kwargs):
            renpy.show_screen(screen, *args, **kwargs)

        def say(self, message, character=None):
            if not character:
                character = adv
            try:
                renpy.say(character, message)
            except Exception:
                pass

        def call_label(self, label):
            renpy.call(label)

        def play_sfx(self, filepath):
            playsfx(filepath)

        def play_music(self, filepath):
            playmusic(filepath)

    RenpyCallbacks.set_instance(ConcreteRenpyCallbacks())

    def create_bag_view_controller(total_columns, total_rows):
        controller = BagViewController(total_rows, total_columns)

        controller.equipped_colour = colour.green
        controller.unequipped_colour = colour.yellow
        controller.background_colour = colour.maroon
        controller.item_transparency = 120
        controller.tooltip_transparency = 180

        return controller

    def create_left_diary_page():
        return Rect2D(right=625, bottom=570).add_offset(Vector2D(40, 95))

    def create_right_diary_page():
        return Rect2D(right=625, bottom=570).add_offset(Vector2D(720, 95))