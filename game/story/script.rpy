# INTRODUCTION
define pov = Character('[povname]')
label start:
    if config.developer:
        $ logDefaultCache() # for debugging improperly read files
    $ autosave()
    stop music fadeout 3.5
    image blank = im.Recolor(loadImage("bg_arthur.png"), 255, 255, 255, 0)
    scene bg disclaimer
    if config.developer and not game.hasDiary:
        $ game.hasDiary = True
        "As a developer you gain access to the diary immediately"
        "Go to /game/scripts/options.rpy, and make config.developer = false to remove this"
    if game.hasDiary:
        show screen float_menu
    with fade
    pause
    scene black
    with fade
    scene bg intro
    with fade
    pause
    scene bg bdr1night
    with fade
    $ playmusic("SGriffinAriaOfTheSoulPersonaCover.ogg")
    "Greetings"
    "I am the Narrator of this {i}Chanson de Geste{/i}, this interactive, prose epic concerning the life of a man."
    "Whether this hero's journey becomes a tragedy, a comedy, a comedic tragedy or a tragic comedy"
    "or just the dull records of another face in the crowd"
    "is up to you to decide."
    "I suppose that raises a question..."
    python:
        povname = renpy.input("Who are you?")
        if not povname:
            povname = "Uszeless"
    "Not your name, I couldn't care less what you call yourself."
    "I suppose, for the purposes of this tale, you are some archetype of our Hero's collective unconscious. I don't know which one in particular"
    "simply that you are a guiding force. Your decisions will be acted upon, subconsciously, of course, by the Hero."
    "Hm? You might be asking, \"Well then, who/what are you, Narrator?\""
    "I'd like to think that I'm the Wise Old Man, the senex, but that might be wishful thinking."
    "Think of me as another voice in the chorus of his collective unconscious and leave it at that, for now."
    "So just call me the Narrator."
    "Curiously, it seems that our Hero is somewhat aware of me, assuming that I am perhaps just a part of his own stream of consciousness."
    "But no, it seems he has a main spokesperson for his thoughts, more articulate in speech than his actual self."
    "This is Arthur Sze."
    show sze normal
    sze "Hi"
    "Or rather, his thoughts"
    sze "Really?"
    "You can tell the difference between Arthur's thoughts, and what he actually says, with the presence of \"quotation marks\", as expected."
    sze "\"Like this?\""
    "Yes, but Arthur's meant to be asleep, right now."
    sze "oh oops..."
    hide sze normal
    with dissolve
    "Well, the damage is done. It seems that he's now in slow-wave sleep; it will soon be untenable for us to keep this 'dream' stable"
    "so a few more words, as Sze seems to be waking in a bit."
    "You won't be able to directly communicate with Sze; the closest thing you can do, besides directing his actions, is \"speaking\" through his thoughts."
    sze "Oi!"
    "Shut up, no one cares what the spokesperson \"thinks\"."
    sze "You what?"
    "Think of Sze's thoughts as a spokesperson, who you can hijack, on extremely rare occasions."
    "As for myself... I must confess, that I am not entirely of Sze"
    "It's complicated..."
    "Sure, I guess I am of Sze's thoughts. But are one's thoughts entirely one's own?"
    "What I mean is, you might be able to guide Sze to meet me. However, a word of warning; a meeting with me, or those of my kind"
    "is usually a sign of approaching calamity." 
    "So perhaps, you should consider forgo making Sze meet me"
    "and instead let me remain merely a figment of his imagination, narrating his path."
    stop music fadeout 1.5
    sze "..."
    sze "Hmm...It appears that such heady discussion is making Sze less sze-leepy"
    scene bg bdr1dwndsk
    with fade
    sze "..."
    sze "\"...urgh\""
    sze "\"that was a fucking weird dream\""
    sze "\"let's try to go back to sleep\""
    "Arthur's bladder objects to such a notion."
    sze "\"...\""
    sze "\"fk u bladder, why do you even exist?\""
    "The Year is 2015"
    "It is the first day of school and you do not look forward to another miserable year of Fort Street."
    "But nevertheless, you pack your bags, and get ready, resigned to another year of mediocrity."
    "Fort Street High School..."
    "The oldest public high school on the continent, it gets its fair share of academically talented students through the Selective school test, along with the occasional transfer."
    "However, it is no longer as prestigious as it used to be; other schools have risen and overtaken the Fort in regards to academic ability."
    "Most notably, James Ruse Agricultural High School, which is now the Zeus of the pantheon of high schools."
    "As for yourself, you're just an average student in the Fort. Which, because it's academically selective, makes you a bit above average."
    "But don't flatter yourself; you aren't exactly stellar."
    "In fact, you're so average, you could almost be the star of {s}a visual novel{/s} a generic anime."
    "And every high school anime must have a love interest."
    stop music
    sze "I had always loved her, since she first graced my eyes in Year 7."
    show bg field
    with fade
    $ playmusic("Herbert von Karajan -Intermezzo Sinfonico- Cavalleria Rusticana.ogg")
    sze "Her name is Serena, a name which evokes images of clear, running brooks, and endless fields of wildflower meadows"
    hide bg field
    with dissolve
    show bg parisafremov
    with fade
    sze "Or perhaps it conjures an image of quaint Parisian cafes at night"
    sze "beside a rose garden in fragrant bloom, with the moon and stars out in full, and Mascagni's Cavalleria Rusticana: Intermezzo of Act 1 played softly in the background"
    sze "But for now, her name wrings out nought but sadness. More sadness than another year of school."
    "But was High School as sad as Sze made it out to be? To understand that much require some more stories....more perspective..."
    #You can now tack on side stories for which the player can try
    menu AltPerspectives:
        "Which of these stories would you like to see?"
        "The WrongHow Causality Hypothesis":
            jump WrongHow1
        "Return me to Sze's perspective":
            jump schoolday1
