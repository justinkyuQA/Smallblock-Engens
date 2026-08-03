from .panel import Panel


class Toolbar(Panel):
    """Horizontal toolbar container."""

    def __init__(
        self,
        x=0,
        y=0,
        width=100,
        height=3,
        title="",
    ):
        super().__init__(x, y, width, height, title)
        self.items = []

    def add_item(self, widget):
        self.items.append(widget)
        self.add(widget)
        return widget

    def clear(self):
        self.items.clear()
        self.children.clear()

    def draw(self, renderer):
        if not self.visible:
            return

        if hasattr(renderer, "rect"):
            renderer.rect(self.x, self.y, self.width, self.height)

        super().draw(renderer)
