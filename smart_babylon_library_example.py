# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smart_babylon_library import timing_decorator
from smart_babylon_library.smart_babylon_library import SmartBabylonLibrary, SmartBabylonLibraryIterator


@timing_decorator
def example_get_book_text(library: SmartBabylonLibrary):
    print("\n=== Example: Get the full text of a book ===")
    book_address = "Room1:Wall1:Shelf1:Volume1:Book1"
    print(f"Book address: {book_address}")
    book_text = library.get_text(book_address)
    print("Full text of the book (first 100 characters):")
    print(book_text[:100])


@timing_decorator
def example_get_book_title(library: SmartBabylonLibrary):
    print("\n=== Example: Get the title of a book ===")
    book_address = "Room1:Wall1:Shelf1:Volume1:Book1"
    print(f"Book address: {book_address}")
    title = library.get_book_title(book_address)
    print(f"Title of the book: {title}")


@timing_decorator
def example_get_page_text(library: SmartBabylonLibrary):
    print("\n=== Example: Get the text of a specific page ===")
    page_address = "Room1:Wall1:Shelf1:Volume1:Book1:Page1"
    print(f"Page address: {page_address}")
    page_text = library.get_text(page_address)
    print("Page text (first 100 characters):")
    print(page_text[:100])


@timing_decorator
def example_get_slice_text(library: SmartBabylonLibrary):
    print("\n=== Example: Get a slice of text from a page ===")
    slice_address = "Room1:Wall1:Shelf1:Volume1:Book1:Page1:10:50"
    print(f"Slice address: {slice_address}")
    slice_text = library.get_text(slice_address)
    print(f"Slice of text (characters 10 to 50): {slice_text}")


@timing_decorator
def example_search_in_titles(library: SmartBabylonLibrary):
    print("\n=== Example: Search for text in book titles ===")
    target_text = "x"
    print(f"Searching for text '{target_text}' in book titles...")
    title_address = library.search_in_titles(target_text, max_attempts=1000)
    if title_address:
        print(f"Text '{target_text}' found in the title of the book at address: {title_address}")
    else:
        print(f"Text '{target_text}' not found in any book title.")


@timing_decorator
def example_search_in_library(library: SmartBabylonLibrary):
    print("\n=== Example: Search for text in the library ===")
    target_text = "x"
    print(f"Searching for text '{target_text}' in the library...")
    result = library.search_in_library(target_text, max_attempts=1000)
    if result:
        address, start, end = result
        print(f"Text '{target_text}' found at address: {address}, from position {start} to {end}.")
    else:
        print(f"Text '{target_text}' not found in the library.")


@timing_decorator
def example_iterate_library(library: SmartBabylonLibrary):
    print("\n=== Example: Iterate through the library (3 steps) ===")
    iterator = SmartBabylonLibraryIterator(library)
    for i, (address, title, text) in enumerate(iterator):
        if i >= 3:
            break
        print(f"Iteration {i + 1}:")
        print(f"Address: {address}")
        print(f"Title: {title}")
        print("Text (first 50 characters):")
        print(text[:50])
        print("-" * 50)


def main():
    library = SmartBabylonLibrary()

    example_get_book_text(library)
    example_get_book_title(library)
    example_get_page_text(library)
    example_get_slice_text(library)
    example_search_in_titles(library)
    example_search_in_library(library)
    example_iterate_library(library)


if __name__ == '__main__':
    main()
