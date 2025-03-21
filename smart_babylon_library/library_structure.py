# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import string

from smart_babylon_library.config import (
    CHARSET,
    MAX_PAGE_CONTENT_LENGTH,
    NUM_WALLS,
    NUM_SHELVES,
    NUM_VOLUMES,
    NUM_PAGES,
    HEXAGON_BASE
)


class LibraryStructure:
    def __init__(
            self,
            charset=CHARSET,
            max_page_content_length=MAX_PAGE_CONTENT_LENGTH,
            num_walls=NUM_WALLS,
            num_shelves=NUM_SHELVES,
            num_volumes=NUM_VOLUMES,
            num_pages=NUM_PAGES,
            hexagon_base=HEXAGON_BASE
    ):
        self.charset = charset
        self.charset_length = len(self.charset)
        self.max_page_content_length = max_page_content_length
        self.num_walls = num_walls
        self.num_shelves = num_shelves
        self.num_volumes = num_volumes
        self.num_pages = num_pages
        self.hexagon_base = hexagon_base

    @staticmethod
    def _format_coordinate(page, volume, shelf, wall):
        return int(page.zfill(3) + volume.zfill(2) + shelf + wall)

    def encode_text_to_address(self, text, wall="1", shelf="01", volume="01", page="001"):
        text = self._normalize_text(text)
        sum_value = self._text_to_number(text)
        library_coordinate = self._format_coordinate(page, volume, shelf, wall)
        result = library_coordinate * (self.charset_length ** self.max_page_content_length) + sum_value
        hexagon_result = self._number_to_base(result, self.hexagon_base)

        return f"{hexagon_result}:{wall}:{shelf}:{volume}:{page}"

    def decode_address_to_text(self, address):
        hexagon_address, wall, shelf, volume, page = address.split(':')
        library_coordinate = self._format_coordinate(page, volume, shelf, wall)

        seed = int(hexagon_address, self.hexagon_base) - library_coordinate * (
                    self.charset_length ** self.max_page_content_length)
        hexagon_base_result = self._number_to_base(seed, self.hexagon_base)
        result = self._number_to_base(int(hexagon_base_result, self.hexagon_base), self.charset_length)

        return self._pad_or_trim_result(result)

    def _normalize_text(self, text):
        return ''.join(c for c in text if c in self.charset).rstrip().ljust(self.max_page_content_length, ' ')

    def _text_to_number(self, text):
        return sum(self.charset.index(c) * (self.charset_length ** i) for i, c in enumerate(text[::-1]))

    def _pad_or_trim_result(self, result):
        return result.ljust(self.max_page_content_length)[:self.max_page_content_length].rstrip()

    def _number_to_base(self, x, base):
        digs = self._get_base_symbols(base)
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

    def _get_base_symbols(self, base):
        if base == 36:
            return string.digits + string.ascii_lowercase
        elif base == 10:
            return string.digits
        elif base == 60:
            return string.digits + string.ascii_uppercase + string.ascii_lowercase
        else:
            return self.charset
