# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smart_babylon_library import LibraryStructure, TextEncoder
from smart_babylon_library.babylon_lib_with_books import BabylonLibraryWithBooks
from smart_babylon_library.babylon_library import BabylonLibrary, BabylonLibraryIterator
from smart_babylon_library.tools import timeit


@timeit
def text_encoder_example(text):
    text_encoder = TextEncoder()
    print("=== Using TextEncoder ===")
    encoded_address = text_encoder.encode_text(text)
    print(f"Encoded address: {encoded_address}")
    print(f"Encoded address length: {len(encoded_address)} characters")

    decoded_text = text_encoder.decode_address(encoded_address)
    print(f"Decoded text: '{decoded_text}'")
    print(f"Decoded text length: {len(decoded_text)} characters")


@timeit
def library_structure_example(text):
    library_structure = LibraryStructure()
    print("=== Using LibraryStructure ===")
    full_address = library_structure.encode_text_to_address(text)
    print(f"Full library address: {full_address}")
    print(f"Full address length: {len(full_address)} characters")

    decoded_full_text = library_structure.decode_address_to_text(full_address)
    print(f"Decoded full text: '{decoded_full_text}'")
    print(f"Decoded full text length: {len(decoded_full_text)} characters")


@timeit
def babylon_library_example():
    library = BabylonLibrary()
    print("=== Using BabylonLibrary ===")
    # Example 1: Get text by address
    address = "Room1:Wall1:Shelf1:Volume1:Book1:Page1"
    text = library.get_text(address)
    print(f"Text at address {address}:\n{text}\n")

    # Example 2: Get text by address with coordinates
    address_with_coords = "Room1:Wall1:Shelf1:Volume1:Book1:Page1:10:20"
    partial_text = library.get_text(address_with_coords)
    print(f"Text at address {address_with_coords}:\n{partial_text}\n")

    # Example 3: Search for text
    target_text = "ok"
    found_address, found_coords = library.search_for_text_with_pattern(target_text, max_attempts=1000)
    if found_address:
        print(f"Text '{target_text}' found at address {found_address}:\n{library.get_text(found_address)}\n")
    else:
        print(f"Text '{target_text}' not found in 1000 attempts.\n")

    # Example 4: Iterate using the iterator
    print("=== Using BabylonLibraryIterator ===")
    print("Iterating through the library:")
    iterator = BabylonLibraryIterator(library)
    for _ in range(5):
        address, text = next(iterator)
        print(f"Address: {address}\nText: {text[:50]}...\n")

    # Example: Parallel search
    target_text = "ok"
    found_address, found_coords = library.search_for_text_with_pattern_parallel(target_text, max_attempts=1000,
                                                                                num_threads=4)
    if found_address:
        print(f"Text '{target_text}' found at address {found_address}:\n{library.get_text(found_address)}\n")
    else:
        print(f"Text '{target_text}' not found in 1000 attempts.\n")


@timeit
def babylon_library_with_books():
    # Create the library
    library = BabylonLibraryWithBooks()
    print("=== Using BabylonLibraryWithBooks ===")
    # Generate and add 5 books to the library
    for _ in range(5):
        book = library.generate_book(num_pages=10)
        address = library.add_book_to_library(book)
        print(f"Added book '{book['title']}' at address {address}")

    # Search for text in the library
    target_text = "hello"
    result = library.search_in_library(target_text)
    if result:
        address, start, end = result
        print(f"Text '{target_text}' found at address {address}, position {start}-{end}.")
    else:
        print(f"Text '{target_text}' not found in the library.")

    # Iterate over the library
    print("\nIterating through the library:")
    for address, title in library:
        print(f"Address: {address}, Title: {title}")
        print('-' * 50)
        print(library.get_text(address))


def main():
    print("*** Start ***")
    babylon_library_example()
    babylon_library_with_books()
    print('-' * 50)
    text = "i love python"
    print(f"Original text: '{text}'")
    print(f"Text length: {len(text)} characters\n")
    text_encoder_example(text)
    library_structure_example(text)
    print("*** End ***")


if __name__ == "__main__":
    main()
