# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2025, Alexander Suvorov
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from .constants import PUNCTUATION_MARKS
from .core import CharacterSet

class Punctuation(CharacterSet):
    @property
    def characters(self):
        return frozenset(PUNCTUATION_MARKS)

    @property
    def name(self) -> str:
        return "Punctuation and Symbols"