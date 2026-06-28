def rects_overlap(a, b):
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return (
        ax < bx + bw and
        ax + aw > bx and
        ay < by + bh and
        ay + ah > by
    )


def circles_overlap(a, b):
    ax, ay, ar = a
    bx, by, br = b

    dx = ax - bx
    dy = ay - by

    return dx * dx + dy * dy <= (ar + br) ** 2
