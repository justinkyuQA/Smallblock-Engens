"""
SmallBlock UI Events
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class UIEvent:
    """Base UI event."""

    type: str
    source: Any = None


@dataclass
class MouseEvent(UIEvent):
    x: int = 0
    y: int = 0
    button: int = 0


@dataclass
class KeyEvent(UIEvent):
    key: str = ""
    pressed: bool = True


@dataclass
class FocusEvent(UIEvent):
    focused: bool = True


@dataclass
class TextEvent(UIEvent):
    text: str = ""


@dataclass
class ResizeEvent(UIEvent):
    width: int = 0
    height: int = 0
