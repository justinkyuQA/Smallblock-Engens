"""
SmallBlock DockPanel Widget
"""

from .container import Container


class DockPanel(Container):
    """Container with simple docking support."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.docks = {
            "top": [],
            "bottom": [],
            "left": [],
            "right": [],
            "center": [],
        }

    def dock(self, widget, position="center"):
        if position not in self.docks:
            raise ValueError(f"Unknown dock position: {position}")

        self.add(widget)
        self.docks[position].append(widget)

    def draw(self, renderer):
        for widgets in self.docks.values():
            for widget in widgets:
                widget.draw(renderer)
