from util.gametools import Controls, Vector2D
import math

class PaddleBot(Controls):
    def __init__(self, paddle, bounds, skill=1):
        self.paddle = paddle
        self.skill = skill
        self.bounds = bounds
        self.inPosition = False
        self._balls = []
    
    def track_ball(self, ball):
        self._balls.append(ball)
    
    def is_ball_incoming(self, ball):
        x_diff = self.paddle.position.x - ball.position.x
        return (x_diff * ball.velocity.x > 0)

    # returns (y_pos, expected_time) 
    def predict_bounce(self, ball):
        position = ball.position.copy()
        velocity = ball.velocity.copy()

        time_of_flight = 0

        for _ in range(self.skill):
            if velocity.y == 0:
                return (position.y, float("inf"))

            if velocity.y < 0:
                new_pos, new_vel = self._predict_down_bounce(position, velocity, self.bounds.top)
                dt = abs(new_pos-position) / abs(velocity)
            elif velocity.y > 0:
                new_pos, new_vel = self._predict_up_bounce(position, velocity, self.bounds.bottom-ball.height)
                dt = abs(new_pos-position) / abs(velocity)

            if new_pos.x > self.bounds.right or new_pos.x < self.bounds.left:
                break

            position = new_pos
            velocity = new_vel
            time_of_flight += dt

        # get line from centre
        line = self._get_line_equation(position+Vector2D(ball.width/2, ball.height/2), velocity)        
        x_intercept = self.paddle.position.x
        y_intercept = line(x_intercept) 
        dt = abs(Vector2D(x_intercept, y_intercept)-position) / abs(velocity)
        time_of_flight += dt
        return (y_intercept, time_of_flight)

    def _get_line_equation(self, position, velocity):
        # y = mx + b
        # dy/dx = m
        # b = y-mx
        m = velocity.y / velocity.x
        b = position.y - (m*position.x)
        return lambda x: (m*x + b)
    
    def _get_inverse_line_equation(self, position, velocity):
        # y = mx + b
        # x = (y-b)/m
        # dy/dx = m
        # b = y-mx
        m = velocity.y / velocity.x
        b = position.y - (m*position.x)
        return lambda y: (y-b)/m
    
    def _predict_down_bounce(self, position, velocity, y_intercept):
        line = self._get_inverse_line_equation(position, velocity)
        x_intercept = line(y_intercept)
        return (Vector2D(x_intercept, y_intercept), Vector2D(velocity.x, +abs(velocity.y)))
    
    def _predict_up_bounce(self, position, velocity, y_intercept):
        line = self._get_inverse_line_equation(position, velocity)
        x_intercept = line(y_intercept)
        return (Vector2D(x_intercept, y_intercept), Vector2D(velocity.x, -abs(velocity.y)))

    
    def move_to_position(self, y):
        # If the bot is not in a position where it can hit the ball
        if self.inPosition is False:
            # Get it to be within middle segment
            if y < self.paddle.rect.top + self.paddle.height/3:
                self.paddle.move_up()
            elif y > self.paddle.rect.bottom - self.paddle.height/3:
                self.paddle.move_down()
            else:
                self.paddle.stop()
                self.inPosition = True
        # if fallen out of position
        else:
            if y < self.paddle.rect.top:
                self.inPosition = False
            elif y > self.paddle.rect.bottom:
                self.inPosition = False
    
    def update(self):
        predictions = []

        for ball in self._balls:
            if self.is_ball_incoming(ball):
                y, dt = self.predict_bounce(ball)
                predictions.append((y, dt))

        if not len(predictions) > 0:
            self.paddle.stop()
            return

        nearest_prediction = min(predictions, key=lambda p: p[1]) # sort by dt
        self.move_to_position(nearest_prediction[0])