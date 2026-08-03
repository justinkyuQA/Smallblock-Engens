from .widget import Widget


class Label(Widget):
    """Simple text label."""

    def __init__(
        self,
        text="",
        x=0,
        y=0,
    ):
        super().__init__(x, y, len(text), 1)
        self.text = text

    def set_text(self, text):
        self.text = str(text)
        self.width = len(self.text)

    def draw(self, renderer):
        if not self.visible:
            return

        if hasattr(renderer, "text"):
            renderer.text(self.x, self.y, self.text)

        super().draw(renderer)
