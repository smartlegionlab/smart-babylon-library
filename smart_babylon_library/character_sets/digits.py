# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2025, Alexander Suvorov
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from .constants import DIGITS
from .core import CharacterSet

class Digits(CharacterSet):
    @property
    def characters(self):
        return frozenset(DIGITS)

    @property
    def name(self) -> str:
        return "Digits (0-9)"