from .clock import Clock
from .events import EventBus
from .logger import Logger

class Engine:

    def __init__(self,name="SmallBlock"):
        self.name=name
        self.clock=Clock()
        self.events=EventBus()
        self.log=Logger()
        self.running=False

    def initialize(self):
        self.log.info(f"{self.name} initialized")

    def update(self,dt):
        pass

    def shutdown(self):
        self.log.info(f"{self.name} shutdown")

    def run(self,frames=10):
        self.running=True
        self.initialize()

        for frame in range(frames):
            dt=self.clock.tick()
            self.update(dt)
            self.events.emit("frame",frame)

        self.shutdown()
