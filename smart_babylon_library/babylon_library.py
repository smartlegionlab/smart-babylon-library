# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import string


class BabylonLibrary:
    def __init__(self, charset=string.ascii_letters + string.digits + string.punctuation + " "):
        self.charset = charset
        self.charset_length = len(self.charset)

    def _sanitize_text(self, text):
        return ''.join(c for c in text if c in self.charset)

    def _text_to_number(self, text):
        number = 0
        for i, char in enumerate(text[::-1]):
            number += self.charset.index(char) * (self.charset_length ** i)
        return number

    def _number_to_text(self, number, text_length):
        text = []
        for _ in range(text_length):
            number, remainder = divmod(number, self.charset_length)
            text.append(self.charset[remainder])
        return ''.join(reversed(text))

    def search_by_content(self, text):
        text = self._sanitize_text(text)
        number = self._text_to_number(text)
        return f"{number}:{len(text)}"

    def search_by_address(self, address):
        number, text_length = address.split(':')
        number = int(number)
        text_length = int(text_length)
        return self._number_to_text(number, text_length)


def main():
    library = BabylonLibrary()

    text = "Hello, Babylon!"
    address = library.search_by_content(text)
    print(f"Address for text: {address}")
    print(f'Address length: {len(address)}')

    retrieved_text = library.search_by_address(address)
    print(f"Text at address: '{retrieved_text}'")


if __name__ == "__main__":
    main()
