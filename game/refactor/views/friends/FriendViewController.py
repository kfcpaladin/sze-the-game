class FriendViewController(object):
    def __init__(self):
        self.positive_colour = None
        self.neutral_colour = None
        self.negative_colour = None
        self._friend = None

    @property
    def friend(self):
        return self._friend

    def select_friend(self, friend):
        self._friend = friend

    def get_friend_colour(self, friend):
        if friend.friendship > 0:
            return self.positive_colour
        elif friend.friendship < 0:
            return self.negative_colour
        
        return self.neutral_colour