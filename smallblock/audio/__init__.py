from dataclasses import dataclass

@dataclass
class EngineInfo:
    name:str
    version:str
    author:str
    description:str

ENGINE_INFO=EngineInfo(
    "Audio",
    "0.1",
    "Justin Kyu",
    "Audio engine"
)

from .oscillator import *
from .mixer import *
from .envelope import *
from .export import *
