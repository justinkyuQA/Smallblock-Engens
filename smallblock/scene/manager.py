from .scene import Scene

class SceneManager:

    def __init__(self):
        self.current = None

    def change(self, scene):
        if self.current:
            self.current.shutdown()

        self.current = scene
        self.current.initialize()

    def update(self, dt):
        if self.current:
            self.current.update(dt)

    def render(self):
        if self.current:
            self.current.render()

    def shutdown(self):
        if self.current:
            self.current.shutdown()
