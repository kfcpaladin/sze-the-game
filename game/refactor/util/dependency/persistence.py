from refactor.persistence import JSONExporter

@JSONExporter.register("dependency_list")
def export_dependency_list(dependency_list):
    data = [] 
    for dependency in dependency_list:
        data.append(dependency.accept(JSONExporter))
    return data

