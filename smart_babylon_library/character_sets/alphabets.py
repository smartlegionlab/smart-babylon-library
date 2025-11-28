# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2025, Alexander Suvorov
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from smart_babylon_library.character_sets.constants import (
    CYRILLIC_UPPERCASE,
    CYRILLIC_LOWERCASE,
    LATIN_UPPERCASE,
    LATIN_LOWERCASE
)
from smart_babylon_library.character_sets.core import CharacterSet


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
