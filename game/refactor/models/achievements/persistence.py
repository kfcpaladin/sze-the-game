from refactor.persistence import JSONExporter, JSONImporter, BufferedData
from . import Achievement, AchievementDependency

@JSONExporter.register("achievement")
def export_achievement(achievement):
    data = {}
    data.setdefault("id", achievement.id)
    data.setdefault("title", achievement.title)
    data.setdefault("brief", achievement.brief)
    data.setdefault("description", achievement.description)
    data.setdefault("icon", achievement.icon)
    data.setdefault("is_hidden", achievement.is_hidden)

    data.setdefault("unlock_dependencies", achievement.unlock_dependencies.accept(JSONExporter))
    data.setdefault("complete_dependencies", achievement.unlock_dependencies.accept(JSONExporter))    

    return data

@JSONExporter.register("achievement_dependency")
def export_achievement_dependency(dependency):
    data = {}
    data.setdefault("type", "achievement_dependency")
    data.setdefault("id", dependency.id)
    return data

@JSONImporter.register("achievement")
def import_achievement(data):
    _id = data.get("id")
    title = data.get("title")
    brief = data.get("brief")
    description = data.get("description")
    is_hidden = data.get("is_hidden", False)
    icon = data.get("icon", None)

    achievement = Achievement(_id, title, brief, description, is_hidden=is_hidden, icon=icon)
    
    unlock_dependencies = data.get("unlock_dependencies", [])
    complete_dependencies = data.get("complete_dependencies", [])

    for unlock_dependency in unlock_dependencies:
        data = BufferedData("dependency", unlock_dependency)
        data.add_buffered_operation(achievement.add_unlock_dependency)
        JSONImporter.add_buffered_data(data)
    
    for complete_dependency in complete_dependencies:
        data = BufferedData("dependency", complete_dependency)
        data.add_buffered_operation(achievement.add_complete_dependency)
        JSONImporter.add_buffered_data(data)

    JSONImporter.cache_object(("achievement", achievement.id), achievement)
    return achievement

@JSONImporter.register("dependency")
def import_dependency(data):
    _type = data.get("type", None)
    if _type == "achievement_dependency":
        return JSONImporter.visit(_type, data)
    
    raise ValueError("Unknown dependency type {0}".format(_type))

@JSONImporter.register("achievement_dependency")
def import_achievement_dependency(data):
    _id = data.get("id")
    achievement = JSONImporter.fetch_cached_object(("achievement", _id))
    if achievement:
        return AchievementDependency(achievement)
    else:
        raise ValueError("Unknown achievement dependency for {0}".format(_id))
