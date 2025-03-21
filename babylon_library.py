import hashlib
import random
import string

RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


class BabylonLibrary:
    def __init__(self):
        self.charset = string.ascii_letters + string.digits + string.punctuation + " " + RU

    def generate_text(self, seed, length=100):
        hash_value = hashlib.sha256(seed.encode()).hexdigest()
        text = []
        for i in range(0, len(hash_value), 2):
            index = int(hash_value[i:i+2], 16) % len(self.charset)
            text.append(self.charset[index])
            if len(text) >= length:
                break
        return ''.join(text)

    def get_text(self, room, wall, shelf, volume, book, page):
        seed = f"{room}:{wall}:{shelf}:{volume}:{book}:{page}"
        return self.generate_text(seed)

    @staticmethod
    def generate_random_address():
        room = random.randint(1, 100)
        wall = random.randint(1, 6)
        shelf = random.randint(1, 10)
        volume = random.randint(1, 10)
        book = random.randint(1, 100)
        page = random.randint(1, 1000)
        return room, wall, shelf, volume, book, page


def main():
    library = BabylonLibrary()

    random_address = library.generate_random_address()
    print(f"Random address: {random_address}")

    text = library.get_text(*random_address)
    print(f"Text on page: {text}")

    same_text = library.get_text(*random_address)
    print(f"Text on the same page: {same_text}")


if __name__ == '__main__':
    main()
