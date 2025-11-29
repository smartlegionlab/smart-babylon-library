# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2025, Alexander Suvorov
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from dataclasses import dataclass
from typing import Tuple, List, Optional
from smart_babylon_library.character_sets.core import CharacterSet
from smart_babylon_library.character_sets.alphabets import CyrillicAlphabet, LatinAlphabet
from smart_babylon_library.character_sets.digits import Digits
from smart_babylon_library.character_sets.punctuation import Punctuation


@dataclass
class LibraryConfig:
    universe: str = "default"
    title_length_range: Tuple[int, int] = (2, 3000)
    content_length_range: Tuple[int, int] = (1, 50000)
    pages_per_book_range: Tuple[int, int] = (1, 15784)
    character_sets: Optional[List[CharacterSet]] = None

    def __post_init__(self):
        if not isinstance(self.universe, str):
            raise ValueError("Universe must be a string")
        if self.title_length_range[0] < 1 or self.title_length_range[1] < self.title_length_range[0]:
            raise ValueError("Invalid title_length_range")
        if self.content_length_range[0] < 1 or self.content_length_range[1] < self.content_length_range[0]:
            raise ValueError("Invalid content_length_range")
        if self.pages_per_book_range[0] < 1 or self.pages_per_book_range[1] < self.pages_per_book_range[0]:
            raise ValueError("Invalid pages_per_book_range")

        if self.character_sets is None:
            self.character_sets = [
                CyrillicAlphabet(),
                LatinAlphabet(),
                Digits(),
                Punctuation()
            ]
