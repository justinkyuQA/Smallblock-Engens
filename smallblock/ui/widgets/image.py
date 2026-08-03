"""
SmallBlock Image Widget
"""

from .widget import Widget


class Image(Widget):
    """Displays a sprite or image object."""

    def __init__(self, image=None, **kwargs):
        super().__init__(**kwargs)
        self.image = image

    def set_image(self, image):
        self.image = image

    def draw(self, renderer):
        if self.image is None:
            return

        if hasattr(renderer, "sprite"):
            renderer.sprite(self.image, self.x, self.y)

    def update(self, dt):
        pass
