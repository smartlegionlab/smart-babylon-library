# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smart_babylon_library.babylon_library import BabylonLibrary, BabylonLibraryIterator


def test_babylon_library_generate_text():
    library = BabylonLibrary()
    seed = "test_seed"
    text = library.generate_text(seed)
    assert isinstance(text, str)
    assert len(text) == library.page_length


def test_babylon_library_get_text():
    library = BabylonLibrary()
    address = "Room1:Wall1:Shelf1:Volume1:Book1:Page1"
    text = library.get_text(address)
    assert isinstance(text, str)
    assert len(text) == library.page_length


def test_babylon_library_generate_random_address():
    library = BabylonLibrary()
    address = library.generate_random_address()
    assert isinstance(address, str)
    assert address.count(":") == 5


def test_babylon_library_search_for_text_with_pattern():
    library = BabylonLibrary()
    target_text = "test"
    result = library.search_for_text_with_pattern(target_text, max_attempts=100)
    assert result in [(None, None), (str, tuple)]


def test_babylon_library_iterator():
    library = BabylonLibrary()
    iterator = BabylonLibraryIterator(library)
    address, text = next(iterator)
    assert isinstance(address, str)
    assert isinstance(text, str)
