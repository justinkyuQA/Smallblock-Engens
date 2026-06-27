from dataclasses import dataclass

@dataclass(frozen=True)
class EngineInfo:
    name: str
    version: str
    author: str
    description: str

ENGINE_INFO = EngineInfo(
    name="Filesystem",
    version="0.1",
    author="Justin Kyu",
    description="Filesystem engine"
)
