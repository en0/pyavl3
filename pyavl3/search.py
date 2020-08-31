from typing import Hashable, Tuple, Generator
from collections import deque

from .interface import ADTInterface, SearchAlgorithm


class GreatherThanSearch(SearchAlgorithm):

    def __init__(self, limit: Hashable):
        self._limit = limit

    def __call__(self, tree: ADTInterface) -> Generator[Tuple[Hashable, any], None, None]:
        q = deque([(0, tree.root)])
        while q:
            v, n = q.pop()
            if n is None:
                continue
            elif v == 0:
                if n.key <= self._limit:
                    q.append((0, n.right))
                elif n.key > self._limit:
                    q.append((0, n.right))
                    q.append((1, n))
                    q.append((0, n.left))
            elif v == 1:
                yield n.key, n.value


class GreatherThanOrEqualSearch(SearchAlgorithm):

    def __init__(self, limit: Hashable):
        self._limit = limit

    def __call__(self, tree: ADTInterface) -> Generator[Tuple[Hashable, any], None, None]:
        q = deque([(0, tree.root)])
        while q:
            v, n = q.pop()
            if n is None:
                continue
            elif v == 0:
                if n.key < self._limit:
                    q.append((0, n.right))
                elif n.key >= self._limit:
                    q.append((0, n.right))
                    q.append((1, n))
                    q.append((0, n.left))
            elif v == 1:
                yield n.key, n.value


class LessThanSearch(SearchAlgorithm):

    def __init__(self, limit: Hashable):
        self._limit = limit

    def __call__(self, tree: ADTInterface) -> Generator[Tuple[Hashable, any], None, None]:
        q = deque([(0, tree.root)])
        while q:
            v, n = q.pop()
            if n is None:
                continue
            elif v == 0:
                if n.key >= self._limit:
                    q.append((0, n.left))
                elif n.key < self._limit:
                    q.append((0, n.right))
                    q.append((1, n))
                    q.append((0, n.left))
            elif v == 1:
                yield n.key, n.value


class LessThanOrEqualSearch(SearchAlgorithm):

    def __init__(self, limit: Hashable):
        self._limit = limit

    def __call__(self, tree: ADTInterface) -> Generator[Tuple[Hashable, any], None, None]:
        q = deque([(0, tree.root)])
        while q:
            v, n = q.pop()
            if n is None:
                continue
            elif v == 0:
                if n.key > self._limit:
                    q.append((0, n.left))
                elif n.key <= self._limit:
                    q.append((0, n.right))
                    q.append((1, n))
                    q.append((0, n.left))
            elif v == 1:
                yield n.key, n.value


class BetweenSearch(SearchAlgorithm):

    def __init__(self, lower: Hashable, upper: Hashable):
        self._lower = lower
        self._upper = upper

    def __call__(self, tree: ADTInterface) -> Generator[Tuple[Hashable, any], None, None]:
        greater_search = GreatherThanSearch(self._lower)
        for k, v in greater_search(tree):
            # Take advantage of the fact that these searches
            # return using in-order traversal
            if k >= self._upper:
                break;
            yield k, v
