"""
SmallBlock Radio Button Widget
"""

from .widget import Widget


class RadioButton(Widget):
    """Simple radio button."""

    def __init__(self, text="", selected=False, group=None, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.selected = selected
        self.group = group

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

    def draw(self, renderer):
        mark = "*" if self.selected else " "
        renderer.text(self.x, self.y, f"({mark}) {self.text}")

    def update(self, dt):
        pass
