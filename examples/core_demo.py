from smallblock.core import Engine

class Demo(Engine):

    def initialize(self):
        super().initialize()

        self.events.subscribe(
            "frame",
            lambda frame: self.log.info(f"Frame {frame}")
        )

    def update(self,dt):
        self.log.info(f"dt={dt:.6f}")

Demo().run()
