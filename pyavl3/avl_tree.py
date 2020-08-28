from typing import Hashable, Tuple, Iterator

from .avl_node import AVLNode
from .interface import ADTInterface
from .traversal import InOrderTraversal


class AVLTree(ADTInterface):

    traversal = InOrderTraversal

    def __init__(self) -> None:
        self._root = None
        self._n = 0

    def __getitem__(self, key: Hashable) -> any:
        node = self._get(self._root, key)
        if node is None:
            raise KeyError(key)
        return node.value

    def __setitem__(self, key: Hashable, value: any) -> None:
        node = AVLNode(key, value)
        self._root = self._insert(self._root, node)

    def __delitem__(self, key: Hashable) -> None:
        pass

    def __len__(self) -> int:
        return self._n

    def __contains__(self, key: Hashable) -> bool:
        return self._get(self._root, key) is not None

    def __iter__(self) -> Iterator[Tuple[Hashable, any]]:
        return AVLTree.traversal(self._root)

    def get(self, key: Hashable, default: any = None) -> any:
        node = self._get(self._root, key)
        if node is None:
            return default
        return node.value

    def _get(self, root: AVLNode, key: Hashable) -> AVLNode:
        if root is None:
            return None
        elif key < root.key:
            return self._get(root.left, key)
        elif key > root.key:
            return self._get(root.right, key)
        elif key == root.key:
            return root

    def _insert(self, root: AVLNode, node: AVLNode) -> AVLNode:
        if root is None:
            self._n += 1
            return node
        elif node.key < root.key:
            root.left = self._insert(root.left, node)
        elif node.key > root.key:
            root.right = self._insert(root.right, node)
        elif node.key == root.key:
            root.value = node.value

        root.height = max(self._height(root.left), self._height(root.right)) + 1
        balance = self._height(root.left) - self._height(root.right)

        if balance > 1: # left heavy
            if self._height(root.left.left) - self._height(root.left.right) < 0:
                root.left = self._rotate_left(root.left)
            return self._rotate_right(root)
        elif balance < -1: # Right heavy
            if self._height(root.right.left) - self._height(root.right.right) > 0:
                root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def _height(self, root: AVLNode) -> int:
        if root is None:
            return -1
        return root.height

    def _rotate_right(self, x: AVLNode) -> AVLNode:
        """Rotate a subtree around x.left

            x          y
           / \        / \
          y  T3 -->  T1  x
         / \            / \
        T1 T2          T2 T3
        """
        y = x.left
        t2 = y.right
        y.right = x
        x.left = t2

        x.height = max(self._height(x.left), self._height(x.right)) + 1
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        return y

    def _rotate_left(self, y: AVLNode) -> AVLNode:
        """Rotate a subtree around y.right

            x          y
           / \        / \
          y  T3 <--  T1  x
         / \            / \
        T1 T2          T2 T3
        """
        x = y.right
        t2 = x.left
        x.left = y
        y.right = t2

        y.height = max(self._height(y.left), self._height(y.right)) + 1
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        return x
