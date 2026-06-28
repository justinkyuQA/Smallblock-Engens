import time

from smallblock.runtime import RuntimeManager
from smallblock.graphics.renderer import Renderer
from smallblock.sprites import Sprite
from smallblock.camera import Camera
from smallblock.collision import rects_overlap
from smallblock.input import Keyboard


class GameDemo:

    def __init__(self):
        self.enabled = True

        self.renderer = Renderer(64, 24)
        self.camera = Camera()
        self.keyboard = Keyboard()

        self.player = Sprite("""
 /\\
/__\\
 ||
""")

        self.player_x = 2
        self.player_y = 10

        self.wall = (42, 10, 8, 5)

    def initialize(self):
        print("SmallBlock Game Demo")
        time.sleep(1)

    def update(self, dt):

        key = self.keyboard.poll()

        if key == "a":
            self.player_x -= 1

        elif key == "d":
            self.player_x += 1

        elif key == "w":
            self.player_y -= 1

        elif key == "s":
            self.player_y += 1

        elif key == "q":
            self.enabled = False
            return

        self.camera.x = max(0, self.player_x - 20)
        self.camera.y = max(0, self.player_y - 10)

        hit = rects_overlap(
            (
                self.player_x,
                self.player_y,
                self.player.width,
                self.player.height,
            ),
            self.wall,
        )

        self.renderer.clear()

        self.renderer.text(1, 1, "SmallBlock v1 Demo")
        self.renderer.text(
            1,
            2,
            "WASD Move   Q Quit"
        )

        self.renderer.text(
            1,
            3,
            f"Collision: {'YES' if hit else 'NO'}"
        )

        sx, sy = self.camera.world_to_screen(
            self.player_x,
            self.player_y,
        )

        self.renderer.sprite(
            self.player,
            sx,
            sy,
        )

        wx, wy = self.camera.world_to_screen(
            self.wall[0],
            self.wall[1],
        )

        self.renderer.rect(
            wx,
            wy,
            self.wall[2],
            self.wall[3],
            "X",
        )

        self.renderer.present()

        time.sleep(1 / 30)

    def shutdown(self):
        print("SmallBlock demo shutdown.")


runtime = RuntimeManager()

demo = GameDemo()

runtime.add(demo)

demo.initialize()

while demo.enabled:
    demo.update(1 / 30)

demo.shutdown()
