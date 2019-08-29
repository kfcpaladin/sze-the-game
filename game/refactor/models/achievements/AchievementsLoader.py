from .Achievement import Achievement
from .AchievementDependency import AchievementDependency

class AchievementsLoader:
    def __init__(self):
        self._dependencies = {}
        self._achievements = {}
        self._achievements_as_deps = {}
        self._is_loaded = False

    def add_achievement(self, data):
        if self._is_loaded:
            raise Exception("Cannot add more achievements after they are all loaded")

        achievement = self._create_achievement(data)
        unlock_dependencies   = self._assert_not_null(data.get("unlock_dependencies", []))
        complete_dependencies = self._assert_not_null(data.get("complete_dependencies", []))

        self._register_achievement(achievement, unlock_dependencies, complete_dependencies)

    @property
    def achievements(self):
        return (achievement for achievement, _, _ in self._achievements.values()) 
        
    def load(self):
        self._create_dependencies()
        self._is_loaded = True

    def _create_achievement(self, data):
        _id         = data.get("id", "")
        title       = data.get("title", "")
        brief       = data.get("brief", "")
        description = data.get("description", "")
        icon        = data.get("icon", None)
        is_hidden   = data.get("is_hidden", False)

        achievement = Achievement(_id, title, brief, description, is_hidden=is_hidden, icon=icon)
        return achievement

    def _create_dependency(self, data):
        achievement_dep = self._achievements_as_deps.get(data, None)
        return achievement_dep

    def _create_dependencies(self):
        for _id, (achievement, unlock_deps, complete_deps) in self._achievements.items():
            for dependency_data in unlock_deps:
                dependency = self._create_dependency(dependency_data)
                if dependency:
                    achievement.add_unlock_dependency(dependency)
            
            for dependency_data in complete_deps:
                dependency = self._create_dependency(dependency_data)
                if dependency:
                    achievement.add_complete_dependency(dependency)

    def _assert_not_null(self, value):
        if value is None:
            raise ValueError("Loaded a null value")
        return value


    def _register_achievement(self, achievement, unlock_dependencies, complete_dependencies):
        _id = achievement.id
        self._achievements.setdefault(
            _id, 
            (achievement, unlock_dependencies, complete_dependencies)
        )
        self._achievements_as_deps.setdefault(
            _id,
            AchievementDependency(achievement)
        )
    

