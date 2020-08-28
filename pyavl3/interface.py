from typing import Hashable, Iterator, Tuple
from abc import ABC, abstractmethod


class ADTInterface(ABC):

    @abstractmethod
    def __getitem__(self, key: Hashable) -> any:
        raise NotImplemented

    @abstractmethod
    def __setitem__(self, key: Hashable, value: any) -> None:
        raise NotImplemented

    @abstractmethod
    def __delitem__(self, key: Hashable) -> None:
        raise NotImplemented

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplemented

    @abstractmethod
    def __contains__(self, key: Hashable) -> bool:
        raise NotImplemented

    @abstractmethod
    def __iter__(self) -> Iterator[Tuple[Hashable, any]]:
        raise NotImplemented

