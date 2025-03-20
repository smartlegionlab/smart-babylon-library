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

from smart_babylon_library.config import (
    CHARSET,
    MAX_PAGE_CONTENT_LENGTH,
    MAX_WALLS,
    MAX_SHELVES,
    MAX_VOLUMES,
    MAX_PAGES,
    HEXAGON_BASE
)


class BabylonLibrary:
    def __init__(
            self,
            charset=CHARSET,
            max_page_content_length=MAX_PAGE_CONTENT_LENGTH,
            max_walls=MAX_WALLS,
            max_shelves=MAX_SHELVES,
            max_volumes=MAX_VOLUMES,
            max_pages=MAX_PAGES,
            hexagon_base=HEXAGON_BASE
    ):
        self.charset = charset
        self.charset_length = len(self.charset)
        self.max_page_content_length = max_page_content_length
        self.max_walls = max_walls
        self.max_shelves = max_shelves
        self.max_volumes = max_volumes
        self.max_pages = max_pages
        self.hexagon_base = hexagon_base

    @staticmethod
    def _format_library_coordinate(page, volume, shelf, wall):
        return int(page.zfill(3) + volume.zfill(2) + shelf + wall)

    def generate_library_coordinate(self):
        wall = str(random.randint(1, self.max_walls))
        shelf = str(random.randint(1, self.max_shelves))
        volume = str(random.randint(1, self.max_volumes)).zfill(2)
        page = str(random.randint(1, self.max_pages)).zfill(3)
        return int(page + volume + shelf + wall)

    def search_by_content(self, text, wall="1", shelf="01", volume="01", page="001"):
        text = self._sanitize_text(text)
        sum_value = self._calculate_sum_value(text)
        library_coordinate = self._format_library_coordinate(page, volume, shelf, wall)
        result = library_coordinate * (self.charset_length ** self.max_page_content_length) + sum_value
        hexagon_result = self._convert_to_base(result, self.hexagon_base)

        return f"{hexagon_result}:{wall}:{shelf}:{volume}:{page}"

    def search_by_address(self, address):
        hexagon_address, wall, shelf, volume, page = address.split(':')
        library_coordinate = self._format_library_coordinate(page, volume, shelf, wall)

        seed = int(hexagon_address, self.hexagon_base) - library_coordinate * (
                    self.charset_length ** self.max_page_content_length)
        hexagon_base_result = self._convert_to_base(seed, self.hexagon_base)
        result = self._convert_to_base(int(hexagon_base_result, self.hexagon_base), self.charset_length)

        return self._pad_or_trim_result(result)

    def _sanitize_text(self, text):
        return ''.join(c for c in text if c in self.charset).rstrip().ljust(self.max_page_content_length, ' ')

    def _calculate_sum_value(self, text):
        return sum(self.charset.index(c) * (self.charset_length ** i) for i, c in enumerate(text[::-1]))

    def _pad_or_trim_result(self, result):
        return result.ljust(self.max_page_content_length)[:self.max_page_content_length].rstrip()

    def _convert_to_base(self, x, base):
        digs = self._get_digits(base)
        if x < 0:
            sign = -1
        elif x == 0:
            return digs[0]
        else:
            sign = 1

        x *= sign
        chars = []
        while x:
            chars.append(digs[x % base])
            x //= base
        if sign < 0:
            chars.append('-')
        chars.reverse()
        return ''.join(chars)

    def _get_digits(self, base):
        if base == 36:
            return string.digits + string.ascii_lowercase
        elif base == 10:
            return string.digits
        elif base == 60:
            return string.digits + string.ascii_uppercase + string.ascii_lowercase
        else:
            return self.charset
