import hashlib
import random
import string
from typing import Optional, Dict, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed


RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


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
            # If no coordinates, return the full text
            full_text = self.generate_text(address)
            return full_text
        elif len(parts) == 8:
            # If coordinates are provided, return a substring
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

    # Example 1: Get text by address
    address = "Room1:Wall1:Shelf1:Volume1:Book1:Page1"
    text = library.get_text(address)
    print(f"Text at address {address}:\n{text}\n")

    # Example 2: Get text by address with coordinates
    address_with_coords = "Room1:Wall1:Shelf1:Volume1:Book1:Page1:10:20"
    partial_text = library.get_text(address_with_coords)
    print(f"Text at address {address_with_coords}:\n{partial_text}\n")

    # Example 3: Search for text
    target_text = "xxx"
    found_address, found_coords = library.search_for_text_with_pattern(target_text, max_attempts=1000)
    if found_address:
        print(f"Text '{target_text}' found at address {found_address}:\n{library.get_text(found_address)}\n")
    else:
        print(f"Text '{target_text}' not found in 1000 attempts.\n")

    # Example 4: Iterate using the iterator
    print("Iterating through the library:")
    iterator = BabylonLibraryIterator(library)
    for _ in range(5):
        address, text = next(iterator)
        print(f"Address: {address}\nText: {text[:50]}...\n")

    # Example: Parallel search
    target_text = "xxx"
    found_address, found_coords = library.search_for_text_with_pattern_parallel(target_text, max_attempts=1000,
                                                                                num_threads=4)
    if found_address:
        print(f"Text '{target_text}' found at address {found_address}:\n{library.get_text(found_address)}\n")
    else:
        print(f"Text '{target_text}' not found in 1000 attempts.\n")


if __name__ == '__main__':
    main()
