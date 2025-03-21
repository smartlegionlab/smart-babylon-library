import string

RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


class BabylonLibrary:
    def __init__(self, charset=string.ascii_letters + string.digits + string.punctuation + " " + RU):
        self.charset = charset
        self.charset_length = len(self.charset)
        self.base62_chars = string.digits + string.ascii_letters

    def _sanitize_text(self, text):
        return ''.join(c for c in text if c in self.charset)

    def _text_to_number(self, text):
        number = 0
        for char in text:
            number = number * self.charset_length + self.charset.index(char)
        return number

    def _number_to_base62(self, number):
        if number == 0:
            return self.base62_chars[0]
        code = []
        while number > 0:
            code.append(self.base62_chars[number % 62])
            number //= 62
        return ''.join(reversed(code))

    def _base62_to_number(self, code):
        number = 0
        for char in code:
            number = number * 62 + self.base62_chars.index(char)
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
        code = self._number_to_base62(number)
        return f"{code}:{len(text)}"

    def search_by_address(self, address):
        code, text_length = address.split(':')
        text_length = int(text_length)
        number = self._base62_to_number(code)
        return self._number_to_text(number, text_length)


def main():
    library = BabylonLibrary()

    text = "Hello world!"
    print(f'String: {text}')
    print(f'String length: {len(text)}')
    address = library.search_by_content(text)
    print(f"Address for text: {address}")
    print(f'Address length: {len(address)}')

    retrieved_text = library.search_by_address(address)
    print(f"Text at address: '{retrieved_text}'")


if __name__ == "__main__":
    main()
