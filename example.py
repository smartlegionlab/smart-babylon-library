"""
Example usage of Smart Babylon Library
"""
from smart_babylon_library import SmartBabylonLibrary, LibraryConfig
from smart_babylon_library.character_sets.alphabets import LatinAlphabet
from smart_babylon_library.character_sets.digits import Digits


def main():
    print("=== Smart Babylon Library Demo ===\n")

    library = SmartBabylonLibrary()

    book = library.get_book(floor=1, room=3, cabinet=2, shelf=5, book_number=42)
    print(f"Book: {book}")
    print(f"Book title length: {len(book.title)}")
    print(f"Pages in book: {book.max_pages}")

    custom_config = LibraryConfig(
        title_length_range=(10, 20),
        content_length_range=(100, 200),
        pages_per_book_range=(3, 5)
    )

    print(f"\n--- Custom config test ---")
    custom_library = SmartBabylonLibrary(custom_config)

    for i in range(3):
        custom_book = custom_library.get_book(floor=1, room=1, cabinet=1, shelf=1, book_number=i)
        page = custom_book.get_page(0)

        print(f"Book {i}:")
        print(f"  Title length: {len(custom_book.title)} (range: 10-20)")
        print(f"  Pages in book: {custom_book.max_pages} (range: 3-5)")
        print(f"  Page 0 length: {len(page.content)} (range: 100-200)")
        print()

    print(f"\n--- Custom character sets test ---")
    charset_config = LibraryConfig(
        title_length_range=(5, 15),
        content_length_range=(50, 150),
        character_sets=[LatinAlphabet(), Digits()]
    )

    charset_library = SmartBabylonLibrary(charset_config)
    charset_book = charset_library.get_book(floor=1, room=1, cabinet=1, shelf=1, book_number=1)
    print(f"Custom charset book title: {charset_book.title}")
    print(f"Title contains only Latin/digits: "
          f"{all(c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ' for c in charset_book.title)}")

    coordinates_dict = book.coordinates.to_dict()
    print(f"\nCoordinates as dict: {coordinates_dict}")

    book_json = book.to_json()
    print(f"\nBook as JSON (first 200 chars): {book_json[:200]}...")


if __name__ == "__main__":
    main()
