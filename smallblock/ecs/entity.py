class Entity:

    _next_id = 1

    def __init__(self):
        self.id = Entity._next_id
        Entity._next_id += 1
        self.components = {}

    def add(self, component):
        self.components[type(component).__name__] = component
        return self

    def get(self, component_type):
        return self.components.get(component_type.__name__)

    def has(self, component_type):
        return component_type.__name__ in self.components
