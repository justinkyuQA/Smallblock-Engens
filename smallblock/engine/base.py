class Engine:

    def __init__(self, name):
        self.name = name
        self.enabled = True

    def initialize(self):
        pass

    def update(self, dt):
        pass

    def shutdown(self):
        pass

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False
