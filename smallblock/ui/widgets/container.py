"""
SmallBlock UI Container
"""

from .widget import Widget


class Container(Widget):
    """Widget capable of holding child widgets."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def draw(self, renderer):
        if not self.visible:
            return

        for child in self.children:
            child.draw(renderer)

    def update(self, dt):
        if not self.enabled:
            return

        for child in self.children:
            child.update(dt)
