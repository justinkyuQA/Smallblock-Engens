from smallblock.scene import Scene, SceneManager

class Menu(Scene):

    def initialize(self):
        print("Menu initialized")

    def update(self, dt):
        print(f"Menu update ({dt:.3f})")

    def render(self):
        print("Menu render")

    def shutdown(self):
        print("Menu shutdown")


class Editor(Scene):

    def initialize(self):
        print("Editor initialized")

    def update(self, dt):
        print(f"Editor update ({dt:.3f})")

    def render(self):
        print("Editor render")

    def shutdown(self):
        print("Editor shutdown")


manager = SceneManager()

manager.change(Menu())
manager.update(0.016)
manager.render()

print("-----")

manager.change(Editor())
manager.update(0.016)
manager.render()

manager.shutdown()
