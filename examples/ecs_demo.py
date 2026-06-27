from smallblock.ecs import World
from smallblock.components import Transform

world = World()

player = world.create()
player.add(Transform(100, 200))

enemy = world.create()
enemy.add(Transform(40, 80))

for entity in world.each(Transform):
    t = entity.get(Transform)
    print(
        f"Entity {entity.id}:",
        t.position
    )
