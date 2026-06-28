class Camera:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def world_to_screen(self, x, y):
        return int(x - self.x), int(y - self.y)

    def move(self, dx, dy):
        self.x += dx
        self
