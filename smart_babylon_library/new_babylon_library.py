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

from smart_babylon_library.config import RU


class BabylonLibrary:
    def __init__(self, charset=string.ascii_letters + string.digits + string.punctuation + " " + RU, page_length=3200):
        self.charset = charset
        self.page_length = page_length

    def generate_text(self, seed):
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

    def get_text(self, address):
        return self.generate_text(address)

    @staticmethod
    def generate_random_address():
        room = random.randint(1, 100)
        wall = random.randint(1, 6)
        shelf = random.randint(1, 10)
        volume = random.randint(1, 10)
        book = random.randint(1, 100)
        page = random.randint(1, 1000)
        return f"Room{room}:Wall{wall}:Shelf{shelf}:Volume{volume}:Book{book}:Page{page}"

    @staticmethod
    def generate_address_with_pattern(pattern):
        room = pattern.get("room", random.randint(1, 100))
        wall = pattern.get("wall", random.randint(1, 6))
        shelf = pattern.get("shelf", random.randint(1, 10))
        volume = pattern.get("volume", random.randint(1, 10))
        book = pattern.get("book", random.randint(1, 100))
        page = pattern.get("page", random.randint(1, 1000))
        return f"Room{room}:Wall{wall}:Shelf{shelf}:Volume{volume}:Book{book}:Page{page}"

    def search_for_text_with_pattern(self, target_text, pattern=None, max_attempts=1000000):
        for _ in range(max_attempts):
            address = self.generate_address_with_pattern(pattern or {})
            text = self.get_text(address)
            if target_text in text:
                return address, text
        return None, None


def main():
    library = BabylonLibrary()

    target_text = "xxx"
    pattern = {"room": 42, "wall": 3}
    # pattern = None
    address, text = library.search_for_text_with_pattern(target_text, pattern, max_attempts=1000000)
    if address:
        print(f"Address found: {address}")
        print(f"Text on page: {text}")
    else:
        print(f"Text '{target_text}' not found.")
    # Address found: Room6:Wall2:Shelf4:Volume9:Book18:Page50


if __name__ == "__main__":
    main()
