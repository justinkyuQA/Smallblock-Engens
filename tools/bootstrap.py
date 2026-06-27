from pathlib import Path

ENGINES = [
    ("core","Engine lifecycle"),
    ("math","Math library"),
    ("graphics","Rendering engine"),
    ("audio","Audio engine"),
    ("assets","Asset manager"),
    ("input","Input manager"),
    ("ecs","Entity Component System"),
    ("scene","Scene manager"),
    ("physics","Physics engine"),
    ("animation","Animation engine"),
    ("ui","User interface"),
    ("speech","Speech engine"),
    ("network","Networking engine"),
    ("random","Random engine"),
    ("chaos","Chaos engine"),
    ("runtime","Runtime"),
    ("plugins","Plugin manager"),
    ("registry","Engine registry")
]

ROOT = Path("smallblock")

for name, desc in ENGINES:

    folder = ROOT / name
    folder.mkdir(parents=True, exist_ok=True)

    init = folder / "__init__.py"

    if not init.exists():

        class_name = "".join(part.capitalize() for part in name.split("_")) + "Manager"

        init.write_text(f'''"""
{desc}
"""

from dataclasses import dataclass

@dataclass
class EngineInfo:
    name:str
    version:str
    author:str
    description:str

ENGINE_INFO = EngineInfo(
    "{name.title()}",
    "0.1",
    "Justin Kyu",
    "{desc}"
)

class {class_name}:

    def initialize(self):
        pass

    def update(self,dt):
        pass

    def shutdown(self):
        pass
''')

    (folder / "README.md").touch(exist_ok=True)

    tests = folder / "tests"
    tests.mkdir(exist_ok=True)

    (tests / "__init__.py").touch(exist_ok=True)

print("Bootstrap complete.")
