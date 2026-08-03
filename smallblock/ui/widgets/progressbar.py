"""
SmallBlock Progress Bar Widget
"""

from .widget import Widget


class ProgressBar(Widget):
    """Simple progress bar."""

    def __init__(self, value=0.0, maximum=100.0, **kwargs):
        super().__init__(**kwargs)
        self.value = value
        self.maximum = maximum

    def set(self, value):
        self.value = max(0.0, min(value, self.maximum))

    @property
    def percent(self):
        if self.maximum <= 0:
            return 0.0
        return self.value / self.maximum

    def draw(self, renderer):
        width = max(1, self.width)
        filled = int(width * self.percent)
        bar = "#" * filled + "-" * (width - filled)
        renderer.text(self.x, self.y, f"[{bar}]")

    def update(self, dt):
        pass
