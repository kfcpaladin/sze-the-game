label asszembly1jigolo:
    sze "\"I need to put some stuff in my locker\""
    wil "\"...\""
    pra "\"Alright, see you at assembly\""
    sze "\"uh...yeah...\""
    dea "\"BYEEEE!!!\""
    "You hurry off back to the Rowe corridor, trying not to look suss"
    scene bg rowecorridor
    jit "\"Who's that?\""
    sze "\"Fuck\""
    menu:
        "Run":
            "You run to assembly like the chicken that you are"
            sze "{cps=*1.5}BOk BOk BOk BOk BOk{/cps}{nw}"
            sze "That was a close call"
            $ sze.strength -= 1
            jump asszembly1_2
        "Sneak up on the source of the sound":
            "You sneak up on the source of the sound"
            sze "\"...\""
            $ playsfx("vpunch.ogg")
            jit "\"Whoa, SHIT!\"" with vpunch
            sze "\"Oh, it's just Gary\""
            sze "{cps=*1.5}Gary/Jitian is a shady, food-smuggling, hentai-watching{/cps} {nw}"
            sze "{s}Jitian{/s} is a great guy with a taste for questionable animes..."
            $ jit.friendship -= 1
            jit "\"Can u not, like plz? I thought you were teacher\""
            sze "\"Soz, why you here?\""
            jump asszemblyjigolo1_2
        "You confront the speaker":
            "You walk up to the speaker, without attempting to disguise your approach"
            jit "\"Oh, hi Arthur\""
            sze "{cps=*1.5}Gary/Jitian is a shady, food-smuggling, hentai-watching{/cps} {nw}"
            sze "Gary/Jitian is a great guy with a taste for questionable animes..."
            sze "\"lol, why you always so shifty?\""
            $ sze.strength += 1
            jit "\"Shut the fuck up, there might be teachers...\""
            sze "\"Well, I'm planning on ditching the assembly\""
            jump asszemblyjigolo1_2

label asszemblyjigolo1_2:
    jit "\"Arrite, so long as you don't be dog, we'll be fine with you here\""
    jit "\"Follow me, and listen... If u see a teacher, bail yeh.\""
    "You see a couple of other people milling about"
    sze "\"Where are we going?\""
    jit "\"The Rowe Dungeon\""
    sze "\"Fuck, not there! We'll get destroyed by the principal\""
    jit "\"That's not it, son! Y would we use that one? That one's the legendary Cohen Dungeon\""
    jit "\"U must be munted to not know dat\""
    "You follow Gary to Rowe Dungeon"
    jit "\"Hey Sze, check this out\""
    menu:
        "Look at the stuff on Gary's laptop":
            jit "\"This is quality anime\""
            sze "\"Lol why is there a bunch of schoolgirls and some tentacles {nw}\""
            sze "\"Oh\""
            $ sze.thirst += 1
            jit "\"Oh ho ho ho\""
            jit "\"This is the good bit\""
            "..."
            "You go to wash hands"
            $ sze.thirst += 1
            jit "\"That was good scene wasn't it?\""
            sze "\"...yea...is ok, i guess\""
            $ jit.friendship += 1
            jump asszemblyjigolo1_3

        "Study":
            sze "\"No ty, I need to study for HSC\""
            jit "\"Relax it's still the first day of year 11\""
            sze "\"But William is already doing 50 HSC papers per day\""
            #that moment when someone has more than 150 hours per day...
            jit "\"He's going to get 99+ ATAR anyway, he's just one of those guys\""
            jit "\"And then there are some others who will go all tryhard yet still get rekt. No offence mate\""
            "You ponder the philosophical nature of intelligence and ruminate upon the mysteries and questions of epistemology"
            $ sze.intellect += 1
            "You then direct your focus to your work, this time examining the ways of the locus"
            $ sze.intellect += 1
            jit "\"Whoa ok chill calm down\""
            jit "\"Don't need to be that try hard\""
            jump asszemblyjigolo1_3

        "Talk to Gary" if game.electionPromise is True:
            sze "\"Actually, I wanted to ask you something\""
            jit "\"Eh? I'm watching my pronz tho\""
            sze "\"...k...\""
            jit "\"Yeah, what is it?\""
            sze "\"For some reason...Will Yang wants Pragash to run for SRC\""
            jit "\"lol that would be funny, considering how they kicked him off\""
            jit "\"But idk man, these days, Yang always has an agenda...seems kinda shifty to me...\""
            "The thought never occurred to you but Gary's warning has made you more alert...ish"
            $ sze.strength += 1
            sze "\"I'll leave you to your hentai then\""
            jit "\"*nods* thanks mate\""
            $ jit.friendship += 1
            jump asszemblyjigolo1_3

label asszemblyjigolo1_3:
    "You suddenly hear heavy footsteps echoing down the corridor leading to the stairs to the dungeon"
    "Gaz stops and looks up"
    jit "\"Shit, go see what's going on...quietly\""
    sze "\"Why me?\""
    jit "\"Just cos brah...u need to do it...do it for the Africans\""
    sze "\"I don't see any Africans{nw}\""
    jit "\"We're all from Africa cos Science\""
    sze "\"Yeah, but we're not Africans cos we're not black{nw}\""
    jit "\"U being racist? Ever heard of Afrikaans? Are u denying the white colonisation of Africa and by extension the subsequent genocides and the apartheid?\""
    sze "\"What? No?!\""
    sze "\"But we're not white either\""
    jit "\"We're in Australia tho... ur pretty much white boi in the eyes of ur ancestors\""
    sze "\"Fine...\""
    jit "\"Look, mate, just sneak out, take a peek, return and report\""
    "You hear more footsteps, this time drawing closer to the top of the stairs\""
    sze "\"...\""
    jit "\"Go... go up and look\""
    sze "\"...\""
    menu:
        "Continue arguing" if jit.friendship <=2:
            sze "\"Jitian, I really don't want to tho\""
            jit "\"...\""
            jit "\"omfg...Just\""
            jit "\"Go out there\""
            jit "\"Look\""
            jit "\"See who it is\""
            jit "\"Come back\""
            jit "\"Ez pz\""
            sze "\"{b} What if it is a teacher {/b}\""
            jit "\"{b} stfu, if it is then they can hear you {/b}\""
            "Turns out, it wasn't a teacher"
            "It was a patrol of them"
            "\"{i} {b} Oi, you there! STOP! {/b} {/i}\""
            jit "\"fml, fcking Arthur\""
            $ jit.friendship -= 1
            sze "\"Why is it my fault?\""
            $ jit.friendship -= 1
            jit "\"U for realz??? I don't even...\""
            $ jit.friendship -= 1
            "You sense that Gary is somewhat reluctant to talk to you now..."
            "\" {i} Stop moving, put everything in your bags, place your hands behind your head, interlock your fingers...{/i} {nw}\""
            sze "\"fuck fuck fuck fuck fuck\""
            sze "\"knew I shouldn't've jigged\""
            "You endure the march of shame in silence"
            "..."
            "..."
# need scene change {reminder}
            "You finally arrive at the Fountain quad in front of the school hall and wait for asszembly to end"
            jump asszembly1shitstorm
# check mox counter, if >=1 = suspension, if <1 = detention after school
        "Don't look just run" if sze.intellect >=3:
            sze "\"Wait...\""
            jit "\"?...\""
            sze "\"It can't be random students cos this place is too far away from the hall or the toilets\""
            jit "\"Oh shit tru...Everyone bail, sneak out\""
            jit "\"Oh tru...smart, Sze, good job\""
            $ jit.friendship += 1
            "Everyone sneaks through the side door of the Rowe Dungeon just as the footsteps reach the stairwell"
            "You hear the pursuers' voices in the room you just left"
            "\"{i} I thought I saw movement... {/i}\""
            scene bg schoolfront
            with fade
            jump fugitivesfromasszembly1

        "Go look":
            sze "\"Fine\""
            sze "Climbing stairs is pretty shitty"
            sze "\"!\""
            jump asszembly1shitstorm

        "Dog the bois":
            sze "\"Fuck this shit, I'm out!\""
            jit "\"Oi, you can't just leave\""
            sze "\"Really?\""
            jit "\"errrr....\""
            sze "\"cya\""
            $ jit.friendship -= 1
            scene bg schoolfront
            jit "\"not so fast, where you going?\""
            sze "\"idk, eff this, I'm out\""
            "You turn your head, seeing the chaos of a patrol of teachers hunting down the hopeless students of Rowe\""
            jump fugitivesfromasszembly1

label fugitivesfromasszembly1:
            jit "\"Whew...Sze let's go, find somewhere to hide\""
            sze "\"k, you lead the way\""
            jit "\"Nah, you probs have better ideas as to what would be best place to go to\""
            sze "\"Whaa- fine\""
            menu:
                "\"Toilets\"":
# Include scene change - toilet
                    sze "\"What about the toilets?\""
                    jit "\"Mate, that's pretty grot\""
                    sze "\"You said I would probs have better ideas\""
                    sze "\"This is my better idea\""
                    jit "\"Still pretty crap\""
                    jit "\"{cps=*0.2}...{/cps} See what I did there >.< EHHHHHHH???\""
                    sze "\"fuk off\""
                    jit "\"Fine let's go\""
                    call asszemblyjigolo1encounter
                    jit "\"That was too fucking close\""
                    jump asszemblyjigolokindagaytoilet

                "\"Outside the school\"":
# scene change - norton st
                    sze "\"Let's just go outside school\""
                    jit "\"Hmmmm {cps=*0.2}...{/cps} Interesting suggestion\""
                    sze "\"Nothing but fence in the way\""
                    jit "\"Whoa, whoa, Arthur is a badass, step back\""
                    $ sze.fort -= 1
                    jit "\"You lead, then\""
                    call asszemblyjigolo1encounter 
                    jump asszemblyjigolodiscoverthefood

                "\"Play with vices\"":
# scene change - darkened workshop
                    sze "\"{s}I wanna play with vices{/s} Let's go to a classroom, like the engineering workshop\""
                    jit "\"Wow, are you gay for Mr. Grant?\""
                    sze "\"No, I just think it is a good place to hide\""
                    jit "\"Suuurre...\""
                    sze "\"Got any idea for a less \"gay\" place to hide in then?\""
                    jit "\"Your mum's pussy\""
                    sze "\"...can you not\""
                    jit "\"soz, you lead\""
                    call asszemblyjigolo1encounter
                    jump asszemblyjigoloviceland

#    to be continued...
#    Dog the bois -> 2 options go back to assembly, run on for a long time -> go back to assembly -> dog bois again/ sneak back in// run on for a long time -> jit finds you, lose friendship, link to don't look just run
#    Yang-kor Wat -> Yang's Ministry of Public Relations (e.g. Yang's Church of Yangology)
            jump dead

label asszemblyjigolo1encounter:
    "You move towards your destination"
    $ playsfx("vpunch.ogg")
    "{cps=*0.2}...{/cps}" with vpunch
    $ playsfx("hpunch.ogg")
    "{cps=*0.2}...{/cps}" with hpunch
    jit "\"Wait...I think I hear some more teachers\""
    sze "\"Shit, again?!\""
# a bit of johnny cash could work here
    menu:
        "\"I Surrender\"":
            sze "\"I reckon we should just surrender\""
            $ sze.strength -= 1
            jit "\"wow\""
            sze "\"Soz, but I just too szeebs\""
            jit "\"Well, fuck\""
            $ jit.friendship -= 1
            jit "\"Cya, I ain't staying around for the teachers to catch up\""
            sze "\"...\""
            jump asszembly1shitstorm

        "\"Run\"":
            sze "\"I am a human being\""
            sze "\"capable of doing terrible things\""
            jit "\"wot?\""
            sze "\"run\""
            "\"Both you and Jitian bolt off across the school\""
            $ playsfx("hpunch.ogg")
            "\"...\"" with hpunch
            $ playmusic("p3MassDestruction.ogg")
            "\"Right into another patrol of teachers\""
            jit "\"Ohhhhhhhh FAARk\""
            sze "3 teachers...assuming they have combat score of 3 each and a combined arms bonus of 3, I will require a combat score of greater than 12 to beat all of them..."
            sze "For some reason, I think I should check my stats"
            sze "lolwut, random thoughts..."
            menu:
                "\"I Surrender\"":
                    sze "\"I reckon we should just surrender\""
                    $ sze.strength -= 1
                    jit "\"wow\""
                    jit "\"You were supposed to be the Chosen One... the Hero...\""
                    sze "\"Soz, but I just too szeebs\""
                    jit "\"Well, fuck\""
                    $ jit.friendship -= 1
                    jit "\"Cya, I ain't staying around for the teachers to catch up\""
                    sze "\"...\""
                    jump asszembly1shitstorm
                "\"Stand our ground\"":
                    jit "\"Shit, I'm out of here\""
                    "\"Your courage fleetingly flees from you...\""
                    "\"But then you realise that, if caught you will probably be suspended, if suspended you can no longer see Serena\""
                    "\"You steel your heart\""
                    sze "\"No Jitian...today we do not flee\""
                    sze "\"Today we stand our ground\""
                    jit "\"Mate, are you fucking munted? We're gonna get rekt- {nw}\""
                    sze "\"I see in your eyes the same fear that would take the heart of me\""
                    jit "\"Fuk off, I don't want to get sued for copying Aragorn on top of getting caught by Moxham's cronies\""
                    if sze.intellect >=4:
                        sze "\"If we fight good, we won't get caught\""
                        sze "\"If we get caught we will face a fate worse than death by the minions of Sauron\""
                        sze "\"{s}I will not be able to sze Serena{/s} We will have to face the wrath of Moxham\""
                        $ playsfx("hpunch.ogg")
                        jit "\"Let's fight then!!\"" with hpunch
                        $ _jig1fight1a = renpy.random.randint(0, 6) + int(sze.strength)*2 + int(sze.intellect) + int(jit.friendship)
                        if _jig1fight1a > 12:
                            "With Jitian by your side, you stand your ground"
                            $ playsfx("vpunch.ogg")
                            "The teachers thunder towards you" with vpunch
                            $ playsfx("vpunch.ogg")
                            "They begin to wail on you" with vpunch
                            "But your iron defence holds out"
                            jit "\"You truly are the Chosen One\""
                            "With one last co-ordinated push, you repel their attack and knock them unconscious"
                            $ playmusic("p3_JikaNetTanaka.ogg")
                            $ sze.strength += 1
                            "Exhausted, you both decide to take a breather, when suddenly you hear rustling"
                            bil "\"Well, now this is a proper mess\""
                            sze "Oh no, the school janitor/cleaner. He must be here to clean us up"
                            bil "\"Relax, I offer my cleaning services to all who require it, unless you're talking about the school toilets cos those are complicated.\""
                            bil "\"And I see that you are in need of such services\""
                            sze "\"Ok...but is there a catch, cos otherwise I ceebs?\""
                            bil "\"Normally there is a fee, but current Fortians receive a 100 percent student discount\""
                            jit "\"Still kinda too expensive though, considering we did the school a service\""
                            "Bill the Cleaner begins to get to work on the unconscious teachers, injecting them with an unknown substance"
                            menu:
                                "\"Ask what he's doing\"":
                                    sze "\"What are you injecting them with?\""
                                    bil "\"...\""
                                    bil "\"Don't ask question you don't want answers to\""
                                    bil "\"Just kidding, Fort Street is a school of academic excellence and a house of learning\""
                                    bil "\"I'm injecting them with a solution of benzodiazepines and alcohol; the ratio and the specific benzo is a trade secret\""
                                    bil "\"This impacts their memory, inducing short-term amnesia. As for any side effects, they won't really be any. Kind of\""
                                    sze "Wow, I learnt some science; benzodiazepine and alcohol can make short term amnesia"
# will be included in end of term chemistry
                                    $ sze.intellect += 1
                                    jit "\"Damn, I should try that some time\""
                                    sze "\"What for?\""
                                    jit "\"...you don't wanna know\""
                                    bil "\"Move along and keep quiet, otherwise I may have to remove some of your short term memories\""
                                    "Unsure of his seriousness, you continue onwards with Gary"
                                    return
                                "\"Let's keep moving\"":
                                    sze "\"I reckon we shouldn't ask too many questions, it seems dangerous\""
                                    jit "\"Yeah, that guy is kinda shift, bruh\""
                                    $ jit.friendship += 1
                                    return
                        else:
# finish
                            "Both you and Jitian put up a valiant defence"
                            "THey slowly wear you down, causing the two of you to leave gaps"
                            "But since the scripter couldn't be bothered finishing this part right now, you automatically lose"
                            "\"{b}RIP, bad luck for you and your buddy, kiddo {/b}\""
                            jump asszembly1shitstorm

                    else:
                        sze "\" WOLOLOLOLOLOLOLOLOLOLO!\""
                        $ playsfx("hpunch.ogg")
                        "You unleash what you think is a terrifying warcry" with hpunch
                        "You succeed in scaring Jitian away"
                        $ _jig1fight1b = renpy.random.randint(0, 6) + int(sze.strength)*2 + int(sze.intellect)
                        if _jig1fight1b > 12:
                            "Picking up a stick, you steel yourself as the teachers charge"
                            "jabby jabby"
                            sze "\"one day I will finish this fight properly\""
#                           finish him...
                            jit "\"good job\""
                            jit "\"we sure did nail them, right?\""
                            sze "\"...\""
                            sze "\"who dafuq are you?\""
                            jit "\"calm down mate\""
                            return
                        else:
                            sze "\"fuck\""
                            "\"{b}Tsk tsk tsk, you know this violence is an un-Fortian of ejaculating your emotions{/b}\""
                            "\"Time to turn the tables and inject you with some re-education; all resistance will be penetrated, the same goes for your friend\""
                            jit "\"Calm the fuck down, you don't need to grope my fuckin' arm off\""
                            jit "\"Plus, I'm the master of re-education\""
                            "\"{b}Not when we're through with properly... analysing you{/b}\""
                            jit "\"awww hell no...\""
                            sze "Resistance is futile, best to follow them"
                            jump asszembly1shitstorm

# time for fight coding -> to succeed need total 5, dice roll 1-6 + strength*2 + intelligence + jit.friendship if he joins in...
                "\"Fight\"":
                    sze "\"Let's fight\""
                    jit "\"wut\""
                    sze "\"by running\""
                    $ sze.strength -= 1
                    jit "\"lol gud idea\""
                    return
