import random
import string


class Library:
    def __init__(self, charset='abcdefghijklmnopqrstuvwxyz, .',
                 max_page_content_length=3200, max_walls=4,
                 max_shelves=5, max_volumes=32, max_pages=410,
                 hexagon_base=36):
        self.charset = charset
        self.charset_length = len(charset)
        self.max_page_content_length = max_page_content_length
        self.max_walls = max_walls
        self.max_shelves = max_shelves
        self.max_volumes = max_volumes
        self.max_pages = max_pages
        self.hexagon_base = hexagon_base

    def generate_library_coordinate(self):
        wall = str(random.randint(1, self.max_walls))
        shelf = str(random.randint(1, self.max_shelves))
        volume = str(random.randint(1, self.max_volumes)).zfill(2)
        page = str(random.randint(1, self.max_pages)).zfill(3)
        return int(page + volume + shelf + wall)

    def search_by_content(self, text, library_coordinate):
        text = self._sanitize_text(text)
        sum_value = self._calculate_sum_value(text)
        result = library_coordinate * (self.charset_length ** self.max_page_content_length) + sum_value
        return self._convert_to_base(result, self.hexagon_base)

    def search_by_address(self, address):
        hexagon_address, wall, shelf, volume, page = address.split(':')
        volume = volume.zfill(2)
        page = page.zfill(3)
        library_coordinate = int(page + volume + shelf + wall)

        seed = int(hexagon_address, self.hexagon_base) - library_coordinate * (self.charset_length ** self.max_page_content_length)
        hexagon_base_result = self._convert_to_base(seed, self.hexagon_base)
        result = self._convert_to_base(int(hexagon_base_result, self.hexagon_base), self.charset_length)

        return self._pad_or_trim_result(result)

    def _sanitize_text(self, text):
        return ''.join([c for c in text.lower() if c in self.charset]).rstrip().ljust(self.max_page_content_length, ' ')

    def _calculate_sum_value(self, text):
        sum_value = 0
        for i, c in enumerate(text[::-1]):
            char_value = ord(c) - ord('a') if c.isalpha() else 28 if c == '.' else 27
            sum_value += char_value * (self.charset_length ** i)
        return sum_value

    def _pad_or_trim_result(self, result):
        if len(result) < self.max_page_content_length:
            random.seed(result)
            while len(result) < self.max_page_content_length:
                result += self.charset[int(random.random() * len(self.charset))]
        elif len(result) > self.max_page_content_length:
            result = result[-self.max_page_content_length:]
        return result

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
            return string.digits + 'abcdefghijklmnopqrstuvwxyz'
        elif base == 10:
            return '0123456789'
        elif base == 60:
            return '0123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        else:
            return self.charset


def main():
    library = Library()

    text_to_search = "Test"
    library_coordinate = library.generate_library_coordinate()
    hexagon_result = library.search_by_content(text_to_search, library_coordinate)

    print(f"Address for text '{text_to_search}': {hexagon_result}")
    wall = "1"
    shelf = "01"
    volume = "01"
    page = "001"

    address = f"{hexagon_result}:{wall}:{shelf}:{volume}:{page}"

    content_result = library.search_by_address(address)

    print(f"Contents at address '{address}': {content_result}")


if __name__ == '__main__':
    main()
