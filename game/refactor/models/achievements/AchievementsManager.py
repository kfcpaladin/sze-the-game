class AchievementsManager:
    def __init__(self, loader):
        self._loader = loader

    def add_achievements(self, achievements):
        for _id, old_data in achievements.items():
            self.add_achievement(_id, old_data)

    def add_achievement(self, _id, old_data):
        new_data = {}
        new_data.setdefault("id", _id)
        new_data.setdefault("title", old_data.get("title"))
        new_data.setdefault("brief", old_data.get("brief"))
        new_data.setdefault("description", old_data.get("description"))
        new_data.setdefault("unlock_dependencies", old_data.get("dependencies", []))
        new_data.setdefault("is_hidden", old_data.get("hidden", False))
        self._loader.add_achievement(new_data)

    
    def load(self):
        self._loader.load()

    @property 
    def achievements(self):
        return self._loader.achievements

    @property
    def unlocked_achievements(self):
        return (achieve for achieve in self.achievements if achieve.is_unlocked)

    @property
    def completed_achievements(self):
        return (achieve for achieve in self.achievements if achieve.is_completed)