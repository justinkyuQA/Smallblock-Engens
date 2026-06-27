def status():
    from smallblock.registry import EngineRegistry

    r = EngineRegistry()
    r.discover()
    engines = r.list()

    print()
    print("SmallBlock Engine Status")
    print("========================")
    print()

    for e in engines:
        print(f"[OK] {e.name:12} {e.version:6} {e.description}")

    print()
    print(f"Total Registered Engines: {len(engines)}")
