# TODO: Placeholder class - Waiting for refactor
class Clock(object):
    def __init__(self):
        self._times = {} 
    
    @property
    def times(self):
        return self._times.keys()

    def add_time(self, time):
        self._times[time] = False

    def check_time(self, time):
        return self._times[time]

    def set_time(self, time):
        for other_time, _ in self._times.items():
            self._times[other_time] = False
        self._times[time] = True
    
    def get_time(self):
        for time, is_true in self._times.items():
            if is_true:
                return time
        raise ValueError("Time not currently set")