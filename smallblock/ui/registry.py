"""
SmallBlock UI Registry
"""

class UIRegistry:
    """Registry for UI widget classes."""

    def __init__(self):
        self._widgets = {}

    def register(self, name, widget_class):
        self._widgets[name] = widget_class

    def unregister(self, name):
        self._widgets.pop(name, None)

    def get(self, name):
        return self._widgets.get(name)

    def create(self, name, *args, **kwargs):
        widget = self.get(name)

        if widget is None:
            raise KeyError(f"Unknown widget: {name}")

        return widget(*args, **kwargs)

    def names(self):
        return sorted(self._widgets.keys())

    def clear(self):
        self._widgets.clear()
