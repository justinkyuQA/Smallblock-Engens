from .widgets.window import Window


class UIManager:
    """Manages all UI windows."""

    def __init__(self):
        self.windows = []

    def add(self, window):
        if isinstance(window, Window):
            self.windows.append(window)
        return window

    def remove(self, window):
        if window in self.windows:
            self.windows.remove(window)

    def clear(self):
        self.windows.clear()

    def update(self, dt):
        for window in self.windows:
            if window.open:
                window.update(dt)

    def draw(self, renderer):
        for window in self.windows:
            if window.open:
                window.draw(renderer)
