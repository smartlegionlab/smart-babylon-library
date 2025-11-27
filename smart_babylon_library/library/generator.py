# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2025, Alexander Suvorov
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import hashlib
import random
from ..character_sets.alphabets import CyrillicAlphabet, LatinAlphabet
from ..character_sets.digits import Digits
from ..character_sets.punctuation import Punctuation

class DeterministicGenerator:
    MAX_BOOK_TITLE_LENGTH = 3000
    MIN_BOOK_TITLE_LENGTH = 2
    MAX_PAGE_CONTENT_LENGTH = 50000
    MAX_PAGES_PER_BOOK = 15784

    def __init__(self):
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
        title_length = random_generator.randint(self.MIN_BOOK_TITLE_LENGTH, self.MAX_BOOK_TITLE_LENGTH)
        title_chars = [random_generator.choice(self._all_chars) for _ in range(title_length)]
        return ''.join(title_chars)

    def generate_page_content(self, coordinates) -> str:
        random_generator = self._get_deterministic_random(f"content_{coordinates.seed}")
        content_length = random_generator.randint(1, self.MAX_PAGE_CONTENT_LENGTH)
        content_chars = [random_generator.choice(self._all_chars) for _ in range(content_length)]
        return ''.join(content_chars)
