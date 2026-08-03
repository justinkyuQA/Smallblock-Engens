"""
SmallBlock TreeView Widget
"""

from .widget import Widget


class TreeNode:
    """Simple tree node."""

    def __init__(self, text):
        self.text = text
        self.children = []

    def add(self, node):
        self.children.append(node)
        return node


class TreeView(Widget):
    """Simple tree widget."""

    def __init__(self, root=None, **kwargs):
        super().__init__(**kwargs)
        self.root = root

    def draw(self, renderer):
        if self.root is None:
            return

        self._draw_node(renderer, self.root, self.x, self.y, 0)

    def _draw_node(self, renderer, node, x, y, depth):
        renderer.text(x + depth * 2, y, node.text)

        for index, child in enumerate(node.children):
            self._draw_node(renderer, child, x, y + index + 1, depth + 1)

    def update(self, dt):
        pass
