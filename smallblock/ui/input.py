"""
SmallBlock UI Input Router
"""


class InputRouter:
    """Routes keyboard and mouse input to the UI."""

    def __init__(self):
        self.focus_manager = None
        self.capture = None

    def set_focus_manager(self, focus_manager):
        self.focus_manager = focus_manager

    def capture_input(self, widget):
        self.capture = widget

    def release_input(self):
        self.capture = None

    def dispatch(self, event):
        if self.capture is not None:
            self.capture.handle_event(event)
            return

        if self.focus_manager is None:
            return

        widget = self.focus_manager.focused

        if widget is not None:
            widget.handle_event(event)
