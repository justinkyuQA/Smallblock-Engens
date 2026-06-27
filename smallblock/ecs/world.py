class World:

    def __init__(self):
        self.entities = []

    def create(self):
        from .entity import Entity
        e = Entity()
        self.entities.append(e)
        return e

    def each(self, component_type):
        for entity in self.entities:
            if entity.has(component_type):
                yield entity
