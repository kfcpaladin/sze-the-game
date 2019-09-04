class KahootViewController(object):
    def __init__(self, total_time):
        self._is_hovered = [False, False, False, False] 
        self._total_time = total_time
        self._time_remaining = total_time
    
    @property
    def total_time(self):
        return self._total_time
    
    @property
    def time_remaining(self):
        return self._time_remaining
    
    @property
    def is_time_ran_out(self):
        return not self._time_remaining > 0

    def update(self, dt):
        time_remaining = self._time_remaining - dt
        if time_remaining < 0:
            time_remaining = 0
        self._time_remaining = time_remaining
    
    def on_hover(self, index):
        self._is_hovered[index] = True
    
    def on_unhover(self, index):
        self._is_hovered[index] = False
    
    def is_hovered(self, index):
        return self._is_hovered[index]

    def get_button_colour(self, index, colour):
        if self.is_hovered(index):
            return colour.opacity(0.5)
        return colour

