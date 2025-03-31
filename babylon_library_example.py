# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smart_babylon_library import timing_decorator, BabylonLibrary, BabylonLibraryIterator


@timing_decorator
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


def main():
    print("*** Start ***")
    babylon_library_example()
    print("*** End ***")


if __name__ == "__main__":
    main()
