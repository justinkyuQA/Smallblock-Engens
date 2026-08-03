"""
SmallBlock UI Tests
"""

from smallblock.ui import UIFactory


def test_factory_creates_window():
    window = UIFactory.window("Test")

    assert window is not None


def test_factory_creates_button():
    button = UIFactory.button("OK")

    assert button.text == "OK"


def test_factory_creates_label():
    label = UIFactory.label("Hello")

    assert label.text == "Hello"


def test_factory_creates_panel():
    panel = UIFactory.panel()

    assert panel is not None
