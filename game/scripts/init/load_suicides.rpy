init -1 python:
    def create_gunshot_suicide_view_controller():
        from models.suicides.gunshot import GunshotSuicide, Head
        from models.suicides.gunshot import Shotgun, Pistol
        pistol = Pistol(
            width=200,
            height=150,
            bullet_velocity=config.screen_width/0.5,
            round_size=20)
        
        shotgun = Shotgun(
            width=350,
            height=150,
            bullet_velocity=config.screen_width/0.6,
            round_size=25,
            spread_angle=5
        )
        
        head = Head(width=200, height=300)
        head.position = Vector2D(200, 200)

        bounding_box = Rect2D(right=config.screen_width, bottom=config.screen_height)

        gunshot_suicide = GunshotSuicide(bounding_box, head, shotgun)

        controller = GunshotSuicideViewController(gunshot_suicide)

        return controller