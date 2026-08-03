"""
SmallBlock UI Theme
"""

from .style import Style


class Theme:
    """Collection of reusable styles."""

    def __init__(self, name="Default"):
        self.name = name
        self.styles = {}

    def add(self, widget_type, style):
        if not isinstance(style, Style):
            raise TypeError("style must be a Style instance")

        self.styles[widget_type] = style

    def get(self, widget_type):
        return self.styles.get(widget_type, Style())

    def remove(self, widget_type):
        self.styles.pop(widget_type, None)

    def clear(self):
        self.styles.clear()
