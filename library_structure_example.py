# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smart_babylon_library import LibraryStructure
from smart_babylon_library.tools import timing_decorator


@timing_decorator
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
    print('-' * 50)
    text = "i love python"
    print(f"Original text: '{text}'")
    print(f"Text length: {len(text)} characters\n")
    library_structure_example(text)
    print("*** End ***")


if __name__ == "__main__":
    main()
