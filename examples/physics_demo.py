from smallblock.physics import Body, PhysicsWorld

world = PhysicsWorld()

player = Body(
    x=0,
    y=0,
    vx=10,
    vy=0,
    gravity=9.8,
)

world.add(player)

for frame in range(10):
    world.update(0.1)

    print(
        frame,
        round(player.x, 2),
        round(player.y, 2),
        round(player.vx, 2),
        round(player.vy, 2),
    )
