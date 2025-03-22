import hashlib
import random
import string
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Optional, Dict, Tuple


RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


class BookGenerator:
    def __init__(
        self,
        charset: str = RU + string.ascii_letters + string.digits + string.punctuation + ' ',
        min_word_length: int = 1,
        max_word_length: int = 15,
        max_sentences_per_paragraph: int = 10,
        max_paragraphs_per_page: int = 5,
        page_length: int = 3200,
    ):
        self.charset = charset
        self.min_word_length = min_word_length
        self.max_word_length = max_word_length
        self.max_sentences_per_paragraph = max_sentences_per_paragraph
        self.max_paragraphs_per_page = max_paragraphs_per_page
        self.page_length = page_length

    def generate_word(self) -> str:
        length = random.randint(self.min_word_length, self.max_word_length)
        return ''.join(random.choice(self.charset) for _ in range(length))

    def generate_sentence(self) -> str:
        sentence_length = random.randint(5, 20)  # Number of words in a sentence
        words = [self.generate_word() for _ in range(sentence_length)]
        sentence = ' '.join(words).capitalize()
        sentence += random.choice(['.', '!', '?'])
        return sentence

    def generate_paragraph(self) -> str:
        paragraph_length = random.randint(3, self.max_sentences_per_paragraph)
        sentences = [self.generate_sentence() for _ in range(paragraph_length)]
        return ' '.join(sentences)

    def generate_page(self) -> str:
        page = []
        while len(''.join(page)) < self.page_length:
            paragraph = self.generate_paragraph()
            page.append(paragraph)
            if len(page) >= self.max_paragraphs_per_page:
                break
        return '\n\n'.join(page)

    def generate_book(self, num_pages: int, title: Optional[str] = None) -> Dict[str, List[str]]:
        if title is None:
            title = self.generate_word()  # Generate a random title
        pages = [self.generate_page() for _ in range(num_pages)]
        return {"title": title, "pages": pages}

    def search_in_book(self, book: Dict[str, List[str]], target_text: str) -> Optional[Tuple[str, int, int, int]]:
        for page_index, page in enumerate(book["pages"]):
            start_index = page.find(target_text)
            if start_index != -1:
                return book["title"], page_index, start_index, start_index + len(target_text)
        return None

    def search_by_title(self, books: List[Dict[str, List[str]]], title: str) -> Optional[Dict[str, List[str]]]:
        for book in books:
            if book["title"] == title:
                return book
        return None


class BabylonLibrary:
    def __init__(
        self,
        charset: str = RU + string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation + ' ',
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

    def generate_text(self, seed: str) -> str:
        hash_value = hashlib.sha256(seed.encode()).hexdigest()
        text = []
        while len(text) < self.page_length:
            for i in range(0, len(hash_value), 2):
                index = int(hash_value[i:i + 2], 16) % len(self.charset)
                text.append(self.charset[index])
                if len(text) >= self.page_length:
                    break
            hash_value = hashlib.sha256(hash_value.encode()).hexdigest()
        return ''.join(text)

    def get_text(self, address: str) -> str:
        parts = address.split(':')
        if len(parts) == 6:
            full_text = self.generate_text(address)
            return full_text
        elif len(parts) == 8:
            full_text = self.generate_text(':'.join(parts[:6]))
            start = int(parts[6])
            end = int(parts[7])
            if start > end:
                start = 0
            if end > self.page_length:
                end = self.page_length
            return full_text[start:end]
        else:
            raise ValueError("Incorrect address format.")

    def generate_random_address(self) -> str:
        return self.generate_address_with_pattern()

    def generate_address_with_pattern(
        self, pattern: Optional[Dict[str, int]] = None, coordinates: Optional[Tuple[int, int]] = None
    ) -> str:
        if pattern is None:
            pattern = {}
        room = pattern.get("room", random.randint(1, self.max_rooms))
        wall = pattern.get("wall", random.randint(1, self.max_walls))
        shelf = pattern.get("shelf", random.randint(1, self.max_shelves))
        volume = pattern.get("volume", random.randint(1, self.max_volumes))
        book = pattern.get("book", random.randint(1, self.max_books))
        page = pattern.get("page", random.randint(1, self.max_pages))
        address = f"Room{room}:Wall{wall}:Shelf{shelf}:Volume{volume}:Book{book}:Page{page}"
        if coordinates:
            start, end = coordinates
            address += f":{start}:{end}"
        return address

    def search_for_text_with_pattern(
        self, target_text: str, pattern: Optional[Dict[str, int]] = None, max_attempts: int = 1000000
    ) -> Tuple[Optional[str], Optional[Tuple[int, int]]]:
        for _ in range(max_attempts):
            address = self.generate_address_with_pattern(pattern)
            text = self.get_text(address)
            start_index = text.find(target_text)
            if start_index != -1:
                end_index = start_index + len(target_text)
                address_with_coords = f"{address}:{start_index}:{end_index}"
                return address_with_coords, (start_index, end_index)
        return None, None

    def generate_next_address(self, current_address: str) -> str:
        parts = current_address.split(':')
        room = int(parts[0].replace("Room", ""))
        wall = int(parts[1].replace("Wall", ""))
        shelf = int(parts[2].replace("Shelf", ""))
        volume = int(parts[3].replace("Volume", ""))
        book = int(parts[4].replace("Book", ""))
        page = int(parts[5].replace("Page", ""))

        page += 1
        if page > self.max_pages:
            page = 1
            book += 1
            if book > self.max_books:
                book = 1
                volume += 1
                if volume > self.max_volumes:
                    volume = 1
                    shelf += 1
                    if shelf > self.max_shelves:
                        shelf = 1
                        wall += 1
                        if wall > self.max_walls:
                            wall = 1
                            room += 1
                            if room > self.max_rooms:
                                room = 1

        return f"Room{room}:Wall{wall}:Shelf{shelf}:Volume{volume}:Book{book}:Page{page}"

    def generate_previous_address(self, current_address: str) -> str:
        parts = current_address.split(':')
        room = int(parts[0].replace("Room", ""))
        wall = int(parts[1].replace("Wall", ""))
        shelf = int(parts[2].replace("Shelf", ""))
        volume = int(parts[3].replace("Volume", ""))
        book = int(parts[4].replace("Book", ""))
        page = int(parts[5].replace("Page", ""))

        page -= 1
        if page < 1:
            page = self.max_pages
            book -= 1
            if book < 1:
                book = self.max_books
                volume -= 1
                if volume < 1:
                    volume = self.max_volumes
                    shelf -= 1
                    if shelf < 1:
                        shelf = self.max_shelves
                        wall -= 1
                        if wall < 1:
                            wall = self.max_walls
                            room -= 1
                            if room < 1:
                                room = self.max_rooms

        return f"Room{room}:Wall{wall}:Shelf{shelf}:Volume{volume}:Book{book}:Page{page}"

    def search_for_text_with_pattern_parallel(
            self, target_text: str, pattern: Optional[Dict[str, int]] = None, max_attempts: int = 1000000,
            num_threads: int = 4
    ) -> Tuple[Optional[str], Optional[Tuple[int, int]]]:

        def search_task():
            address = self.generate_address_with_pattern(pattern)
            text = self.get_text(address)
            start_index = text.find(target_text)
            if start_index != -1:
                return address, (start_index, start_index + len(target_text))
            return None

        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(search_task) for _ in range(max_attempts)]
            for future in as_completed(futures):
                result = future.result()
                if result:
                    address, coords = result
                    address_with_coords = f"{address}:{coords[0]}:{coords[1]}"
                    return address_with_coords, coords

        return None, None


class BabylonLibraryIterator:
    def __init__(self, library: BabylonLibrary, start_address: Optional[str] = None):
        self.library = library
        self.current_address = start_address or library.generate_address_with_pattern(
            {"room": 1, "wall": 1, "shelf": 1, "volume": 1, "book": 1, "page": 1}
        )

    def __iter__(self):
        return self

    def __next__(self) -> Tuple[str, str]:
        address = self.current_address
        text = self.library.get_text(address)
        self.current_address = self.library.generate_next_address(self.current_address)
        return address, text


def main():
    library = BabylonLibrary()
    #
    # # Example 1: Get text by address
    # address = "Room1:Wall1:Shelf1:Volume1:Book1:Page1"
    # text = library.get_text(address)
    # print(f"Text at address {address}:\n{text}\n")
    #
    # # Example 2: Get text by address with coordinates
    # address_with_coords = "Room1:Wall1:Shelf1:Volume1:Book1:Page1:10:20"
    # partial_text = library.get_text(address_with_coords)
    # print(f"Text at address {address_with_coords}:\n{partial_text}\n")
    #
    # # Example 3: Search for text
    # target_text = "xxx"
    # found_address, found_coords = library.search_for_text_with_pattern(target_text, max_attempts=1000)
    # if found_address:
    #     print(f"Text '{target_text}' found at address {found_address}:\n{library.get_text(found_address)}\n")
    # else:
    #     print(f"Text '{target_text}' not found in 1000 attempts.\n")
    #
    # # Example 4: Iterate using the iterator
    # print("Iterating through the library:")
    # iterator = BabylonLibraryIterator(library)
    # for _ in range(5):
    #     address, text = next(iterator)
    #     print(f"Address: {address}\nText: {text[:50]}...\n")
    #
    # # Example: Parallel search
    # target_text = "xxx"
    # found_address, found_coords = library.search_for_text_with_pattern_parallel(target_text, max_attempts=1000,
    #                                                                             num_threads=4)
    # if found_address:
    #     print(f"Text '{target_text}' found at address {found_address}:\n{library.get_text(found_address)}\n")
    # else:
    #     print(f"Text '{target_text}' not found in 1000 attempts.\n")

    # Create a book generator
    # book_gen = BookGenerator()
    #
    # # Generate a book with 5 pages
    # book = book_gen.generate_book(num_pages=5, title="My First Book")
    #
    # # Print the book's title and first page
    # print(f"Book Title: {book['title']}")
    # print("First page of the book:")
    # print(book["pages"][0])
    #
    # # Search for a word in the book
    # target_text = "hello"
    # result = book_gen.search_in_book(book, target_text)
    # if result:
    #     title, page_index, start, end = result
    #     print(f"Text '{target_text}' found in book '{title}', page {page_index + 1}, position {start}-{end}.")
    # else:
    #     print(f"Text '{target_text}' not found in the book.")
    #
    # # Search for a book by title
    # books = [book_gen.generate_book(num_pages=3) for _ in range(5)]  # Generate 5 random books
    # search_title = books[2]["title"]  # Search for the third book's title
    # found_book = book_gen.search_by_title(books, search_title)
    # if found_book:
    #     print(f"Book found: {found_book['title']}")
    # else:
    #     print(f"Book with title '{search_title}' not found.")


if __name__ == '__main__':
    main()
