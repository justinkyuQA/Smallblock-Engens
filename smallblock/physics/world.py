class PhysicsWorld:

    def __init__(self):
        self.bodies = []

    def add(self, body):
        self.bodies.append(body)

    def update(self, dt):
        for body in self.bodies:
            body.update(dt)
