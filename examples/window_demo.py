import math

from smallblock.graphics.window import Window


t = 0


def draw(win):
    global t

    t += 0.05

    cx = 320 + math.cos(t) * 120
    cy = 240 + math.sin(t) * 80

    win.line(0, 0, 640, 480, "red")
    win.line(640, 0, 0, 480, "green")

    win.rect(40, 40, 140, 80, "yellow")
    win.fill_rect(240, 60, 120, 120, "blue")

    win.circle(cx, cy, 50, "magenta")

    win.text(
        20,
        430,
        "SmallBlock Graphics Engine v1.0 - Double Buffered Window",
        "white"
    )


win = Window(640, 480, "SmallBlock Graphics v1.0")
win.run(draw, fps=60)
