"""
SmallBlock UI Layout
"""


class Layout:
    """Base layout manager."""

    def apply(self, parent):
        raise NotImplementedError


class VerticalLayout(Layout):
    """Stack widgets vertically."""

    def apply(self, parent):
        y = 0

        for widget in parent.children:
            widget.x = 0
            widget.y = y
            y += widget.height


class HorizontalLayout(Layout):
    """Arrange widgets horizontally."""

    def apply(self, parent):
        x = 0

        for widget in parent.children:
            widget.x = x
            widget.y = 0
            x += widget.width
