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
                index = int(hash_value[i:i+2], 16) % len(self.charset)
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
