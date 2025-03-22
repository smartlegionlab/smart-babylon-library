# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smart_babylon_library import LibraryStructure, TextEncoder
from smart_babylon_library.babylon_library import BabylonLibrary
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
    random_address = library.generate_random_address()
    print(f"Random address: {random_address}")

    text = library.get_text(random_address)
    print(f"Text on page ({len(text)} symbols): {text}")

    same_text = library.get_text(random_address)
    print(f"Text on the same page ({len(same_text)} symbols): {same_text}...")


def main():
    print("*** Start ***")
    text = "i love python"
    print(f"Original text: '{text}'")
    print(f"Text length: {len(text)} characters\n")
    text_encoder_example(text)
    library_structure_example(text)
    babylon_library_example()
    print("*** End ***")
    library = BabylonLibrary()

    target_text = "xxx"
    pattern = {"room": 42, "wall": 3}
    # pattern = None
    address, text = library.search_for_text_with_pattern(target_text, pattern, max_attempts=1000000)
    if address:
        print(f"Address found: {address}")
        print(f"Text on page: {text}")
    else:
        print(f"Text '{target_text}' not found.")
    # Address found: Room6:Wall2:Shelf4:Volume9:Book18:Page50


if __name__ == "__main__":
    main()
