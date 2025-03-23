import random
import string
from typing import List, Optional, Dict, Tuple, Iterator


class BabylonLibraryWithBooks:
    def __init__(
        self,
        charset: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" +
                       string.ascii_letters + string.digits,
        page_length: int = 3200,
        max_rooms: int = 100,
        max_walls: int = 6,
        max_shelves: int = 10,
        max_volumes: int = 10,
        max_books: int = 100,
        max_pages: int = 1000,
    ):
        self.charset = charset
        self.page_length = page_length
        self.max_rooms = max_rooms
        self.max_walls = max_walls
        self.max_shelves = max_shelves
        self.max_volumes = max_volumes
        self.max_books = max_books
        self.max_pages = max_pages

    def generate_word(self, seed: str, min_length: int = 1, max_length: int = 10) -> str:
        random.seed(seed)
        length = random.randint(min_length, max_length)

        first_char = random.choice(self.charset)

        if first_char.isalpha():
            if first_char in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
                charset = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
            else:
                charset = string.ascii_letters
        else:
            charset = string.digits

        word = first_char + ''.join(random.choice(charset) for _ in range(length - 1))
        return word

    def generate_sentence(self, seed: str) -> str:
        random.seed(seed)
        sentence_length = random.randint(5, 20)
        words = [self.generate_word(seed + str(i)) for i in range(sentence_length)]
        sentence = ' '.join(words).capitalize()
        sentence += random.choice(['.', '!', '?']) + ' '
        return sentence

    def generate_page(self, seed: str) -> str:
        random.seed(seed)
        page = []
        while len(''.join(page)) < self.page_length:
            sentence = self.generate_sentence(seed + str(len(page)))
            page.append(sentence)
        return ''.join(page)

    def generate_book_title(self, seed: str) -> str:
        random.seed(seed)
        if random.choice([True, False]):
            return self.generate_word(seed, min_length=3, max_length=10).capitalize()
        else:
            sentence = self.generate_sentence(seed).strip()
            return sentence[:-1]

    def generate_book(self, seed: str, num_pages: int) -> Dict[str, List[str]]:
        title = self.generate_book_title(seed + "title")
        pages = [self.generate_page(seed + "page" + str(i)) for i in range(num_pages)]
        return {"title": title, "pages": pages}

    def get_text(self, address: str, start: Optional[int] = None, end: Optional[int] = None) -> str:
        parts = address.split(':')
        if len(parts) == 5:
            seed = address
            book = self.generate_book(seed, self.max_pages)
            full_text = ''.join(book["pages"])
            return full_text[start:end] if start is not None and end is not None else full_text
        elif len(parts) == 6:
            seed = ':'.join(parts[:5])
            page_num = int(parts[5].replace("Page", "")) - 1
            book = self.generate_book(seed, self.max_pages)
            if 0 <= page_num < len(book["pages"]):
                page_text = book["pages"][page_num]
                return page_text[start:end] if start is not None and end is not None else page_text
            else:
                raise ValueError("Page number out of range.")
        elif len(parts) == 8:
            seed = ':'.join(parts[:5])
            page_num = int(parts[5].replace("Page", "")) - 1
            start = int(parts[6])
            end = int(parts[7])
            book = self.generate_book(seed, self.max_pages)
            if 0 <= page_num < len(book["pages"]):
                page_text = book["pages"][page_num]
                return page_text[start:end]
            else:
                raise ValueError("Page number out of range.")
        else:
            raise ValueError("Incorrect address format.")

    def search_in_library(self, target_text: str, max_attempts: int = 1000000) -> Optional[Tuple[str, int, int]]:
        for _ in range(max_attempts):
            address = self.generate_random_address()
            text = self.get_text(address)
            start_index = text.find(target_text)
            if start_index != -1:
                return address, start_index, start_index + len(target_text)
        return None

    def search_in_titles(self, target_text: str, max_attempts: int = 1000000) -> Optional[str]:
        for _ in range(max_attempts):
            address = self.generate_random_address()
            seed = ':'.join(address.split(':')[:5])
            book = self.generate_book(seed, self.max_pages)
            if target_text in book["title"]:
                return seed
        return None

    def generate_random_address(self) -> str:
        room = random.randint(1, self.max_rooms)
        wall = random.randint(1, self.max_walls)
        shelf = random.randint(1, self.max_shelves)
        volume = random.randint(1, self.max_volumes)
        book = random.randint(1, self.max_books)
        page = random.randint(1, self.max_pages)
        return f"Room{room}:Wall{wall}:Shelf{shelf}:Volume{volume}:Book{book}:Page{page}"

    def __iter__(self) -> Iterator[Tuple[str, str]]:
        self.current_room = 1
        self.current_wall = 1
        self.current_shelf = 1
        self.current_volume = 1
        self.current_book = 1
        self.current_page = 1
        return self

    def __next__(self) -> Tuple[str, str]:
        if self.current_page > self.max_pages:
            self.current_page = 1
            self.current_book += 1
            if self.current_book > self.max_books:
                self.current_book = 1
                self.current_volume += 1
                if self.current_volume > self.max_volumes:
                    self.current_volume = 1
                    self.current_shelf += 1
                    if self.current_shelf > self.max_shelves:
                        self.current_shelf = 1
                        self.current_wall += 1
                        if self.current_wall > self.max_walls:
                            self.current_wall = 1
                            self.current_room += 1
                            if self.current_room > self.max_rooms:
                                raise StopIteration

        address = f"Room{self.current_room}:Wall{self.current_wall}:Shelf{self.current_shelf}:Volume{self.current_volume}:Book{self.current_book}:Page{self.current_page}"
        book = self.generate_book(f"Room{self.current_room}:Wall{self.current_wall}:Shelf{self.current_shelf}:Volume{self.current_volume}:Book{self.current_book}", self.max_pages)
        page_text = book["pages"][self.current_page - 1]
        self.current_page += 1
        return address, page_text


def main():
    library = BabylonLibraryWithBooks()

    book_address = "Room1:Wall1:Shelf1:Volume1:Book1"
    book_text = library.get_text(book_address)
    print("Text of the entire book:", book_text[:100])

    page_address = "Room1:Wall1:Shelf1:Volume1:Book1:Page1"
    page_text = library.get_text(page_address)
    print("Page text1:", page_text[:100])

    slice_address = "Room1:Wall1:Shelf1:Volume1:Book1:Page1:10:50"
    slice_text = library.get_text(slice_address)
    print("Slicing text on a page 1:", slice_text)

    title_address = library.search_in_titles("а")
    if title_address:
        print(f"Found in the title of the book: {title_address}")

    result = library.search_in_library("а")
    if result:
        address, start, end = result
        print(f"Found at address: {address}, с {start} по {end}")

    for address, text in library:
        print(f"Address: {address}, Text: {text[:50]}...")


if __name__ == '__main__':
    main()
