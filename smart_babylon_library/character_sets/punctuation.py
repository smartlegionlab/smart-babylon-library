from .core import CharacterSet
from .constants import PUNCTUATION_MARKS


class Punctuation(CharacterSet):

    @property
    def characters(self):
        return frozenset(PUNCTUATION_MARKS)

    @property
    def name(self) -> str:
        return "Punctuation and Symbols"
