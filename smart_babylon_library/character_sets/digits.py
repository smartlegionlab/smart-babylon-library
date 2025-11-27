from .core import CharacterSet
from .constants import DIGITS


class Digits(CharacterSet):

    @property
    def characters(self):
        return frozenset(DIGITS)

    @property
    def name(self) -> str:
        return "Digits (0-9)"
