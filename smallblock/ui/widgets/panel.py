from .widget import Widget


class Panel(Widget):
    """Container widget."""

    def __init__(
        self,
        x=0,
        y=0,
        width=100,
        height=100,
        title="",
    ):
        super().__init__(x, y, width, height)
        self.title = title

    def draw(self, renderer):
        if not self.visible:
            return

        if hasattr(renderer, "rect"):
            renderer.rect(self.x, self.y, self.width, self.height)

        if self.title and hasattr(renderer, "text"):
            renderer.text(self.x + 1, self.y + 1, self.title)

        super().draw(renderer)
