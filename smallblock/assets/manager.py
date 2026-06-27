from pathlib import Path
import json

class AssetManager:

    def __init__(self, root="assets"):
        self.root = Path(root)
        self.cache = {}

    def path(self, *parts):
        return self.root.joinpath(*parts)

    def exists(self, *parts):
        return self.path(*parts).exists()

    def text(self, *parts):
        p = self.path(*parts)

        if str(p) not in self.cache:
            self.cache[str(p)] = p.read_text()

        return self.cache[str(p)]

    def json(self, *parts):
        p = self.path(*parts)

        if str(p) not in self.cache:
            self.cache[str(p)] = json.loads(p.read_text())

        return self.cache[str(p)]

    def clear(self):
        self.cache.clear()
