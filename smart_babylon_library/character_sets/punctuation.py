# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2025, Alexander Suvorov
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from smart_babylon_library.character_sets.constants import PUNCTUATION_MARKS
from smart_babylon_library.character_sets.core import CharacterSet


class Punctuation(CharacterSet):
    @property
    def characters(self):
        chars = list(PUNCTUATION_MARKS)
        return sorted(chars)

    @property
    def name(self) -> str:
        return "Punctuation and Symbols"
