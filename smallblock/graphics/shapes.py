from .primitives import line

def circle(canvas, cx, cy, radius, color):
    x = radius
    y = 0
    err = 1 - radius

    while x >= y:
        canvas.set_pixel(cx + x, cy + y, color)
        canvas.set_pixel(cx + y, cy + x, color)
        canvas.set_pixel(cx - y, cy + x, color)
        canvas.set_pixel(cx - x, cy + y, color)
        canvas.set_pixel(cx - x, cy - y, color)
        canvas.set_pixel(cx - y, cy - x, color)
        canvas.set_pixel(cx + y, cy - x, color)
        canvas.set_pixel(cx + x, cy - y, color)

        y += 1

        if err < 0:
            err += 2 * y + 1
        else:
            x -= 1
            err += 2 * (y - x) + 1

def triangle(canvas, x1, y1, x2, y2, x3, y3, color):
    line(canvas, x1, y1, x2, y2, color)
    line(canvas, x2, y2, x3, y3, color)
    line(canvas, x3, y3, x1, y1, color)
