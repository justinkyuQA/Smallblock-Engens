class RuntimeManager:

    def __init__(self):
        self.engines = []
        self.running = False

    def add(self, engine):
        self.engines.append(engine)

    def initialize(self):
        for engine in self.engines:
            if hasattr(engine, "initialize"):
                engine.initialize()

    def update(self, dt):
        for engine in self.engines:
            if getattr(engine, "enabled", True):
                if hasattr(engine, "update"):
                    engine.update(dt)

    def shutdown(self):
        for engine in reversed(self.engines):
            if hasattr(engine, "shutdown"):
                engine.shutdown()

    def run(self, frames=10, dt=1/60):
        self.running = True

        self.initialize()

        for _ in range(frames):
            self.update(dt)

        self.shutdown()

        self.running = False
