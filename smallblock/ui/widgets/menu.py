"""
SmallBlock Menu Widget
"""

from .widget import Widget


class Menu(Widget):
    """Simple menu widget."""

    def __init__(self, title="Menu", items=None, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.items = list(items or [])
        self.selected = 0

    def add(self, text):
        self.items.append(text)

    def remove(self, text):
        if text in self.items:
            self.items.remove(text)

    def draw(self, renderer):
        renderer.text(self.x, self.y, self.title)

        for index, item in enumerate(self.items):
            marker = ">" if index == self.selected else " "
            renderer.text(self.x, self.y + index + 1, f"{marker} {item}")

    def update(self, dt):
        pass
