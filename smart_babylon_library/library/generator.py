# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2025, Alexander Suvorov
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import hashlib
import random

from smart_babylon_library.character_sets.alphabets import CyrillicAlphabet, LatinAlphabet
from smart_babylon_library.character_sets.digits import Digits
from smart_babylon_library.character_sets.punctuation import Punctuation
from smart_babylon_library.library.config import LibraryConfig


class DeterministicGenerator:
    def __init__(self, config: LibraryConfig = None):
        self.config = config or LibraryConfig()
        self._all_chars = (
            list(CyrillicAlphabet().characters) +
            list(LatinAlphabet().characters) +
            list(Digits().characters) +
            list(Punctuation().characters)
        )

    def _get_deterministic_random(self, seed: str) -> random.Random:
        seed_hash = hashlib.sha256(seed.encode()).hexdigest()
        return random.Random(int(seed_hash, 16))

    def generate_book_title(self, coordinates) -> str:
        random_generator = self._get_deterministic_random(f"title_{coordinates.seed}")
        min_len, max_len = self.config.title_length_range
        title_length = random_generator.randint(min_len, max_len)
        title_chars = [random_generator.choice(self._all_chars) for _ in range(title_length)]
        return ''.join(title_chars)

    def generate_page_content(self, coordinates) -> str:
        random_generator = self._get_deterministic_random(f"content_{coordinates.seed}")
        min_len, max_len = self.config.content_length_range
        content_length = random_generator.randint(min_len, max_len)
        content_chars = [random_generator.choice(self._all_chars) for _ in range(content_length)]
        return ''.join(content_chars)

    def get_max_pages_for_book(self, coordinates) -> int:
        random_generator = self._get_deterministic_random(f"pages_{coordinates.seed}")
        min_pages, max_pages = self.config.pages_per_book_range
        return random_generator.randint(min_pages, max_pages)
