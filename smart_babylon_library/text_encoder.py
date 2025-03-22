# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import string

from smart_babylon_library.config import RU


class TextEncoder:
    def __init__(self, charset=string.ascii_letters + string.digits + string.punctuation + " " + RU):
        self.charset = charset
        self.charset_length = len(self.charset)
        self.base62_chars = string.digits + string.ascii_letters

    def _sanitize_text(self, text: str) -> str:
        return ''.join(c for c in text if c in self.charset and c not in "!@#")

    def _text_to_num(self, text):
        number = 0
        for char in text:
            number = number * self.charset_length + self.charset.index(char)
        return number

    def _num_to_base62(self, number):
        if number == 0:
            return self.base62_chars[0]
        code = []
        while number > 0:
            code.append(self.base62_chars[number % 62])
            number //= 62
        return ''.join(reversed(code))

    def _base62_to_num(self, code):
        number = 0
        for char in code:
            number = number * 62 + self.base62_chars.index(char)
        return number

    def _num_to_text(self, number, text_length):
        text = []
        for _ in range(text_length):
            number, remainder = divmod(number, self.charset_length)
            text.append(self.charset[remainder])
        return ''.join(reversed(text))

    def encode_text(self, text):
        text = self._sanitize_text(text)
        number = self._text_to_num(text)
        code = self._num_to_base62(number)
        return f"{code}:{len(text)}"

    def decode_address(self, address):
        code, text_length = address.split(':')
        text_length = int(text_length)
        number = self._base62_to_num(code)
        return self._num_to_text(number, text_length)
