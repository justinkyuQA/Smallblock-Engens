from smallblock.registry import EngineRegistry

r = EngineRegistry()
r.discover()

print("Discovered Engines")
print("------------------")

for e in r.list():
    print(f"{e.name:12} {e.version:6} {e.description}")
