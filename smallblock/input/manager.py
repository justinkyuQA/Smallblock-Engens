class Input:

    def __init__(self):
        self.keys = {}
        self.previous = {}

        self.mouse = {"x": 0, "y": 0}
        self.buttons = {}
        self.actions = {}

    def bind(self, action, *keys):
        self.actions[action] = set(keys)

    def press(self, key):
        self.keys[key] = True

    def release(self, key):
        self.keys[key] = False

    def down(self, key):
        return self.keys.get(key, False)

    def pressed(self, key):
        return self.down(key) and not self.previous.get(key, False)

    def released(self, key):
        return (not self.down(key)) and self.previous.get(key, False)

    def action(self, name):
        return any(self.down(k) for k in self.actions.get(name, []))

    def move_mouse(self, x, y):
        self.mouse["x"] = x
        self.mouse["y"] = y

    def click(self, button):
        self.buttons[button] = True

    def unclick(self, button):
        self.buttons[button] = False

    def button_down(self, button):
        return self.buttons.get(button, False)

    def next_frame(self):
        self.previous = self.keys.copy()
