class Renderer:
    def __init__(self, width=64, height=24, fill=" "):
        self.width = width
        self.height = height
        self.fill = fill
        self.front = []
        self.back = []
        self.clear()

    def clear(self):
        self.back = [[self.fill for _ in range(self.width)] for _ in range(self.height)]

    def pixel(self, x, y, char="#"):
        x, y = int(x), int(y)
        if 0 <= x < self.width and 0 <= y < self.height:
            self.back[y][x] = char[0]

    def rect(self, x, y, w, h, char="#"):
        for yy in range(int(y), int(y + h)):
            for xx in range(int(x), int(x + w)):
                self.pixel(xx, yy, char)

    def text(self, x, y, text):
        for i, ch in enumerate(str(text)):
            self.pixel(x + i, y, ch)

    def sprite(self, sprite, x, y):
        for yy, row in enumerate(sprite.pixels):
            for xx, ch in enumerate(row):
                if ch != " ":
                    self.pixel(x + xx, y + yy, ch)

    def present(self):
        self.front = [row[:] for row in self.back]
        print("\033[H\033[J", end="")
        print("\n".join("".join(row) for row in self.front))
