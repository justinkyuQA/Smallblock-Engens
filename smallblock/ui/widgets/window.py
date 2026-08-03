from .panel import Panel


class Window(Panel):
    """Top-level UI window."""

    def __init__(
        self,
        title="Window",
        x=0,
        y=0,
        width=320,
        height=240,
    ):
        super().__init__(x, y, width, height, title)
        self.open = True

    def close(self):
        self.open = False
        self.hide()

    def show(self):
        self.open = True
        self.visible = True

    def draw(self, renderer):
        if not self.open or not self.visible:
            return

        if hasattr(renderer, "rect"):
            renderer.rect(self.x, self.y, self.width, self.height)

        if self.title and hasattr(renderer, "text"):
            renderer.text(self.x + 2, self.y + 1, self.title)

        super().draw(renderer)
