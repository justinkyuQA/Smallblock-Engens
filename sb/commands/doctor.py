from pathlib import Path

EXPECTED = [
    "core",
    "math",
    "graphics",
    "audio",
    "assets",
    "input",
    "ecs",
    "scene",
    "physics",
    "animation",
    "ui",
    "speech",
    "network",
    "random",
    "chaos",
    "runtime",
    "plugins",
    "registry",
]

def doctor():
    print()
    print("SmallBlock Doctor")
    print("=================")
    print()

    problems = 0

    for name in EXPECTED:
        folder = Path("smallblock") / name
        init = folder / "__init__.py"

        if not folder.exists():
            print(f"[MISS] {name:12} folder missing")
            problems += 1
        elif not init.exists():
            print(f"[WARN] {name:12} __init__.py missing")
            problems += 1
        else:
            print(f"[ OK ] {name:12}")

    print()

    if problems == 0:
        print("Health: OK")
    else:
        print(f"Health: {problems} issue(s) found")
