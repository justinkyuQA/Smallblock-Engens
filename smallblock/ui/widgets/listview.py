"""
SmallBlock ListView Widget
"""

from .widget import Widget


class ListView(Widget):
    """Simple vertical list widget."""

    def __init__(self, items=None, selected=0, **kwargs):
        super().__init__(**kwargs)
        self.items = list(items or [])
        self.selected = selected

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def clear(self):
        self.items.clear()
        self.selected = 0

    def draw(self, renderer):
        for index, item in enumerate(self.items):
            prefix = ">" if index == self.selected else " "
            renderer.text(self.x, self.y + index, f"{prefix} {item}")

    def update(self, dt):
        pass
