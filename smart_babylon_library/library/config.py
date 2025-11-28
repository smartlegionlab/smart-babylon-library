# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2025, Alexander Suvorov
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from dataclasses import dataclass
from typing import Tuple


@dataclass
class LibraryConfig:
    title_length_range: Tuple[int, int] = (2, 3000)
    content_length_range: Tuple[int, int] = (1, 50000)
    pages_per_book_range: Tuple[int, int] = (1, 15784)

    def __post_init__(self):
        if self.title_length_range[0] < 1 or self.title_length_range[1] < self.title_length_range[0]:
            raise ValueError("Invalid title_length_range")
        if self.content_length_range[0] < 1 or self.content_length_range[1] < self.content_length_range[0]:
            raise ValueError("Invalid content_length_range")
        if self.pages_per_book_range[0] < 1 or self.pages_per_book_range[1] < self.pages_per_book_range[0]:
            raise ValueError("Invalid pages_per_book_range")
