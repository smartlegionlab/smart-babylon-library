# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smart_babylon_library import LibraryStructure, TextEncoder
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


def main():
    print("*** Start ***")
    text = "i love python"
    print(f"Original text: '{text}'")
    print(f"Text length: {len(text)} characters\n")
    text_encoder_example(text)
    library_structure_example(text)
    print("*** End ***")


if __name__ == "__main__":
    main()
