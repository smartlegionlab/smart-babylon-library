# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import os
import random
import re
import string
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Optional, Dict, Tuple, Union

from smart_babylon_library.config import RU


class SmartBabylonLibrary:
    def __init__(
        self,
        charset: str = RU + string.ascii_letters + string.digits,
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

    def generate_word(self, seed: str, min_length: int = 1, max_length: int = 10) -> str:
        random.seed(seed)
        length = random.randint(min_length, max_length)

        first_char = random.choice(self.charset)

        if first_char.isalpha():
            if first_char in RU:
                charset = RU
            else:
                charset = string.ascii_letters
        else:
            charset = string.digits + " "

        word = first_char + ''.join(random.choice(charset) for _ in range(length - 1))
        return word

    def generate_sentence(self, seed: str) -> str:
        random.seed(seed)
        sentence_length = random.randint(5, 20)
        words = [self.generate_word(seed + str(i)) for i in range(sentence_length)]
        sentence = ' '.join(words).capitalize()
        sentence += random.choice(['.', '!', '?']) + ' '
        return sentence

    def generate_page(self, seed: str) -> str:
        random.seed(seed)
        page = []
        while len(''.join(page)) < self.page_length:
            sentence = self.generate_sentence(seed + str(len(page)))
            page.append(sentence)
        return ''.join(page)

    def generate_book_title(self, seed: str) -> str:
        random.seed(seed)
        if random.choice([True, False]):
            return self.generate_word(seed, min_length=3, max_length=10).capitalize()
        else:
            sentence = self.generate_sentence(seed).strip()
            return sentence[:-1]

    def generate_book(self, seed: str, num_pages: int) -> Dict[str, Union[str, List[str]]]:
        title = self.generate_book_title(seed + "title")
        pages = [self.generate_page(seed + "page" + str(i)) for i in range(num_pages)]
        return {"title": title, "pages": pages}

    def get_text(self, address: str, start: Optional[int] = None, end: Optional[int] = None) -> str:
        parts = address.split(':')
        if len(parts) == 5:
            seed = address
            book = self.generate_book(seed, self.max_pages)
            full_text = ''.join(book["pages"])
            return full_text[start:end] if start is not None and end is not None else full_text
        elif len(parts) == 6:
            seed = ':'.join(parts[:5])
            page_num = int(parts[5].replace("Page", "")) - 1
            book = self.generate_book(seed, self.max_pages)
            if 0 <= page_num < len(book["pages"]):
                page_text = book["pages"][page_num]
                return page_text[start:end] if start is not None and end is not None else page_text
            else:
                raise ValueError("Page number out of range.")
        elif len(parts) == 8:
            seed = ':'.join(parts[:5])
            page_num = int(parts[5].replace("Page", "")) - 1
            start = int(parts[6])
            end = int(parts[7])
            book = self.generate_book(seed, self.max_pages)
            if 0 <= page_num < len(book["pages"]):
                page_text = book["pages"][page_num]
                if start < 0 or end > len(page_text):
                    raise ValueError("Slice out of range.")
                return page_text[start:end]
            else:
                raise ValueError("Page number out of range.")
        else:
            raise ValueError("Incorrect address format.")

    def get_book_title(self, address: str) -> str:
        parts = address.split(':')
        if len(parts) == 5:
            seed = address
            book = self.generate_book(seed, self.max_pages)
            return str(book["title"])
        else:
            raise ValueError("Incorrect address format for getting book title.")

    def search_in_library(self, target_text: str, max_attempts: int = 1000000) -> Optional[Tuple[str, int, int]]:
        for _ in range(max_attempts):
            address = self.generate_random_address()
            text = self.get_text(address)
            start_index = text.find(target_text)
            if start_index != -1:
                return address, start_index, start_index + len(target_text)
        return None

    def search_in_titles(self, target_text: str, max_attempts: int = 1000000) -> Optional[str]:
        for _ in range(max_attempts):
            address = self.generate_random_address()
            seed = ':'.join(address.split(':')[:5])
            book = self.generate_book(seed, self.max_pages)
            if target_text in book["title"]:
                return seed
        return None

    def generate_random_address(self) -> str:
        room = random.randint(1, self.max_rooms)
        wall = random.randint(1, self.max_walls)
        shelf = random.randint(1, self.max_shelves)
        volume = random.randint(1, self.max_volumes)
        book = random.randint(1, self.max_books)
        page = random.randint(1, self.max_pages)
        return f"Room{room}:Wall{wall}:Shelf{shelf}:Volume{volume}:Book{book}:Page{page}"

    def search_in_library_parallel(
            self, target_text: str, max_attempts: int = 1000000, num_threads: Optional[int] = None
    ) -> Optional[Tuple[str, int, int]]:
        if num_threads is None:
            num_threads = os.cpu_count() or 4
            print(f"Using {num_threads} threads based on available CPU cores.")

        attempts_per_thread = max_attempts // num_threads

        def search_task(attempts: int):
            for _ in range(attempts):
                address = self.generate_random_address()
                text = self.get_text(address)

                pattern = re.compile(r'\b' + re.escape(target_text) + r'\b')
                match = pattern.search(text)

                if match:
                    start_index = match.start()
                    end_index = match.end()
                    print(f"Found '{target_text}' at address: {address}, positions: {start_index}-{end_index}")
                    return address, start_index, end_index
            return None

        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(search_task, attempts_per_thread) for _ in range(num_threads)]

            for future in as_completed(futures):
                result = future.result()
                if result:
                    return result

        print(f"'{target_text}' not found after {max_attempts} attempts.")
        return None


class SmartBabylonLibraryIterator:
    def __init__(self, library: SmartBabylonLibrary, start_address: Optional[str] = None):
        self.library = library
        self.current_address = start_address or "Room1:Wall1:Shelf1:Volume1:Book1:Page1"

    def __iter__(self):
        return self

    def __next__(self) -> Tuple[str, str, str]:
        parts = self.current_address.split(':')
        room = int(parts[0].replace("Room", ""))
        wall = int(parts[1].replace("Wall", ""))
        shelf = int(parts[2].replace("Shelf", ""))
        volume = int(parts[3].replace("Volume", ""))
        book = int(parts[4].replace("Book", ""))
        page = int(parts[5].replace("Page", ""))

        book_address = f"Room{room}:Wall{wall}:Shelf{shelf}:Volume{volume}:Book{book}"
        title = self.library.get_book_title(book_address)

        text = self.library.get_text(self.current_address)

        page += 1
        if page > self.library.max_pages:
            page = 1
            book += 1
            if book > self.library.max_books:
                book = 1
                volume += 1
                if volume > self.library.max_volumes:
                    volume = 1
                    shelf += 1
                    if shelf > self.library.max_shelves:
                        shelf = 1
                        wall += 1
                        if wall > self.library.max_walls:
                            wall = 1
                            room += 1
                            if room > self.library.max_rooms:
                                raise StopIteration

        self.current_address = f"Room{room}:Wall{wall}:Shelf{shelf}:Volume{volume}:Book{book}:Page{page}"
        return self.current_address, title, text
