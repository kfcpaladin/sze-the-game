label kahootGame(question):
    menu:
        "Start Kahoot?":
            $ _previousMusic = getMusicHistory(-1)
            $ playmusic("kahoot.ogg")
            $ controller = KahootViewController(total_time=10)
            call screen screen_kahoot(question, controller)
            $ stopmusic()
            $ answer = _return
            if answer is not None:
                "[answer.message]"
            else:
                "You had a seizure and couldn't answer the question"
            if answer.points > 0:
                $ playmusic("p4LikeADreamComeTrue.ogg")
                "You are victorious with [answer.points] points, sparing only [controller.time_remaining] seconds"
                "This new found academic brilliance of yours makes you feel something {b}interesting{/b}"
                $ sze.intellect += 10
            else:
                "The class stares at you, perhaps thinking of how {i}retarded{/i} you are"
                $ sze.intellect -= 4
            $ playmusic(_previousMusic)
            return
        "Pussy out":
            "Your knees start shaking and your penis recedes into its cavity"
            "Finally you give up on the game of Kahoot"
            return

# handles all screen elements
screen screen_kahoot(question, controller, theme=themes.kahoot, rect=view_controllers.screen_rect):
    modal True
    default answers = question.answers
    timer 0.1:
        repeat True
        action If(
            not controller.is_time_ran_out,
            true=[Function(controller.update, 0.1)], 
            false=[Hide('kahootscreen', dissolve)])

    frame:
        background Solid(theme.background)

    use kahoot_timer(controller, theme, Rect2D(right=100, bottom=100).add_offset(Vector2D(50, 250)))    
    use kahoot_question(question, theme)
    use kahoot_answer_grid(answers, controller, theme, rect)

screen kahoot_question(question, theme):
    frame:
        xfill True
        xalign 0.5
        ysize 100
        background Solid(theme.title_background)
        frame:
            background Solid(PrimaryColours.CLEAR)
            xalign 0.5
            yalign 0.5
            text "{color=[theme.title_text]}{size=30}{font=[theme.font]}[question.description]{/font}{/size}{/color}"

screen kahoot_answer_grid(answers, controller, theme, rect):
    default answer_rect = Rect2D(right=rect.width/2-15, bottom=100)
    grid 2 2:
        xoffset 10
        yoffset rect.height-200-20
        xspacing 10
        yspacing 10
        use kahoot_answer(answers[0], 0, controller, theme, colour=theme.red, rect=answer_rect)
        use kahoot_answer(answers[1], 1, controller, theme, colour=theme.blue, rect=answer_rect)
        use kahoot_answer(answers[2], 2, controller, theme, colour=theme.yellow, rect=answer_rect)
        use kahoot_answer(answers[3], 3, controller, theme, colour=theme.green, rect=answer_rect)

screen kahoot_answer(answer, index, controller, theme, colour, rect):
    frame:
        xsize rect.width
        ysize rect.height
        background Solid(controller.get_button_colour(index, colour))
        textbutton "{color=[theme.light_text]}[answer.description]{/color}":
            background Solid(PrimaryColours.CLEAR)
            xalign 0.5
            xfill True
            yfill True
            action [
                Hide("kahootScreen", dissolve),
                Return(answer)]
            hovered [
                Function(playsfx, "button_select.ogg"),
                Function(controller.on_hover, index)]
            unhovered [Function(controller.on_unhover, index)]

screen kahoot_timer(controller, theme, rect):
    frame:
        xpos rect.left
        xsize rect.width
        ypos rect.top
        ysize rect.height
        background Solid(theme.primary_accent)
        text "{b}{color=[theme.light_text]}[controller.time_remaining]{/colour}{/b}":
            xalign 0.5
            yalign 0.5

#################################################################################
#timer bar
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

