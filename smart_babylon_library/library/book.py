# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2025, Alexander Suvorov
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import json

from smart_babylon_library.library.coordinates import LibraryCoordinates
from smart_babylon_library.library.generator import DeterministicGenerator
from smart_babylon_library.library.config import LibraryConfig


class LibraryBook:
    def __init__(self, coordinates, config: LibraryConfig = None):
        self.coordinates = coordinates
        self.config = config or LibraryConfig()
        self._generator = DeterministicGenerator(self.config)
        self._title = None
        self._max_pages = None

    @property
    def title(self) -> str:
        if self._title is None:
            self._title = self._generator.generate_book_title(self.coordinates)
        return self._title

    @property
    def max_pages(self) -> int:
        if self._max_pages is None:
            self._max_pages = self._generator.get_max_pages_for_book(self.coordinates)
        return self._max_pages

    def get_page(self, page_number: int):
        if page_number < 0:
            raise ValueError("Page number must be non-negative")
        if page_number >= self.max_pages:
            raise ValueError(f"Page number cannot exceed {self.max_pages - 1}")

        page_coordinates = LibraryCoordinates(
            self.coordinates.floor, self.coordinates.room,
            self.coordinates.cabinet, self.coordinates.shelf,
            self.coordinates.book, page_number
        )
        return LibraryPage(page_coordinates, self.config)

    def to_dict(self) -> dict:
        return {
            'universe': self.config.universe,
            'coordinates': self.coordinates.to_dict(),
            'title': self.title,
            'page_count': self.max_pages
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def get_page_json(self, page_number: int) -> str:
        page = self.get_page(page_number)
        return page.to_json()

    def __str__(self):
        title = self.title[:30] + '...' if len(self.title) > 30 else self.title
        return f"Book '{title}' (Universe: {self.config.universe})"


class LibraryPage:
    def __init__(self, coordinates, config: LibraryConfig = None):
        self.coordinates = coordinates
        self.config = config or LibraryConfig()
        self._generator = DeterministicGenerator(self.config)
        self._content = None

    @property
    def content(self) -> str:
        if self._content is None:
            self._content = self._generator.generate_page_content(self.coordinates)
        return self._content

    @property
    def page_number(self) -> int:
        return self.coordinates.page

    def to_dict(self) -> dict:
        return {
            'universe': self.config.universe,
            'coordinates': self.coordinates.to_dict(),
            'page_number': self.page_number,
            'content': self.content
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def __str__(self):
        content_preview = self.content[:50] + '...' if len(self.content) > 50 else self.content
        return f"Page {self.page_number} (Universe: {self.config.universe}): {content_preview}"
