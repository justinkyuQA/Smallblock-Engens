import time

from smallblock.graphics.renderer import Renderer
from smallblock.camera import Camera
from smallblock.sprites import Sprite
from smallblock.physics import Body

renderer = Renderer(64, 24)
camera = Camera()

player = Sprite("""
@@
@@
""")

body = Body(10, 10)

while True:

    cmd = input("WASD (q quit): ").lower()

    if cmd == "q":
        break

    body.vx = 0
    body.vy = 0

    if "a" in cmd:
        body.vx = -1
    if "d" in cmd:
        body.vx = 1
    if "w" in cmd:
        body.vy = -1
    if "s" in cmd:
        body.vy = 1

    body.update(1.0)

    camera.x = body.x - 20
    camera.y = body.y - 10

    renderer.clear()

    sx, sy = camera.world_to_screen(body.x, body.y)

    renderer.sprite(player, sx, sy)

    renderer.text(1, 1, "SmallBlock Integration Demo")
    renderer.text(1, 2, f"World: ({body.x:.1f}, {body.y:.1f})")

    renderer.present()

    time.sleep(0.03)
