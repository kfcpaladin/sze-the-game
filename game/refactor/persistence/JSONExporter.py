from . import util

JSONExporter = util.serialisation.Visitor()

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

@JSONExporter.register("dependency_list")
def export_dependency_list(dependency_list):
    data = [] 
    for dependency in dependency_list:
        data.append(dependency.accept(JSONExporter))
    return data

@JSONExporter.register("achievement_dependency")
def export_achievement_dependency(dependency):
    data = {}
    data.setdefault("type", "achievement_dependency")
    data.setdefault("id", dependency.id)
    return data

