"""
SmallBlock UI Demo
"""

from smallblock.ui import (
    UIManager,
    Window,
    Panel,
    Label,
    Button,
    TextBox,
    Toolbar,
    StatusBar,
)


def build_demo():
    ui = UIManager()

    window = Window(
        title="SmallBlock UI Demo",
        width=640,
        height=480,
    )

    toolbar = Toolbar(width=640)
    panel = Panel(
        x=10,
        y=40,
        width=620,
        height=380,
        title="Workspace",
    )

    label = Label(
        "Hello SmallBlock!",
        x=20,
        y=20,
    )

    textbox = TextBox(
        "Type here...",
        x=20,
        y=60,
        width=200,
    )

    button = Button(
        "OK",
        x=20,
        y=110,
    )

    status = StatusBar(
        y=460,
        width=640,
        text="Ready",
    )

    panel.add(label)
    panel.add(textbox)
    panel.add(button)

    window.add(toolbar)
    window.add(panel)
    window.add(status)

    ui.add(window)

    return ui


if __name__ == "__main__":
    ui = build_demo()
    print(f"UI initialized with {len(ui.windows)} window(s).")
