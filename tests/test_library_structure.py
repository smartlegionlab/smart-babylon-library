# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smart_babylon_library.library_structure import LibraryStructure


def test_library_structure_encode_text_to_address():
    library = LibraryStructure()
    text = "test text"
    address = library.encode_text_to_address(text)
    assert isinstance(address, str)
    assert address.count(":") == 4


def test_library_structure_decode_address_to_text():
    library = LibraryStructure()
    text = "test text"
    address = library.encode_text_to_address(text)
    decoded_text = library.decode_address_to_text(address)
    assert isinstance(decoded_text, str)
    assert decoded_text.strip() == text


def test_library_structure_normalize_text():
    library = LibraryStructure()
    text = "test text"
    normalized_text = library._normalize_text(text)
    assert isinstance(normalized_text, str)
    assert len(normalized_text) == library.max_page_content_length


def test_library_structure_text_to_number():
    library = LibraryStructure()
    text = "test"
    number = library._text_to_number(text)
    assert isinstance(number, int)


def test_library_structure_number_to_base():
    library = LibraryStructure()
    number = 12345
    base = 36
    result = library._number_to_base(number, base)
    assert isinstance(result, str)
