# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2025, Alexander Suvorov
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from smart_babylon_library.library.book import LibraryBook, LibraryPage
from smart_babylon_library.library.coordinates import LibraryCoordinates
from smart_babylon_library.library.config import LibraryConfig


class SmartBabylonLibrary:
    def __init__(self, config: LibraryConfig = None):
        self.config = config or LibraryConfig()

    def get_book(self, floor: int, room: int, cabinet: int, shelf: int, book_number: int):
        coordinates = LibraryCoordinates(floor, room, cabinet, shelf, book_number, 0)
        return LibraryBook(coordinates, self.config)

    def get_book_from_dict(self, coordinates_dict: dict):
        coordinates = LibraryCoordinates.from_dict(coordinates_dict)
        return LibraryBook(coordinates, self.config)

    def get_book_json(self, coordinates_dict: dict) -> str:
        book = self.get_book_from_dict(coordinates_dict)
        return book.to_json()

    def get_page(self, floor: int, room: int, cabinet: int, shelf: int, book_number: int, page: int):
        coordinates = LibraryCoordinates(floor, room, cabinet, shelf, book_number, page)
        return LibraryPage(coordinates, self.config)

    def get_page_from_dict(self, coordinates_dict: dict):
        coordinates = LibraryCoordinates.from_dict(coordinates_dict)
        return LibraryPage(coordinates, self.config)

    def get_page_json(self, coordinates_dict: dict) -> str:
        page = self.get_page_from_dict(coordinates_dict)
        return page.to_json()
