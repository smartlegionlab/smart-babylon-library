# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import random
import string
from typing import List, Optional, Dict, Tuple, Iterator


class BabylonLibraryWithBooks:
    def __init__(
        self,
        charset: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" +
                       string.ascii_letters + string.digits,
        page_length: int = 3200,
        max_rooms: int = 100,
        max_walls: int = 6,
        max_shelves: int = 10,
        max_volumes: int = 10,
        max_books: int = 100,
        max_pages: int = 1000,
    ):
        self.charset = charset
        self.page_length = page_length
        self.max_rooms = max_rooms
        self.max_walls = max_walls
        self.max_shelves = max_shelves
        self.max_volumes = max_volumes
        self.max_books = max_books
        self.max_pages = max_pages
        self.books = []

    def generate_word(self, min_length: int = 1, max_length: int = 10) -> str:
        length = random.randint(min_length, max_length)
        if random.random() < 0.95:
            charset = ''.join([c for c in self.charset if c.isalpha()])
        else:
            charset = ''.join([c for c in self.charset if c.isdigit()])
        return ''.join(random.choice(charset) for _ in range(length))

    def generate_sentence(self) -> str:
        sentence_length = random.randint(5, 20)
        words = [self.generate_word() for _ in range(sentence_length)]
        sentence = ' '.join(words).capitalize()
        sentence += random.choice(['.', '!', '?']) + ' '
        return sentence

    def generate_page(self) -> str:
        page = []
        while len(''.join(page)) < self.page_length:
            sentence = self.generate_sentence()
            page.append(sentence)
        return ''.join(page)

    def generate_book_title(self) -> str:
        if random.choice([True, False]):
            return self.generate_word(min_length=3, max_length=10).capitalize()
        else:
            sentence = self.generate_sentence().strip()
            return sentence[:-1]

    def generate_book(self, num_pages: int, title: Optional[str] = None) -> Dict[str, List[str]]:
        if title is None:
            title = self.generate_book_title()
        pages = [self.generate_page() for _ in range(num_pages)]
        return {"title": title, "pages": pages}

    def add_book_to_library(self, book: Dict[str, List[str]]) -> str:
        self.books.append(book)
        room = random.randint(1, self.max_rooms)
        wall = random.randint(1, self.max_walls)
        shelf = random.randint(1, self.max_shelves)
        volume = random.randint(1, self.max_volumes)
        book_num = len(self.books)
        return f"Room{room}:Wall{wall}:Shelf{shelf}:Volume{volume}:Book{book_num}"

    def get_text(self, address: str, start: Optional[int] = None, end: Optional[int] = None) -> str:
        book = self.books[int(address.split(":")[-1].replace("Book", "")) - 1]
        full_text = ''.join(book["pages"])
        if start is not None and end is not None:
            return full_text[start:end]
        return full_text

    def search_in_library(self, target_text: str) -> Optional[Tuple[str, int, int]]:
        for address in range(len(self.books)):
            book = self.books[address]
            full_text = ''.join(book["pages"])
            start_index = full_text.find(target_text)
            if start_index != -1:
                return f"Room1:Wall1:Shelf1:Volume1:Book{address + 1}", start_index, start_index + len(target_text)
        return None

    def __iter__(self) -> Iterator[Tuple[str, str]]:
        self.current_index = 0
        return self

    def __next__(self) -> Tuple[str, str]:
        if self.current_index >= len(self.books):
            raise StopIteration
        address = f"Room1:Wall1:Shelf1:Volume1:Book{self.current_index + 1}"
        title = self.books[self.current_index]["title"]
        self.current_index += 1
        return address, title
