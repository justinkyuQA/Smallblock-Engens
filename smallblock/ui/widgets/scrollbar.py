"""
SmallBlock ScrollBar Widget
"""

from .widget import Widget


class ScrollBar(Widget):
    """Simple vertical scrollbar."""

    def __init__(self, minimum=0, maximum=100, value=0, **kwargs):
        super().__init__(**kwargs)
        self.minimum = minimum
        self.maximum = maximum
        self.value = value

    def set(self, value):
        self.value = max(self.minimum, min(value, self.maximum))

    @property
    def percent(self):
        if self.maximum <= self.minimum:
            return 0.0
        return (self.value - self.minimum) / (self.maximum - self.minimum)

    def draw(self, renderer):
        height = max(1, self.height)
        position = int(self.percent * (height - 1))

        for y in range(height):
            char = "#" if y == position else "|"
            renderer.text(self.x, self.y + y, char)

    def update(self, dt):
        pass
