from .widget import Widget


class TextBox(Widget):
    """Basic editable text box."""

    def __init__(
        self,
        text="",
        x=0,
        y=0,
        width=20,
        height=3,
    ):
        super().__init__(x, y, width, height)
        self.text = text
        self.cursor = len(text)

    def set_text(self, text):
        self.text = str(text)
        self.cursor = len(self.text)

    def append(self, text):
        self.text += str(text)
        self.cursor = len(self.text)

    def clear(self):
        self.text = ""
        self.cursor = 0

    def draw(self, renderer):
        if not self.visible:
            return

        if hasattr(renderer, "rect"):
            renderer.rect(self.x, self.y, self.width, self.height)

        if hasattr(renderer, "text"):
            renderer.text(self.x + 1, self.y + 1, self.text)

        super().draw(renderer)
