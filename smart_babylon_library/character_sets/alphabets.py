from .core import CharacterSet
from .constants import (
    CYRILLIC_UPPERCASE,
    CYRILLIC_LOWERCASE,
    LATIN_UPPERCASE,
    LATIN_LOWERCASE
)


class CyrillicAlphabet(CharacterSet):

    @property
    def characters(self):
        return frozenset(CYRILLIC_UPPERCASE + CYRILLIC_LOWERCASE)

    @property
    def name(self) -> str:
        return "Russian Alphabet (both cases)"


class LatinAlphabet(CharacterSet):

    @property
    def characters(self):
        return frozenset(LATIN_UPPERCASE + LATIN_LOWERCASE)

    @property
    def name(self) -> str:
        return "English Alphabet (both cases)"
