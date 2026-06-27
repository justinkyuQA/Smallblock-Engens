class Canvas:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [
            [(0,0,0) for x in range(width)]
            for y in range(height)
        ]

    def clear(self, color=(0,0,0)):
        for y in range(self.height):
            for x in range(self.width):
                self.pixels[y][x] = color

    def set_pixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = color

    def save(self, filename):
        with open(filename,"w") as f:
            f.write("P3\n")
            f.write(f"{self.width} {self.height}\n")
            f.write("255\n")

            for row in self.pixels:
                for r,g,b in row:
                    f.write(f"{r} {g} {b} ")
                f.write("\n")
