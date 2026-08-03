"""
SmallBlock Focus Manager
"""


class FocusManager:
    """Tracks keyboard focus for UI widgets."""

    def __init__(self):
        self._focused = None

    @property
    def focused(self):
        return self._focused

    def set_focus(self, widget):
        if self._focused is widget:
            return

        if self._focused is not None:
            self._focused.handle_event(
                {"type": "focus_lost"}
            )

        self._focused = widget

        if widget is not None:
            widget.handle_event(
                {"type": "focus_gained"}
            )

    def clear(self):
        self.set_focus(None)

    def has_focus(self, widget):
        return self._focused is widget
