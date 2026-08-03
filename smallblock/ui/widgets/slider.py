"""
SmallBlock Slider Widget
"""

from .widget import Widget


class Slider(Widget):
    """Simple horizontal slider."""

    def __init__(self, value=0.0, minimum=0.0, maximum=100.0, **kwargs):
        super().__init__(**kwargs)
        self.minimum = minimum
        self.maximum = maximum
        self.value = value

    def set(self, value):
        self.value = max(self.minimum, min(value, self.maximum))

    @property
    def percent(self):
        if self.maximum == self.minimum:
            return 0.0
        return (self.value - self.minimum) / (self.maximum - self.minimum)

    def draw(self, renderer):
        width = max(1, self.width)
        position = int(self.percent * (width - 1))

        bar = ["-"] * width
        bar[position] = "|"

        renderer.text(self.x, self.y, "[" + "".join(bar) + "]")

    def update(self, dt):
        pass
