class Sprite:
    def __init__(self, pixels):
        if isinstance(pixels, str):
            pixels = pixels.strip("\n").splitlines()
        self.pixels = [list(row) for row in pixels]
        self.height = len(self.pixels)
        self.width = max((len(row) for row in self.pixels), default=0)
