import string

RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


class BabylonLibrary:
    def __init__(self, charset=string.ascii_letters + string.digits + string.punctuation + " " + RU):
        self.charset = charset
        self.charset_length = len(self.charset)

    def _sanitize_text(self, text):
        return ''.join(c for c in text if c in self.charset)

    def _text_to_number(self, text):
        number = 0
        for char in text:
            number = number * self.charset_length + self.charset.index(char)
        return number

    def _number_to_code(self, number):
        if number == 0:
            return '0'
        digits = string.digits + string.ascii_lowercase
        code = []
        while number > 0:
            code.append(digits[number % 36])
            number //= 36
        return ''.join(reversed(code))

    def _code_to_number(self, code):
        digits = string.digits + string.ascii_lowercase
        number = 0
        for char in code:
            number = number * 36 + digits.index(char)
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
        code = self._number_to_code(number)
        return f"{code}:{len(text)}"

    def search_by_address(self, address):
        code, text_length = address.split(':')
        text_length = int(text_length)
        number = self._code_to_number(code)
        return self._number_to_text(number, text_length)


def main():
    library = BabylonLibrary()

    text = "Hello World!"
    address = library.search_by_content(text)
    print(f"Address for text: {address}")
    print(f'Address length: {len(address)}')

    retrieved_text = library.search_by_address(address)
    print(f"Text at address: '{retrieved_text}'")


if __name__ == "__main__":
    main()
