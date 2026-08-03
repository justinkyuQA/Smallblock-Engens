class Widget:
    def __init__(self, x=0, y=0, width=100, height=30, visible=True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = visible
        self.enabled = True
        self.children = []

    def add(self, widget):
        self.children.append(widget)

    def update(self, dt):
        for child in self.children:
            child.update(dt)

    def draw(self, renderer):
        for child in self.children:
            child.draw(renderer)

    def handle_event(self, event):
        for child in self.children:
            child.handle_event(event)
