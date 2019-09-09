init 1 python:
    # ale
    ale.description = "He is a calculator"
    ale.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain=None,
        msg_loss=None))

    # bil
    bil.description = "A janitor who has a PhD in Chemistry and Physics"
    bil.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain=None,
        msg_loss=None))

    # but
    but.description = "Is a black belt in karate and can eat super-curry"
    but.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="You probably had a deep philosophical debate about politics, increasing your friendship with Aradhya to [but.friendship]",
        msg_loss="You probably made a bad butter pun or mispelt Arradiia's name, causing friendship with him to drop to [but.friendship]."))

    # cha
    cha.description = "He's big and he can squish you. Avoid him at all costs to preserve your virginity!"
    cha.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="If you were a LG, you would be one of Chao's gfs. Friendship with Chao is currently at [cha.friendship]",
        msg_loss="You almost made Chao raep you, friendship with Chao is currently at [cha.friendship]"))

    # dea
    dea.description = "He is obsessed with Halo and his IQ fluctuates more rapidly than Fluitisma's mood"
    dea.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="You have Arbitrarily become more Masterchief to Dean, causing your friendship with Dean to increase to [dea.friendship]",
        msg_loss="You must've confused Masterchief with Masterchef cos he thinks you're a shit, resulting in friendship with Dean to drop to [dea.friendship]"))

    # dik
    dik.description = "Has an impeccable taste in women, quite literally"
    dik.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="You probably listened to some capitalist or historical or weapon related rant, increasing your friendship with Richard to [dik.friendship]",
        msg_loss="You probably use wrong grammar or make rude joke, very annoy Rick Dick, Friendship now is [dik.friendship]"))

    # dng
    dng.description = "Is a fanatic of hard metal, and he once urinated into a pile of tissues, you think..."
    dng.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="You were metal enough for Deng, resulting in friendship with him increasing to [dng.friendship]",
        msg_loss="You probs made bad joke about a female friend of Deng's, or were just retard, lowering friendship with him to [dng.friendship]."))

    # drk
    drk.description = "He and Willis seem to share an intangible bond, one that surpasses your feelings for her"
    drk.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="You probably had deep conversation with him about the Naziness of toilet paper or some shit, raising friendship with him to [drk.friendship]",
        msg_loss="You dirked Derk, causing friendship with him to fall to [drk.friendship]"))

    # flu
    flu.description = "Fluitisma is as emotionally stable as an inverted pendulum. You think she's your physics teacher, but it seems like she's just there to berate you..."
    flu.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="Your phys rank is rapidly rising, as is your friendship with Fluitsma, now at [flu.friendship]. Maybe soon you could get some \"private lessons\"",
        msg_loss="Something you did upset Ms Fluistma. Your current predicted Phys HSC mark is [flu.friendship]. Just kidding, thats your friendship with her"))

    # gra
    gra.description = "Likes to mingle with children, especially you since you are his favourite student. Does not like it when you touch his vices..."
    gra.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="You are probably one of the few students who actually try in engineering. This does not go unnoticed by Grant-senpai, and your friendship with him is now at [gra.friendship]",
        msg_loss="Grant wasnt exactly pleased with your behaviour, resulting in friendship dropping to [gra.friendship]. Looks like you might have to spend some more time in the naughty corner."))

    # jit
    jit.description = "Also known as Gary, his taste in pornographic material is questionable. His laptop is a treasure cove of exotic and potentially illegal material..."
    jit.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="Your friendship with Gary rose to [jit.friendship]. Maybe now he will allow you to access his secret hentai stash.",
        msg_loss="Your friendship with Gary dropped to [jit.friendship]. You probably criticized his interests in chinese \"cartoons\" or something."))

    # kok
    kok.description = "You never see him without Derek, and is your primary opponent in your battle to slay [rin.name]. Unfortunately his charm far exceeds yours, and you are more than likely to lose her to him permanently."
    kok.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="You have strategically gained friendship with Willis, hoping that he will divulge secrets to slaying Serena. It is currently at [kok.friendship]",
        msg_loss="Fuck Willis. \"Friendship\" is currently at [kok.friendship]"))

    # lee
    lee.description = "He aspires to be a future archeitect, and is currently helping your improve your foreign language skills to seduce [rin.name]"
    lee.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="You were lame but its ok coz your friendship with Billabong Lee is at [lee.friendship].",
        msg_loss="You Gullible George, coz your friendship with him is lowered to [lee.friendship]."))

    # mox
    mox.description = "The {color=[PrimaryColours.RED]}{b}dictator{/b}{/color} of this 1984 dystopian knightmare of a school, and is willing to kill anyone who stands between her and Michael Kirby."
    mox.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="Moxham has finally recognised you diligence and continued efforts to improve the school, resulting in your friendship rising to [mox.friendship]",
        msg_loss="Your friendship with Moxham dropped to [mox.friendship]. Looks like more afterschool detentions, suspensions or worse."))

    # pra
    pra.description = "He is a master of economics, and potentially figurehead for your infiltration of the {color=[PrimaryColours.RED]}{b}S.R.C.{/b}{/color}"
    pra.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="If you continue this way, maybe Dynamite Black might mention you in a future song, as friendship with Pragash is currently at [pra.friendship]",
        msg_loss="You weren't very cricket to Pragash, reducing your friendship with him to [pra.friendship]"))

    # rin
    rin.description = "She is the only one you truly desire {b}{s}{rainbow}except maybe your brother{/rainbow}{/s}{/b}"
    rin.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="You grew one step closer with Serena, your friendship with her is now at [rin.friendship]",
        msg_loss="Friendzoned again, your advances towards her were probably rejected, unfortunately your relationship with her has suffered and is now at [rin.friendship]"))

    # roy
    roy.description = "Has the ability to generate a {color=[PrimaryColours.GREEN]}{b}plume of toxic gases{/b}{/color} that is capable of wiping out everyone in the school..."
    roy.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="You improved your friendship with Roy, it is now at [roy.friendship]. You might be safe from his gas attacks, for now.",
        msg_loss="Your friendship with Roy dropped to [roy.friendship]. It is strongly advised that you immediately evacuate the room."))

    # rus
    rus.description = "Tries harder than anyone to slay girls and ace trials, but unfornately cannot do either."
    rus.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="You're [rus.name]'s best friend. Not really, you have to be a girl but you friendshup with him is currently at [rus.friendship]",
        msg_loss="You dogged [rus.name], thus your friendship level with him is currently as [rus.friendship]"))

    # slm
    slm.description = "Your English teacher who is also a hobbit of sorts. Perhaps one day, she can train you to act like Leonardo Decaprio..."
    slm.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain=None,
        msg_loss=None))

    # tod
    tod.description = "An alien from outer space who for some reason is dresses as a {color=[PrimaryColours.GREEN]}{b}leprechaun{/b}{/color}. He/it is skilled in the latest form of alien martial arts, and perhaps could help you defeat your opponent [kok.name] once and forever..."
    tod.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="You new alien karate master has gained some respect for your {b}tenacity and courage{/b}. You are currently at [tod.friendship] friendship with {i}him/it?{/i}",
        msg_loss="Your cowardice and pitiful attitude has disappointed your master, making your friendship drop to [tod.friendship]. His palms, armed with a {color=[PrimaryColours.RED]}{b}life sucking organ{/b}{/color} begins to move towards you."))

    # web

    # wil
    wil.description = "He is an asian kid that you found under the gutters and adopted. Now he plans to restart the {color=[PrimaryColours.RED]}{b}fourth Reich{/b}{/color}, perhaps eliminating you if it is required for his eugenics program..."
    wil.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain="You have further proved to Yang that you belong in his 4th Reich, friendship is currently at [wil.friendship]",
        msg_loss="Ur a fcktard and will, at this rate, fail Yang's eugenics program. Friendship with him is currently at [wil.friendship]"))

    # wiy
    wiy.description = "[wiy.name] suffers from multi-peronality disorder, which causes him to fluctuate between {s}good{/s}less evil and {color=[PrimaryColours.RED]}{b}pure evil{/b}{/color}"
    wiy.get_attribute("friendship").observe(AttributeChangeMessage(
        msg_gain=None,
        msg_loss=None))

    # zhn

