from typing import Iterator, Hashable, Tuple
from collections import deque

from .avl_node import AVLNode


class InOrderTraversal(Iterator[Tuple[Hashable, any]]):
    def __init__(self, root: AVLNode) -> None:
        self._deque = deque([(0, root)])

    def __next__(self) -> Tuple[Hashable, any]:
        while self._deque:
            visits, node = self._deque.pop()
            if node is None:
                continue
            elif visits == 0:
                self._deque.append((1, node))
                self._deque.append((0, node.left))
            elif visits == 1:
                self._deque.append((0, node.right))
                return node.key, node.value
        raise StopIteration()
        
