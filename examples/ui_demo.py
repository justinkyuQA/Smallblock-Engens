"""
SmallBlock UI Example
"""

from smallblock.ui.demo import build_demo


def main():
    ui = build_demo()

    print("SmallBlock UI Demo")
    print("==================")
    print(f"Windows: {len(ui.windows)}")

    window = ui.windows[0]

    print(f"Title: {window.title}")
    print(f"Children: {len(window.children)}")

    for child in window.children:
        print(f" - {child.__class__.__name__}")


if __name__ == "__main__":
    main()
