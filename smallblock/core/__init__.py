from dataclasses import dataclass

@dataclass
class EngineInfo:
    name:str
    version:str
    author:str
    description:str

ENGINE_INFO=EngineInfo(
    "Core",
    "0.1",
    "Justin Kyu",
    "Engine lifecycle"
)

from .engine import Engine
