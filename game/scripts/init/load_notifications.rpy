init 1 python:
    # load in this order for message to appear in this order
    load_tutorial_messages()
    load_attribute_change_messages()
    load_attribute_value_messages()

init python:
    from models.notifications import *
    from util import PriorityList, PriorityEntry

    class Narrator:
        def say(self, message):
            try:
                renpy.say(adv, message)
            except Exception:
                pass

    AttributeNotification.narrator = Narrator() 

    def load_tutorial_messages():
        sze.get_attribute("charm").observe(TutorialMessage(
            brief="Charm is a measure of how well you slay",
            msg_gain="Currently you are a faggot, however this may be changed through slaying not being retarded in day to day life.",
            msg_loss="Currently you are a faggot, however this may be changed through slaying not being retarded in day to day life.",
            show="True"))
            
        sze.get_attribute("fort").observe(TutorialMessage(
            brief="Fortianness is how Fortian you are and can be improved by being more Michael Kirby",
            msg_gain="Currently, you aren't very Fortian.",
            msg_loss="Currently, you aren't very Fortian.",
            show="True"))
            
        sze.get_attribute("intellect").observe(TutorialMessage(
            brief="Intelligence is a measure of how smart you are",
            msg_gain="Currently you are a retard, however this may be changed through diligent studying and participating in class.",
            msg_loss="Currently you are a retard, however this may be changed through diligent studying and participating in class.",
            show="True"))
            
        sze.get_attribute("strength").observe(TutorialMessage(
            brief="Strength is a measure of how strong you are",
            msg_gain="It can be improved by getting good. Currently you aren't very good.",
            msg_loss="It can be improved by getting good. Currently, you make 6 year olds look like professional MMA fighters.",
            show="True"))
            
        sze.get_attribute("thirst").observe(TutorialMessage(
            brief="Thirst is a measure of desperately you want to drink water",
            msg_gain="You become one step closer to Tiddalik.",
            msg_loss="At this rate your body will dehydrate into a shrivelled penis.",
            show="True"))

    def load_attribute_change_messages():
        sze.get_attribute("charm").observe(AttributeChangeMessage(
            msg_gain="Your charm increased",
            msg_loss="Your charm just decreased"))
            
        sze.get_attribute("fort").observe(AttributeChangeMessage(
            msg_gain="You became more Michael Kirby  , as your Fortianness is at [sze.fort]",
            msg_loss="You fortianness dropped."))
            
        sze.get_attribute("intellect").observe(AttributeChangeMessage(
            msg_gain="Congratulations",
            msg_loss="You become a bit dumber"))
            
        sze.get_attribute("strength").observe(AttributeChangeMessage(
            msg_gain="Your combat propensity has increased",
            msg_loss="Your combat propensity has decreased"))
            
        sze.get_attribute("thirst").observe(AttributeChangeMessage(
            msg_gain="You became more thirsty",
            msg_loss="You start zipping your pants back up"))

    def load_attribute_value_messages():
        # charm
        priority_list = PriorityList()
        priority_list.add_entry(PriorityEntry(key=100, value="With a charm of [sze.charm], you slay just by looking. Gaze upon the world, your dominion."))
        priority_list.add_entry(PriorityEntry(key=75, value="With a charm of [sze.charm], you have probably slayed every LG in Sydney by now"))
        priority_list.add_entry(PriorityEntry(key=50, value="You have surpassed even Chao in slaying ability with a charm of [sze.charm]"))
        priority_list.add_entry(PriorityEntry(key=25, value="You are just very slightly charming, at [sze.charm]"))
        priority_list.add_entry(PriorityEntry(key=0, value="With exceptionally average charm of [sze.charm], its going to take a very long time for Serena to notice you."))
        priority_list.add_entry(PriorityEntry(key=-25, value="With charm of [sze.charm], there seems to be an invisible forcefield repelling LGs from you"))
        priority_list.add_entry(PriorityEntry(key=-50, value="With charm at [sze.charm], you are often mistaken as a modern art piece."))
        priority_list.add_entry(PriorityEntry(key=-75, value="The average gayness of every room you enter is increased by 100%, due to your charm of [sze.charm]"))
        priority_list.add_entry(PriorityEntry(key=-100, value="You once tried to masturbate, your hand rejected you."))
        priority_list.add_entry(PriorityEntry(key=-125, value="Even bacteria tries to avoid you."))
        sze.get_attribute("charm").observe(AttributeValueMessage(priority_list))

        # fort
        priority_list = PriorityList()
        priority_list.add_entry(PriorityEntry(key=100, value="You are the epitome of the fort, with a fortianness of [sze.fort]\nYou are a proper protester, you call the police \"pig dogs\" and you are part of an artist collective"))
        priority_list.add_entry(PriorityEntry(key=75, value="Michael Kirby looks up to you and your fortianness of [sze.fort]"))
        priority_list.add_entry(PriorityEntry(key=50, value="With a fortianness of [sze.fort], you are often called in to speak at Speech Day"))
        priority_list.add_entry(PriorityEntry(key=25, value="With a fortianness of [sze.fort], you probably made it into the SRC"))
        priority_list.add_entry(PriorityEntry(key=0, value="At [sze.fort] fortianness, you are merely a generic student"))
        priority_list.add_entry(PriorityEntry(key=-25, value="Your poor fortianness of [sze.fort] suggests you might secretly be a James Ruse spy"))
        priority_list.add_entry(PriorityEntry(key=-50, value="At [sze.fort] fortianness, Moxham is willing to engage in the capitalist process of putting a bounty on your head to kill you"))
        priority_list.add_entry(PriorityEntry(key=-75, value="With [sze.fort] fortianness, you are probably a dirty, capitalist, bourgeois pig who might have underlying religious affiliations"))
        priority_list.add_entry(PriorityEntry(key=-100, value="Your racist, sexist and classist behaviour is an affront to the school"))
        sze.get_attribute("fort").observe(AttributeValueMessage(priority_list))

        # intellect
        priority_list = PriorityList()
        priority_list.add_entry(PriorityEntry(key=100, value="With intelligence of [sze.intellect], maybe its for the better. Your thoughts were too complex for even Stephen Hawking."))
        priority_list.add_entry(PriorityEntry(key=75, value="But your predicted ATAR is still a safe 99.95, and your intelligence of [sze.intellect]"))
        priority_list.add_entry(PriorityEntry(key=50, value="You are quite smart already, maybe not band-6 yet, but getting there. A bit more hard work and you will truly ACE TRIALS. Your current intelligence is [sze.intellect]"))
        priority_list.add_entry(PriorityEntry(key=25, value="Your intelligence is at [sze.intellect], not particularly amazing."))
        priority_list.add_entry(PriorityEntry(key=0, value="With your remarkably average intelligence of [sze.intellect], Serena will probably not be impressed."))
        priority_list.add_entry(PriorityEntry(key=-25, value="You are a bit slow, with intelligence of [sze.intellect]"))
        priority_list.add_entry(PriorityEntry(key=-50, value="You are probably doing worse than Chao in your tests currently, with intelligence of [sze.intellect]"))
        priority_list.add_entry(PriorityEntry(key=-75, value="It's astonishing how someone with an intelligence of [sze.intellect] even made it to Fort Street. How many dicks did you have to suck to get here?"))
        priority_list.add_entry(PriorityEntry(key=-100, value="With intelligence of [sze.intellect], you are not even a functioning member of society."))
        priority_list.add_entry(PriorityEntry(key=-125, value="You are somehow dumber than a rock, like literally. I dont know how that is even possible."))
        sze.get_attribute("intellect").observe(AttributeValueMessage(priority_list))

        # strength
        priority_list = PriorityList()
        priority_list.add_entry(PriorityEntry(key=100, value="Your combat propensity is at [sze.strength], making you Level S-Class 11th-dan Golden Jade Dragon Jedi Master Ninja Samurai Knight Marshal Admiral, surpassing Saitama in skill."))
        priority_list.add_entry(PriorityEntry(key=75, value="With combat propensity at [sze.strength], you probably ended 300 spartans with a single one-inch punch."))
        priority_list.add_entry(PriorityEntry(key=50, value="Your combat propensity of [sze.strength] would allow you to beat black-belt Aradhya and Jew-jitsu Steven with ease."))
        priority_list.add_entry(PriorityEntry(key=25, value="At combat propensity levels of [sze.strength], you can probs beat the average student."))
        priority_list.add_entry(PriorityEntry(key=0, value="At [sze.strength], your combat propensity, it is advised that you tactically retreat from your \"fights\"."))
        priority_list.add_entry(PriorityEntry(key=-25, value="Your below average combat propensity of [sze.strength] suggests that you have a thing for being dominated."))
        priority_list.add_entry(PriorityEntry(key=-50, value="At [sze.strength] combat propensity, the only slaying you know is in Dungeons & Dragons..."))
        priority_list.add_entry(PriorityEntry(key=-75, value="With [sze.strength] combat propensity pussies slays you."))
        priority_list.add_entry(PriorityEntry(key=-100, value="When you have [sze.strength] combat \"propensity\", you will get rekt so hard, you will be reincarnated as an abortion."))
        priority_list.add_entry(PriorityEntry(key=-125, value="Your combat \"propensity\" or lack thereof will lead to much assrippings in the future"))
        sze.get_attribute("strength").observe(AttributeValueMessage(priority_list))

        # thirst
        priority_list = PriorityList()
        priority_list.add_entry(PriorityEntry(key=100, value="At a thirst of [sze.thirst], you rival Tiddalik"))
        priority_list.add_entry(PriorityEntry(key=75, value="With a thirst of [sze.thirst], sometimes moxham appears in your {s}dreams{/s} hallucinations"))
        priority_list.add_entry(PriorityEntry(key=50, value="With a thirst of [sze.thirst], like Roy, you are willing to partake in sexual activities with robots for water"))
        priority_list.add_entry(PriorityEntry(key=25, value="Even a can of SOLO cannot crush your thirst of [sze.thirst]"))
        priority_list.add_entry(PriorityEntry(key=0, value="At [sze.thirst] thirstiness , you have the standard healthy desires of a teenage boy of your age."))
        priority_list.add_entry(PriorityEntry(key=-25, value="With a thirstiness of [sze.thirst], you have been oft compared to LiXu"))
        priority_list.add_entry(PriorityEntry(key=-50, value="At a thirst of [sze.thirst], it is no surprise you have already taken a vow of celibacy."))
        priority_list.add_entry(PriorityEntry(key=-75, value="With [sze.thirst] thirstiness, you elected to have a penectomy."))
        priority_list.add_entry(PriorityEntry(key=-100, value="You are disgusted by the concept of sexual relations, even with Serena."))
        sze.get_attribute("thirst").observe(AttributeValueMessage(priority_list))


