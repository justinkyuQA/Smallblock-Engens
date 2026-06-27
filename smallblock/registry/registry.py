from dataclasses import dataclass
from pathlib import Path
import importlib

@dataclass(frozen=True)
class EngineInfo:
    name: str
    version: str
    author: str
    description: str

class EngineRegistry:

    def __init__(self):
        self.engines = []

    def discover(self):
        self.engines = []
        root = Path("smallblock")

        for folder in root.iterdir():
            if not folder.is_dir():
                continue

            module_name = f"smallblock.{folder.name}.info"

            try:
                module = importlib.import_module(module_name)
                if hasattr(module, "ENGINE_INFO"):
                    self.engines.append(module.ENGINE_INFO)
            except Exception:
                continue

    def list(self):
        return sorted(self.engines, key=lambda e: e.name)
