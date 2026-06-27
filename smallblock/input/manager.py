class Input:

    def __init__(self):
        self.keys = {}
        self.mouse = {"x":0,"y":0}
        self.buttons = {}

    def press(self,key):
        self.keys[key] = True

    def release(self,key):
        self.keys[key] = False

    def down(self,key):
        return self.keys.get(key,False)

    def move_mouse(self,x,y):
        self.mouse["x"] = x
        self.mouse["y"] = y

    def click(self,button):
        self.buttons[button] = True

    def unclick(self,button):
        self.buttons[button] = False

    def button_down(self,button):
        return self.buttons.get(button,False)
