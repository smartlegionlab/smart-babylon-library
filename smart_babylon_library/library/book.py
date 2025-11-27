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


class LibraryBook:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self._generator = DeterministicGenerator()
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
        if page_number > self.max_pages:
            raise ValueError(f"Page number cannot exceed {self.max_pages}")

        page_coordinates = LibraryCoordinates(
            self.coordinates.floor, self.coordinates.room,
            self.coordinates.cabinet, self.coordinates.shelf,
            self.coordinates.book, page_number
        )
        return LibraryPage(page_coordinates)

    def to_dict(self) -> dict:
        return {
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
        return f"Book '{title}'"

class LibraryPage:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self._generator = DeterministicGenerator()
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
            'coordinates': self.coordinates.to_dict(),
            'page_number': self.page_number,
            'content': self.content
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def __str__(self):
        return f"Page {self.page_number}: {self.content[:50]}..." if len(self.content) > 50 else f"Page {self.page_number}: {self.content}"
