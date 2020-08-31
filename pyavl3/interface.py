from abc import ABC, abstractmethod, abstractclassmethod
from typing import (
    Hashable,
    Generator,
    Iterator,
    Tuple,
    Union,
    Dict,
    Iterable,
    Callable,
)

from .avl_node import AVLNode


class ADTInterface(ABC):

    @property
    @abstractmethod
    def root(self) -> AVLNode:
        raise NotImplementedError()

    @abstractmethod
    def __getitem__(self, key: Hashable) -> any:
        raise NotImplementedError()

    @abstractmethod
    def __setitem__(self, key: Hashable, value: any) -> None:
        raise NotImplementedError()

    @abstractmethod
    def __delitem__(self, key: Hashable) -> None:
        raise NotImplementedError()

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def __contains__(self, key: Hashable) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def __iter__(self) -> Iterator[Tuple[Hashable, any]]:
        raise NotImplementedError()

    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def __bool__(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def keys(self) -> Iterator[Hashable]:
        raise NotImplementedError()

    @abstractmethod
    def items(self) -> Iterator[Tuple[Hashable, any]]:
        raise NotImplementedError()

    @abstractmethod
    def values(self) -> Iterator[Hashable]:
        raise NotImplementedError()

    @abstractmethod
    def clear(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def copy(self) -> "AVLTree":
        raise NotImplementedError()

    @abstractmethod
    def setdefault(self, key: Hashable, value: any) -> None:
        raise NotImplementedError()

    @abstractmethod
    def update(
        self,
        iterable: Union[
            Dict[Hashable, any],
            Iterable[Tuple[Hashable, any]],
        ] = None,
        **kwargs
    ) -> None:
        raise NotImplementedError()

    @abstractmethod
    def pop(self, key: Hashable) -> any:
        raise NotImplementedError()

    @abstractmethod
    def popitem(self, key: Hashable) -> Tuple[Hashable, any]:
        raise NotImplementedError()

    @abstractclassmethod
    def fromkeys(self) -> "AVLTree":
        raise NotImplementedError()


SearchAlgorithm = Callable[[ADTInterface], Generator[Tuple[Hashable, any], None, None]]
