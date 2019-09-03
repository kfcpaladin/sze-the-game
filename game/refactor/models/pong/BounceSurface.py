from abc import abstractmethod

class BounceSurface(object):
    def bounce(self, ball):
        pass

def left_right_bounce(surface, ball):
    if not surface.check_collision(ball):
        return

    # bounce right
    if ball.rect.left < surface.rect.left:
        ball.position.x = surface.rect.right
        ball.velocity.x = abs(ball.velocity.x)
    else:
        ball.position.x = surface.position.x - ball.rect.width
        ball.velocity.x = -abs(ball.velocity.x)