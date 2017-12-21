###########################################################################
screen statsscreen:
    tag menu
    # Include the navigation.
    use navigation
    grid 2 1:
        style_group "prefs"
        xfill True
        vbox:
            frame:
                has vbox
                text "Intellect: [sze.intellect] points"
                if sze.intellect > 100:
                    text "You have surpassed even Justin Wu, dux of James Ruse"
                elif sze.intellect > 75:
                    text "Maybe you'll be able to impress Serena with your 99.95 ATAR"
                elif sze.intellect > 50:
                    text "A bit more hard work and you will truly ACE TRIALS"
                elif sze.intellect > 25:
                    text "At marginally above average intellect"
                    text "You really shouldnt be celebrating yet"
                elif sze.intellect > -1:
                    text "With your remarkably average intellect, your waifu will probably not be impressed"
                elif sze.intellect > -25:
                    text "You are a bit slow, should you even be in a selective school?"
                elif sze.intellect > -50:
                    text "Your test results are probably worse than Chao's tests for STDs"
                elif sze.intellect > -75:
                    text "It's astonishing how you made it to Fort Street. How many dicks did you have to suck to get here?"
                elif sze.intellect > -100:
                    text "With almost no brain activity, the fact that your nervous system still works is a scientific anomaly."
                    text "Hot tip: press the 'KMS' button"
                text " "
                text "charm: [sze.charm] points"
                if sze.charm > 100:
                    text "You slay harder than Hugh Hefner"
                    text "You slay just by looking. Gaze upon the world, your dominion"
                elif sze.charm > 75:
                    text "With that level of charm, you have probably slayed every LG in Sydney by now"
                elif sze.charm > 50:
                    text "You have surpassed even Chao in slaying ability; the teacher becomes the student"
                elif sze.charm > 25:
                    text "You are just very slightly charming"
                elif sze.charm > -1:
                    text "With such exceptionally average charm, its going to take a very long time for senpai to notice you."
                elif sze.charm > -25:
                    text "With your charm, or lack thereof, there seems to be an invisible forcefield repelling girls from you"
                elif sze.charm > -50:
                    text "With that much charm, you are often mistaken for a modern art piece"
                elif sze.charm > -75:
                    text "The average gayness of every room you enter is increased by 100%, due to your charm"
                elif sze.charm > -100:
                    text "You once tried to masturbate, your hand rejected you"
                text " "
                text "strength: [sze.strength] points"
                if sze.strength > 100:
                    text "You are Level S-Class 11th-dan Golden Jade Dragon Jedi Master Ninja Samurai Viking Knight Marshal Admiral"
                    text "You surpass saitama in skill"
                elif sze.strength > 75:
                    text "With your combat propensity, you probably ended 300 spartans with a single one-inch punch."
                elif sze.strength > 50:
                    text "Your skill in a fight would allow you to beat black-belt Aradhya and Jew-jitsu Steven."
                elif sze.strength > 25:
                    text "With such strength, you can probs beat the average student."
                elif sze.strength > -1:
                    text "At your level it is advised that you tactically retreat from your fights."
                elif sze.strength > -25:
                    text "Your below average combat propensity suggests that you have a thing for being dominated."
                elif sze.strength > -50:
                    text "At [sze.strength] combat propensity, the only slaying you know is in Dungeons & Dragons..."
                elif sze.strength > -75:
                    text "With that combat 'proficiency' pussies slays you."
                elif sze.strength > -100:
                    text "Don't fight; you will get rekt so hard, you will be reincarnated as an abortion."
                text " "
                text "thirst: [sze.thirst] points"
                if sze.thirst > 100:
                    text "At a thirst of [sze.thirst], you rival Tiddalik"
                elif sze.thirst > 75:
                    text "You're so thirsty, sometimes moxham appears in your {s}dreams{/s} hallucinations"
                elif sze.thirst > 50:
                    text "With that much thirst, like Roy, you are willing to partake in sexual activities with robots for water"
                elif sze.thirst > 25:
                    text "Even a can of SOLO cannot crush your thirst of [sze.thirst]"
                elif sze.thirst > -1:
                    text "With this much thirstiness, you have the standard healthy desires of a teenage boy of your age."
                elif sze.thirst > -25:
                    text "You have been oft compared to LiXu due to your lack of thirst"
                elif sze.thirst > -50:
                    text "The only thing you drink is mountain dew when playing WoW"
                elif sze.thirst > -75:
                    text "With your lack of desire for water, it is no surprise you have already taken a vow of celibacy."
                elif sze.thirst > -100:
                    text "You elected to have a penectomy, your bladder being sufficient for your needs."
                text " "
                text "fort: [sze.fort] points"
                if sze.fort > 100:
                    text "You are the epitome of the fort, with a Fortianness of [sze.fort]"
                    text "you are a proper protester, you call the police 'pig dogs' and you are part of an anarcho-Maoist-libertarian artist collective"
                elif sze.fort > 75:
                    text "Michael Kirby looks up to you and your fortianness"
                elif sze.fort > 50:
                    text "With that much Fortianness, you would be called in to give talks about social justice"
                    text "But you don't have any white priviledge to acknowledge and you are still straight (you think), cis-gendered scum"
                elif sze.fort > 25:
                    text "With that much Fortianness, you probably can make it into the SRC if you were bothered"
                elif sze.fort > -1:
                    text "At [sze.fort] Fortianness, you are merely a generic student"
                elif sze.fort > -25:
                    text "Your poor fortianness of [sze.fort] suggests you might secretly be a James Ruse spy"
                elif sze.fort > -50:
                    text "At [sze.fort] fortianness, Moxham is willing to engage in the capitalist process of putting a bounty on your head to kill you"
                elif sze.fort > -75:
                    text "With so little fortianness, you're probs a dirty, capitalist, bourgeois pig who might have underlying religious affiliations"
                elif sze.fort > -100:
                    text "With so little fortian- how are you not just expelled at this point?"

        vbox:
            frame:
                has vbox
                text "Serena: [rin.friendship] points"
                text "Willis: [kok.friendship] points"
                text "Fluitsma: [flu.friendship] points"
                text "Rusali: [rus.friendship] points"
                text "Pragash: [pra.friendship] points"
                text "Dean: [dea.friendship] points"
                text "William: [wil.friendship] points"
                text "Chao: [cha.friendship] points"
                text "Grant: [gra.friendship] points"
                text "Moxham: [mox.friendship] points"
                text "Richard:[dik.friendship] points"
                text "Derek: [drk.friendship] points"
                text "Jittian:[jit.friendship] points"
                text "Roy: [roy.friendship] points"
                text "Andrew: [lee.friendship] points"
                text "Aradhya: [but.friendship] points"
                text "Steven: [dng.friendship] points"