#!/usr/bin/env python3

from pathlib import Path
import sys

if len(sys.argv) != 3:
    print("Usage:")
    print("python3 tools/new_engine.py <engine> \"Description\"")
    raise SystemExit(1)

name = sys.argv[1]
description = sys.argv[2]

Class = "".join(part.capitalize() for part in name.split("_")) + "Manager"

root = Path("smallblock") / name
(root / "tests").mkdir(parents=True, exist_ok=True)
(root / "examples").mkdir(exist_ok=True)

(root / "__init__.py").write_text(
"""from .manager import *
from .info import ENGINE_INFO
"""
)

(root / "info.py").write_text(f'''from dataclasses import dataclass

@dataclass(frozen=True)
class EngineInfo:
    name: str
    version: str
    author: str
    description: str

ENGINE_INFO = EngineInfo(
    name="{name.title()}",
    version="0.1",
    author="Justin Kyu",
    description="{description}"
)
''')

(root / "manager.py").write_text(f'''class {Class}:

    def initialize(self):
        pass

    def update(self, dt):
        pass

    def shutdown(self):
        pass
''')

(root / "README.md").write_text(f"# {name.title()} Engine\n")

(root / "tests" / "__init__.py").touch()
(root / "examples" / ".gitkeep").touch()

print(f"Created engine: {name}")
