default view_controllers.attributes = load_attribute_view_controller()

init python:
    def load_attribute_view_controller():
        from views.attributes import AttributesViewController, AttributesViewMessage
        from util import PriorityList, PriorityEntry

        controller = AttributesViewController()

        # charm
        priority_list = PriorityList()

        priority_list.add_entry(PriorityEntry(key=100, value="You slay just by looking. Gaze upon the world, your dominion"))
        priority_list.add_entry(PriorityEntry(key=75, value="With that level of charm, you have probably slayed every LG in Sydney by now"))
        priority_list.add_entry(PriorityEntry(key=50, value="You have surpassed even Chao in slaying ability; the teacher becomes the student"))
        priority_list.add_entry(PriorityEntry(key=25, value="You are just very slightly charming"))
        priority_list.add_entry(PriorityEntry(key=0, value="With such exceptionally average charm, its going to take a very long time for senpai to notice you."))
        priority_list.add_entry(PriorityEntry(key=-25, value="With your charm, or lack thereof, there seems to be an invisible forcefield repelling girls from you"))
        priority_list.add_entry(PriorityEntry(key=-50, value="With that much charm, you are often mistaken for a modern art piece"))
        priority_list.add_entry(PriorityEntry(key=-75, value="The average gayness of every room you enter is increased by 100%, due to your charm"))
        priority_list.add_entry(PriorityEntry(key=-100, value="You once tried to masturbate, your hand rejected you"))

        attribute_message = AttributesViewMessage(
            attribute=sze.get_attribute("charm"), 
            brief="Charm is a measure of how well you slay",
            priority_list=priority_list)

        controller.add_attribute_message(attribute_message)

        # fort
        priority_list = PriorityList()

        priority_list.add_entry(PriorityEntry(key=100, value="You are a proper protester, you call the police 'pig dogs' and you are part of an anarcho-Maoist-libertarian artist collective"))
        priority_list.add_entry(PriorityEntry(key=75, value="Michael Kirby looks up to you and your fortianness"))
        priority_list.add_entry(PriorityEntry(key=50, value="With that much Fortianness, you would be called in to give talks about social justice, but you don't have any white priviledge to acknowledge and you are still straight (you think), cis-gendered scum"))
        priority_list.add_entry(PriorityEntry(key=25, value="With that much Fortianness, you probably can make it into the SRC if you were bothered"))
        priority_list.add_entry(PriorityEntry(key=0, value="At [sze.fort] Fortianness, you are merely a generic student"))
        priority_list.add_entry(PriorityEntry(key=-25, value="Your poor fortianness of [sze.fort] suggests you might secretly be a James Ruse spy"))
        priority_list.add_entry(PriorityEntry(key=-50, value="At [sze.fort] fortianness, Moxham is willing to engage in the capitalist process of putting a bounty on your head to kill you"))
        priority_list.add_entry(PriorityEntry(key=-75, value="With so little fortianness, you're probs a dirty, capitalist, bourgeois pig who might have underlying religious affiliations"))
        priority_list.add_entry(PriorityEntry(key=-100, value="With so little fortian- how are you not just expelled at this point?"))
        
        attribute_message = AttributesViewMessage(
            attribute=sze.get_attribute("fort"), 
            brief="Fortianness is how Fortian you are and can be improved by being more Michael Kirby",
            priority_list=priority_list)

        controller.add_attribute_message(attribute_message)

        # intellect
        priority_list = PriorityList()

        priority_list.add_entry(PriorityEntry(key=100, value="You have surpassed even Justin Wu, dux of James Ruse"))
        priority_list.add_entry(PriorityEntry(key=75, value="Maybe you'll be able to impress Serena with your 99.95 ATAR"))
        priority_list.add_entry(PriorityEntry(key=50, value="A bit more hard work and you will truly ACE TRIALS"))
        priority_list.add_entry(PriorityEntry(key=25, value="At marginally above average intellect you really shouldnt be celebrating yet"))
        priority_list.add_entry(PriorityEntry(key=0, value="With your remarkably average intellect, your waifu will probably not be impressed"))
        priority_list.add_entry(PriorityEntry(key=-25, value="You are a bit slow, should you even be in a selective school?"))
        priority_list.add_entry(PriorityEntry(key=-50, value="Your test results are probably worse than Chao's tests for STDs"))
        priority_list.add_entry(PriorityEntry(key=-75, value="It's astonishing how you made it to Fort Street. How many dicks did you have to suck to get here?"))
        priority_list.add_entry(PriorityEntry(key=-100, value="With almost no brain activity, the fact that your nervous system still works is a scientific anomaly."))

        attribute_message = AttributesViewMessage(
            attribute=sze.get_attribute("intellect"), 
            brief="Intelligence is a measure of how smart you are",
            priority_list=priority_list)

        controller.add_attribute_message(attribute_message)

        # strength
        priority_list = PriorityList()

        priority_list.add_entry(PriorityEntry(key=100, value="You are Level S-Class 11th-dan Golden Jade Dragon Jedi Master Ninja Samurai Viking Knight Marshal Admiral"))
        priority_list.add_entry(PriorityEntry(key=75, value="With your combat propensity, you probably ended 300 spartans with a single one-inch punch."))
        priority_list.add_entry(PriorityEntry(key=50, value="Your skill in a fight would allow you to beat black-belt Aradhya and Jew-jitsu Steven."))
        priority_list.add_entry(PriorityEntry(key=25, value="With such strength, you can probs beat the average student."))
        priority_list.add_entry(PriorityEntry(key=0, value="At your level it is advised that you tactically retreat from your fights."))
        priority_list.add_entry(PriorityEntry(key=-25, value="Your below average combat propensity suggests that you have a thing for being dominated."))
        priority_list.add_entry(PriorityEntry(key=-50, value="At [sze.strength] combat propensity, the only slaying you know is in Dungeons & Dragons..."))
        priority_list.add_entry(PriorityEntry(key=-75, value="With that combat 'proficiency' pussies slays you."))
        priority_list.add_entry(PriorityEntry(key=-100, value="Don't fight; you will get rekt so hard, you will be reincarnated as an abortion."))

        attribute_message = AttributesViewMessage(
            attribute=sze.get_attribute("strength"), 
            brief="Strength is a measure of how strong you are",
            priority_list=priority_list)

        controller.add_attribute_message(attribute_message)

        # thirst
        priority_list = PriorityList()

        priority_list.add_entry(PriorityEntry(key=100, value="At a thirst of [sze.thirst], you rival Tiddalik"))
        priority_list.add_entry(PriorityEntry(key=75, value="You're so thirsty, sometimes moxham appears in your {s}dreams{/s} hallucinations"))
        priority_list.add_entry(PriorityEntry(key=50, value="With that much thirst, like Roy, you are willing to partake in sexual activities with robots for water"))
        priority_list.add_entry(PriorityEntry(key=25, value="Even a can of SOLO cannot crush your thirst of [sze.thirst]"))
        priority_list.add_entry(PriorityEntry(key=0, value="With this much thirstiness, you have the standard healthy desires of a teenage boy of your age."))
        priority_list.add_entry(PriorityEntry(key=-25, value="You have been oft compared to LiXu due to your lack of thirst"))
        priority_list.add_entry(PriorityEntry(key=-50, value="The only thing you drink is mountain dew when playing WoW"))
        priority_list.add_entry(PriorityEntry(key=-75, value="With your lack of desire for water, it is no surprise you have already taken a vow of celibacy."))
        priority_list.add_entry(PriorityEntry(key=-100, value="You elected to have a penectomy, your bladder being sufficient for your needs."))

        attribute_message = AttributesViewMessage(
            attribute=sze.get_attribute("thirst"), 
            brief="Thirst is a measure of desperately you want to drink water",
            priority_list=priority_list)

        controller.add_attribute_message(attribute_message)

        return controller