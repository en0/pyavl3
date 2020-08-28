from typing import Hashable


class AVLNode:
    def __init__(self, key: Hashable, value: any = None) -> None:
        self.key = key
        self.value = value
        self.left: "AVLNode" = None
        self.right: "AVLNode" = None
        self.height = 0

    def __repr__(self):
        return f"<Node key={self.key}, value={self.value}, height={self.height}>"
