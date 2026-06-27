def line(canvas, x0, y0, x1, y1, color):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    err = dx - dy

    while True:
        canvas.set_pixel(x0, y0, color)

        if x0 == x1 and y0 == y1:
            break

        e2 = err * 2

        if e2 > -dy:
            err -= dy
            x0 += sx

        if e2 < dx:
            err += dx
            y0 += sy


def rectangle(canvas, x, y, w, h, color):
    line(canvas, x, y, x + w, y, color)
    line(canvas, x, y, x, y + h, color)
    line(canvas, x + w, y, x + w, y + h, color)
    line(canvas, x, y + h, x + w, y + h, color)


def fill_rect(canvas, x, y, w, h, color):
    for yy in range(y, y + h):
        for xx in range(x, x + w):
            canvas.set_pixel(xx, yy, color)
