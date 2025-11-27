from abc import ABC, abstractmethod
from typing import FrozenSet


class CharacterSet(ABC):

    @property
    @abstractmethod
    def characters(self) -> FrozenSet[str]:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    def __contains__(self, character: str) -> bool:
        return character in self.characters

    def __iter__(self):
        return iter(self.characters)

    def __len__(self) -> int:
        return len(self.characters)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', characters_count={len(self)})"
