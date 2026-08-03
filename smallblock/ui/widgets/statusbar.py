from .panel import Panel


class StatusBar(Panel):
    """Displays application status information."""

    def __init__(
        self,
        x=0,
        y=0,
        width=100,
        height=1,
        text="Ready",
    ):
        super().__init__(x, y, width, height)
        self.text = text

    def set_status(self, text):
        self.text = str(text)

    def clear(self):
        self.text = ""

    def draw(self, renderer):
        if not self.visible:
            return

        if hasattr(renderer, "rect"):
            renderer.rect(self.x, self.y, self.width, self.height)

        if hasattr(renderer, "text"):
            renderer.text(self.x + 1, self.y, self.text)

        super().draw(renderer)
