"""
Example usage of Smart Babylon Library with config
"""
from smart_babylon_library import SmartBabylonLibrary, LibraryConfig


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

    coordinates_dict = book.coordinates.to_dict()
    print(f"Coordinates as dict: {coordinates_dict}")

    book_json = book.to_json()
    print(f"\nBook as JSON (first 200 chars): {book_json[:200]}...")

if __name__ == "__main__":
    main()
