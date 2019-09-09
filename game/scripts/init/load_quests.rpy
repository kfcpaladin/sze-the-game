init -1 python:
    from models.quests import QuestManager, Quest, QuestJump
    from util.conditions import *



    def load_quests(*dependencies):
        manager = QuestManager(*dependencies)

        manager.add_quest(Quest(
            id="serenaSlay",
            title="Slay Serena and go to heaven",
            brief="Arthur is planning on slaying Serena",
            description="Once in heaven, Arthur will be able to slay several virgins, thereby satisfying his life goal of being a donkey",
            icon=loadImage("quest_serenaSlay.png")))

        manager.add_quest(Quest(
            id="sexuality",
            title="Arthur's gay journey",
            brief="Arthur is going on an adventure",
            description="In order to acquire all 9 pokeballs, he must conquer Kevin Spacey",
            icon=None))

        # gary quests
        manager.add_quest(Quest(
            id="garythirst1",
            title="Gary's reeducation program",
            brief="Gary will help Arthur slay Serena",
            description="Not only are his expertise in slaying unparalleled, he also offers free condoms",
            icon=None))

        manager.get_quest("garythirst1").set_start_callback(QuestJump("garyreeducation1"))

        manager.add_quest(Quest(
            id="garythirst2",
            title="Gary's reeducation program",
            brief="Gary will help Arthur slay Serena",
            description="Not only are his expertise in slaying unparalleled, he also offers free condoms",
            icon=None))

        manager.get_quest("garythirst2").set_start_callback(QuestJump("garyreeducation2"))

        manager.add_quest(Quest(
            id="garythirst3",
            title="Gary's reeducation program",
            brief="Gary will help Arthur slay Serena",
            description="Not only are his expertise in slaying unparalleled, he also offers free condoms",
            icon=None))

        manager.get_quest("garythirst3").set_start_callback(QuestJump("garyreeducation3"))

        manager.add_quest(Quest(
            id="garythirst4",
            title="Gary's reeducation program",
            brief="Gary will help Arthur slay Serena",
            description="Not only are his expertise in slaying unparalleled, he also offers free condoms",
            icon=None))

        manager.get_quest("garythirst4").set_start_callback(QuestJump("garyreeducation4"))

        manager.add_quest(Quest(
            id="garythirst5",
            title="Gary's reeducation program",
            brief="Gary will help Arthur slay Serena",
            description="Not only are his expertise in slaying unparalleled, he also offers free condoms",
            icon=None))

        manager.get_quest("garythirst5").set_start_callback(QuestJump("garyreeducation5"))

        manager.add_quest(Quest(
            id="garythirst6",
            title="Gary's reeducation program",
            brief="Gary will help Arthur slay Serena",
            description="Not only are his expertise in slaying unparalleled, he also offers free condoms",
            icon=None))

        manager.get_quest("garythirst6").set_start_callback(QuestJump("garyreeducation6"))

        manager.add_quest(Quest(
            id="garythirst7",
            title="Gary's reeducation program",
            brief="Gary will help Arthur slay Serena",
            description="Not only are his expertise in slaying unparalleled, he also offers free condoms",
            icon=None))

        manager.get_quest("garythirst7").set_start_callback(QuestJump("garyreeducation7"))

        manager.add_quest(Quest(
            id="garythirst8",
            title="The final problem",
            brief="Become a slaying god",
            description="If you complete this, you will become the most sexy man alive",
            icon=None))

        manager.get_quest("garythirst8").set_start_callback(QuestJump("garyreeducation8"))

        # todd karate quests
        manager.add_quest(Quest(
            id="jigschool1",
            title="Be a rebel",
            brief="You don't feel like going to school",
            description="You have decided to abandon your education in the morning",
            icon=loadImage("quest_jigschool1.png")))

        manager.get_quest("jigschool1").set_start_callback(QuestJump("jigschool1"))


        return manager
