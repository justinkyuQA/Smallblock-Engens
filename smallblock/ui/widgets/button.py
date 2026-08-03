from .widget import Widget


class Button(Widget):
    """Clickable button."""

    def __init__(
        self,
        text="Button",
        x=0,
        y=0,
        width=None,
        height=3,
        callback=None,
    ):
        if width is None:
            width = len(text) + 4

        super().__init__(x, y, width, height)

        self.text = text
        self.callback = callback
        self.pressed = False

    def click(self):
        if callable(self.callback):
            self.callback()

    def draw(self, renderer):
        if not self.visible:
            return

        if hasattr(renderer, "rect"):
            renderer.rect(self.x, self.y, self.width, self.height)

        if hasattr(renderer, "text"):
            renderer.text(self.x + 2, self.y + 1, self.text)

        super().draw(renderer)
