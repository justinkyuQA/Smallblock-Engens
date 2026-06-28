from dataclasses import dataclass


@dataclass
class Body:
    x: float = 0.0
    y: float = 0.0

    vx: float = 0.0
    vy: float = 0.0

    ax: float = 0.0
    ay: float = 0.0

    width: float = 1.0
    height: float = 1.0

    mass: float = 1.0
    friction: float = 0.98
    gravity: float = 0.0

    def update(self, dt: float):
        self.vx += self.ax * dt
        self.vy += (self.ay + self.gravity) * dt

        self.x += self.vx * dt
        self.y += self.vy * dt

        self.vx *= self.friction
        self.vy *= self.friction
