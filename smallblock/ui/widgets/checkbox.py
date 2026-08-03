"""
SmallBlock Checkbox Widget
"""

from .widget import Widget


class CheckBox(Widget):
    """Simple checkbox widget."""

    def __init__(self, text="", checked=False, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.checked = checked

    def toggle(self):
        self.checked = not self.checked

    def draw(self, renderer):
        mark = "X" if self.checked else " "
        renderer.text(self.x, self.y, f"[{mark}] {self.text}")

    def update(self, dt):
        pass
