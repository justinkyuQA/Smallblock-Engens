"""
SmallBlock Base Widget
"""


class Widget:
    """Base class for all UI widgets."""

    def __init__(
        self,
        x=0,
        y=0,
        width=100,
        height=30,
        visible=True,
        enabled=True,
    ):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.visible = visible
        self.enabled = enabled

        self.parent = None
        self.children = []

    def add(self, widget):
        widget.parent = self
        self.children.append(widget)
        return widget

    def remove(self, widget):
        if widget in self.children:
            self.children.remove(widget)
            widget.parent = None

    def draw(self, renderer):
        pass

    def update(self, dt):
        pass
