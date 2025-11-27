"""
Example usage of Smart Babylon Library
"""
from smart_babylon_library.library.core import SmartBabylonLibrary


def main():
    print("=== Smart Babylon Library Demo ===\n")

    library = SmartBabylonLibrary()

    book = library.get_book(floor=1, room=3, cabinet=2, shelf=5, book_number=42)
    print(f"Book: {book}")
    print(f"Book title: {book.title}")

    coordinates_dict = book.coordinates.to_dict()
    print(f"\nCoordinates as dict: {coordinates_dict}")

    coordinates_json = book.coordinates.to_json()
    print(f"Coordinates as JSON: {coordinates_json}")

    book_json = book.to_json()
    print(f"\nBook as JSON: {book_json}")

    print(f"\nPage access:")
    for page_num in [0, 1, 156]:
        page = book.get_page(page_num)
        print(f"  Page {page_num}: {page}")

    page_json = book.get_page_json(0)
    print(f"\nPage 0 as JSON: {page_json}")

    direct_book_json = library.get_book_json({
        'floor': 1, 'room': 3, 'cabinet': 2,
        'shelf': 5, 'book': 42, 'page': 0
    })
    print(f"\nDirect book JSON: {direct_book_json}")

    direct_page_json = library.get_page_json({
        'floor': 1, 'room': 3, 'cabinet': 2,
        'shelf': 5, 'book': 42, 'page': 777
    })
    print(f"Direct page JSON: {direct_page_json}")

if __name__ == "__main__":
    main()
