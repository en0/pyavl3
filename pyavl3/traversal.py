from collections import deque
from typing import (
    Union,
    Iterator,
    Hashable,
    Tuple,
    Generic,
    TypeVar,
    Callable,
)

from .interface import AVLNode, ADTInterface


IterType = TypeVar('IterType')


class InOrderTraversal(Iterator[IterType]):
    def __init__(
        self,
        tree: Union[ADTInterface, AVLNode],
        transform: Callable[[AVLNode], IterType] = None
    ) -> None:
        if isinstance(tree, ADTInterface):
            self._deque = deque([(0, tree.root)])
        else:
            self._deque = deque([(0, tree)])
        self._xfrm = transform or (lambda x: x)

    def __next__(self) -> IterType:
        while self._deque:
            visits, node = self._deque.pop()
            if node is None:
                continue
            elif visits == 0:
                self._deque.append((1, node))
                self._deque.append((0, node.left))
            elif visits == 1:
                self._deque.append((0, node.right))
                return self._xfrm(node)
        raise StopIteration()
        

class BreadthFirstTraversal(Iterator[IterType]):
    def __init__(
        self,
        tree: Union[ADTInterface, AVLNode],
        transform: Callable[[AVLNode], IterType] = None
    ) -> None:
        if isinstance(tree, ADTInterface):
            self._deque = deque([tree.root])
        else:
            self._deque = deque([tree])
        self._xfrm = transform or (lambda x: x)

    def __next__(self) -> IterType:
        while self._deque:
            node = self._deque.pop()

            if node is None:
                continue

            self._deque.appendleft(node.left)
            self._deque.appendleft(node.right)
            return self._xfrm(node)

        raise StopIteration()
        
