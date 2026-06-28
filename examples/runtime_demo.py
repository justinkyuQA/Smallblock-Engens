from smallblock.runtime import RuntimeManager

class DemoEngine:

    def __init__(self):
        self.enabled = True

    def initialize(self):
        print("Engine initialized")

    def update(self, dt):
        print(f"Engine update ({dt:.3f})")

    def shutdown(self):
        print("Engine shutdown")

runtime = RuntimeManager()

runtime.add(DemoEngine())

runtime.run(frames=5)
