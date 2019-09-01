default popups = PopupsManager()
default achievements = load_achievements(popups)
default quests = load_quests(popups)
default diary = create_diary_view_controller()

default view_controllers.achievements = AchievementViewController(achievements)
default view_controllers.quests = QuestsViewController(quests)
default view_controllers.popups = PopupsViewController(popups)
default view_controllers.bag = create_bag_view_controller(5, 5) 
default view_controllers.friends = create_friend_view_controller()
default view_controllers.left_diary_page = create_left_diary_page()
default view_controllers.right_diary_page = create_right_diary_page()

init python:
    game = load_property_store()
    clock = Clock()

init -5 python:
    from refactor.models.popups import PopupsManager, Popup
    from refactor.models.clock import Clock
    from refactor.util import RenpyCallbacks
    from refactor.util import PropertyStore
    from refactor.util import ObservableProperty

    class ConcreteRenpyCallbacks(RenpyCallbacks):
        def __init__(self):
            RenpyCallbacks.__init__(self)

        def show_screen(self, screen, *args, **kwargs):
            renpy.show_screen(screen, *args, **kwargs)

        def hide_screen(self, screen):
            renpy.hide_screen(screen)

        def say(self, message, character=None):
            if diary.is_open:
                return
            if not character:
                character = adv
            try:
                renpy.say(character, message)
            except Exception:
                pass

        def call_label(self, label):
            diary.close()
            renpy.call(label)

        def play_sfx(self, filepath):
            playsfx(filepath)

        def play_music(self, filepath):
            playmusic(filepath)

    RenpyCallbacks.set_instance(ConcreteRenpyCallbacks())


    def load_property_store():
        store = PropertyStore()

        store.add("chaoPissed", ObservableProperty(False))
        store.add("delivery", ObservableProperty(False))
        store.add("electionPromise", ObservableProperty(False))
        store.add("hasDiary", ObservableProperty(False))
        store.add("metDerek", ObservableProperty(False))
        store.add("norton", ObservableProperty(False))
        store.add("stealWillisGirl", ObservableProperty(False))
        store.add("yangRant", ObservableProperty(False))

        store.add("moxCounter", ObservableProperty(0))
        store.add("timeTravelCounter", ObservableProperty(0))
        store.add("currentDay", ObservableProperty(0))
        store.add("suicideCount", ObservableProperty(0))
        store.add("currentDiaryPage", ObservableProperty(0))

        return store