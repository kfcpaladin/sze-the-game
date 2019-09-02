class FriendViewController(object):
    def __init__(self):
        self._friend = None

    @property
    def friend(self):
        return self._friend

    def select_friend(self, friend):
        self._friend = friend

    def get_friend_colour(self, friend, theme):
        if friend.friendship > 0:
            return theme.positive
        elif friend.friendship < 0:
            return theme.negative
        return theme.neutral