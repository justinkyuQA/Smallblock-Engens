"""
SmallBlock TabView Widget
"""

from .container import Container


class TabView(Container):
    """Simple tab container."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tabs = []
        self.active = 0

    def add_tab(self, title, widget):
        self.tabs.append((title, widget))
        self.add(widget)
        return widget

    def select(self, index):
        if 0 <= index < len(self.tabs):
            self.active = index

    def draw(self, renderer):
        x = self.x

        for index, (title, _) in enumerate(self.tabs):
            marker = "*" if index == self.active else "-"
            renderer.text(x, self.y, f"{marker}{title}")
            x += len(title) + 3

        if self.tabs:
            _, widget = self.tabs[self.active]
            widget.draw(renderer)
