# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import hashlib
import random
import string
from typing import Optional, Dict, Tuple

from smart_babylon_library.config import RU


class BabylonLibrary:
    def __init__(
        self,
        charset: str = RU + string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation + ' ',
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

    def generate_text(self, seed: str) -> str:
        hash_value = hashlib.sha256(seed.encode()).hexdigest()
        text = []
        while len(text) < self.page_length:
            for i in range(0, len(hash_value), 2):
                index = int(hash_value[i:i + 2], 16) % len(self.charset)
                text.append(self.charset[index])
                if len(text) >= self.page_length:
                    break
            hash_value = hashlib.sha256(hash_value.encode()).hexdigest()
        return ''.join(text)

    def get_text(self, address: str) -> str:
        return self.generate_text(address)

    def generate_random_address(self) -> str:
        return self.generate_address_with_pattern()

    def generate_address_with_pattern(self, pattern: Optional[Dict[str, int]] = None) -> str:
        if pattern is None:
            pattern = {}
        room = pattern.get("room", random.randint(1, self.max_rooms))
        wall = pattern.get("wall", random.randint(1, self.max_walls))
        shelf = pattern.get("shelf", random.randint(1, self.max_shelves))
        volume = pattern.get("volume", random.randint(1, self.max_volumes))
        book = pattern.get("book", random.randint(1, self.max_books))
        page = pattern.get("page", random.randint(1, self.max_pages))
        return f"Room{room}:Wall{wall}:Shelf{shelf}:Volume{volume}:Book{book}:Page{page}"

    def search_for_text_with_pattern(
        self, target_text: str, pattern: Optional[Dict[str, int]] = None, max_attempts: int = 1000000
    ) -> Tuple[Optional[str], Optional[str]]:
        for _ in range(max_attempts):
            address = self.generate_address_with_pattern(pattern)
            text = self.get_text(address)
            if target_text in text:
                return address, text
        return None, None

    def __iter__(self):
        self.current_address = self.generate_address_with_pattern(
            {"room": 1, "wall": 1, "shelf": 1, "volume": 1, "book": 1, "page": 1}
        )
        return self

    def __next__(self) -> Tuple[str, str]:
        address = self.current_address
        text = self.get_text(address)
        self.current_address = self._generate_next_address(self.current_address)
        return address, text

    def _generate_next_address(self, current_address: str) -> str:
        parts = current_address.split(':')
        room = int(parts[0].replace("Room", ""))
        wall = int(parts[1].replace("Wall", ""))
        shelf = int(parts[2].replace("Shelf", ""))
        volume = int(parts[3].replace("Volume", ""))
        book = int(parts[4].replace("Book", ""))
        page = int(parts[5].replace("Page", ""))

        page += 1
        if page > self.max_pages:
            page = 1
            book += 1
            if book > self.max_books:
                book = 1
                volume += 1
                if volume > self.max_volumes:
                    volume = 1
                    shelf += 1
                    if shelf > self.max_shelves:
                        shelf = 1
                        wall += 1
                        if wall > self.max_walls:
                            wall = 1
                            room += 1
                            if room > self.max_rooms:
                                room = 1

        return f"Room{room}:Wall{wall}:Shelf{shelf}:Volume{volume}:Book{book}:Page{page}"

    def _generate_previous_address(self, current_address: str) -> str:
        parts = current_address.split(':')
        room = int(parts[0].replace("Room", ""))
        wall = int(parts[1].replace("Wall", ""))
        shelf = int(parts[2].replace("Shelf", ""))
        volume = int(parts[3].replace("Volume", ""))
        book = int(parts[4].replace("Book", ""))
        page = int(parts[5].replace("Page", ""))

        page -= 1
        if page < 1:
            page = self.max_pages
            book -= 1
            if book < 1:
                book = self.max_books
                volume -= 1
                if volume < 1:
                    volume = self.max_volumes
                    shelf -= 1
                    if shelf < 1:
                        shelf = self.max_shelves
                        wall -= 1
                        if wall < 1:
                            wall = self.max_walls
                            room -= 1
                            if room < 1:
                                room = self.max_rooms

        return f"Room{room}:Wall{wall}:Shelf{shelf}:Volume{volume}:Book{book}:Page{page}"


def main():
    library = BabylonLibrary()

    address = "Room1:Wall1:Shelf1:Volume1:Book1:Page1"
    text = library.get_text(address)
    print(f"Text at address {address}:\n{text}\n")

    target_text = "xxx"
    found_address, found_text = library.search_for_text_with_pattern(target_text, max_attempts=1000)
    if found_address:
        print(f"Text '{target_text}' found at address {found_address}:\n{found_text}\n")
    else:
        print(f"Text '{target_text}' not found.\n")

    print("Let's start iterating on the library:")
    iterator = iter(library)
    for _ in range(10):
        address, text = next(iterator)
        print(f"Address: {address}\nText: {text[:50]}...\n")

    print("Moving forward and backward through the library:")
    current_address = "Room1:Wall1:Shelf1:Volume1:Book1:Page1"

    print("Moving forward:")
    for _ in range(5):
        current_address = library._generate_next_address(current_address)
        text = library.get_text(current_address)
        print(f"Address: {current_address}\nText: {text[:50]}...\n")

    print("Moving back:")
    for _ in range(3):
        current_address = library._generate_previous_address(current_address)
        text = library.get_text(current_address)
        print(f"Address: {current_address}\nText: {text[:50]}...\n")


if __name__ == '__main__':
    main()
