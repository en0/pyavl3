from typing import Hashable, Tuple, Iterator

from .avl_node import AVLNode
from .interface import ADTInterface
from .traversal import InOrderTraversal


class AVLTree(ADTInterface):

    # Used for iterator
    traversal = InOrderTraversal

    def __init__(self) -> None:
        self._root = None
        self._n = 0

    def __getitem__(self, key: Hashable) -> any:
        """Get the value at the given key.

        If the key is not found, a KeyError will be raised.
        """
        node = self._get(self._root, key)
        if node is None:
            raise KeyError(key)
        return node.value

    def __setitem__(self, key: Hashable, value: any) -> None:
        """Add or Update the given key using the given value."""
        node = AVLNode(key, value)
        self._root = self._insert(self._root, node)

    def __delitem__(self, key: Hashable) -> None:
        """Remove the given key from the tree."""
        self._root = self._delete(self._root, key)

    def __len__(self) -> int:
        """Return the count of members in the tree."""
        return self._n

    def __contains__(self, key: Hashable) -> bool:
        """Check if a given key exists in the tree"""
        return self._get(self._root, key) is not None

    def __iter__(self) -> Iterator[Tuple[Hashable, any]]:
        """Create and return an iterator"""
        return AVLTree.traversal(self._root)

    def get(self, key: Hashable, default: any = None) -> any:
        """Get the value at the given key or default."""
        node = self._get(self._root, key)
        if node is None:
            return default
        return node.value

    def _get(self, root: AVLNode, key: Hashable) -> AVLNode:
        """Find a key in the given subtree"""

        if root is None:
            # Key is not in subtree
            return None

        elif key < root.key:
            # If key exists, it must be left
            return self._get(root.left, key)

        elif key > root.key:
            # If key exists, it must be right
            return self._get(root.right, key)

        elif key == root.key:
            # Found it.
            return root

    def _delete(self, root: AVLNode, key: Hashable) -> AVLNode:
        """Find and remove the given key from the given subtree."""
        if root is None:
            # This key is not in the given sub-tree
            raise KeyError(key)

        elif key < root.key:
            # If the key exists, it must be left
            root.left = self._delete(root.left, key)

        elif key > root.key:
            # If the key exists, it must be right
            root.right = self._delete(root.right, key)

        elif root.left and root.right:
            # Replace K with the Min(T2)
            #     r         r
            #    / \       / \ 
            #   K  T3 ->  T2 T3
            #  / \       /
            # T1 T2     T1
            # assert(root.key == key)
            new_root = self._pop_right_min(root)
            new_root.left = root.left
            new_root.right = root.right

            # Since we poped a node off, _n is already
            # updated since _delete was used to remove it.
            # Do not update _n here. the number is correct.
            return new_root

        elif root.left:
            # Replace K with T1
            #     r         r
            #    / \       / \ 
            #   K  T3 ->  T1 T3
            #  /
            # T1
            # assert(root.key == key)
            self._n -= 1
            return root.left

        elif root.right:
            # Replace K with T1
            #   r         r
            #  / \       / \ 
            # K  T3 ->  x  T3
            #  \ 
            #  T1
            # assert(root.key == key)
            self._n -= 1
            return root.right

        else:
            # Replace K with NULL
            #   r       r
            #  / \  ->   \ 
            # K  T3      T3
            # assert(root.key == key)
            self._n -= 1
            return None

        # Recompute hight of root
        root.height = self._compute_height(root)

        # return the balanced subtree
        return self._rebalance(root)

    def _insert(self, root: AVLNode, node: AVLNode) -> AVLNode:
        """Insert a node into a subtree"""

        if root is None:
            # Node fits here! Insert it.
            self._n += 1
            return node

        elif node.key < root.key:
            # Node fits left of this root
            root.left = self._insert(root.left, node)

        elif node.key > root.key:
            # Node fits right of this root
            root.right = self._insert(root.right, node)

        elif node.key == root.key:
            # Node is already in the tree.
            # Update it.
            root.value = node.value

        # Recompute hight of root
        root.height = self._compute_height(root)

        # return the balanced subtree
        return self._rebalance(root)

    def _pop_right_min(self, root: AVLNode) -> AVLNode:
        """Remove the min from the right side of the given subtree"""
        n = self._get_min(root.right)
        root.right = self._delete(root.right, n.key)
        return n

    @classmethod
    def _rebalance(cls, root: AVLNode) -> AVLNode:
        """Rebalance the immediate subtree."""

        balance = cls._compute_balance(root)

        if balance > 1: # left heavy
            if cls._compute_balance(root.left) < 0:
                root.left = cls._rotate_left(root.left)
            return cls._rotate_right(root)
        elif balance < -1: # Right heavy
            if cls._compute_balance(root.right) > 0:
                root.right = cls._rotate_right(root.right)
            return cls._rotate_left(root)

        return root

    @classmethod
    def _rotate_right(cls, x: AVLNode) -> AVLNode:
        """Rotate a subtree around x.left"""

        # Rotate right, pivot on y
        #     x          y
        #    / \        / \ 
        #   y  T3 -->  T1  x
        #  / \            / \ 
        # T1 T2          T2 T3

        y = x.left
        t2 = y.right
        y.right = x
        x.left = t2

        # x hight is used to compute y hight
        # so compute x firt.
        x.height = cls._compute_height(x)
        y.height = cls._compute_height(y)

        return y

    @classmethod
    def _rotate_left(cls, y: AVLNode) -> AVLNode:
        """Rotate a subtree around y.right"""

        # Rotate left, pivot on x
        #     x          y
        #    / \        / \ 
        #   y  T3 <--  T1  x
        #  / \            / \ 
        # T1 T2          T2 T3

        x = y.right
        t2 = x.left
        x.left = y
        y.right = t2

        # y hight is used to compute x hight
        # so compute y firt.
        y.height = cls._compute_height(y)
        x.height = cls._compute_height(x)

        return x

    @classmethod
    def _get_min(cls, root: AVLNode) -> AVLNode:
        """Find the min value in a given subtree"""
        if root.left is None:
            return root
        return cls._get_min(root.left)

    @classmethod
    def _height(cls, root: AVLNode) -> int:
        """Get the normalized height of the given node.

        If the node is null, -1 will be returned.
        """
        if root is None:
            return -1
        return root.height

    @classmethod
    def _compute_height(cls, root: AVLNode) -> int:
        """Compute the hight of the given subtree."""
        return max(cls._height(root.left), cls._height(root.right)) + 1

    @classmethod
    def _compute_balance(cls, root: AVLNode) -> int:
        """Compute the balance of the given subtree."""
        return cls._height(root.left) - cls._height(root.right)
