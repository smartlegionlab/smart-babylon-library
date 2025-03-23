# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import string

import pytest

from smart_babylon_library.smart_babylon_library import SmartBabylonLibrary, SmartBabylonLibraryIterator


@pytest.fixture
def library():
    return SmartBabylonLibrary(
        charset="абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" +
                string.ascii_letters + string.digits,
        page_length=100,
        max_rooms=2,
        max_walls=2,
        max_shelves=2,
        max_volumes=2,
        max_books=2,
        max_pages=2,
    )


def test_generate_word(library):
    seed = "test_seed"
    word = library.generate_word(seed)
    assert isinstance(word, str)
    assert len(word) > 0


def test_generate_sentence(library):
    seed = "test_seed"
    sentence = library.generate_sentence(seed)
    assert isinstance(sentence, str)
    assert len(sentence) > 0
    assert sentence.strip()[-1] in [".", "!", "?"]


def test_generate_page(library):
    seed = "test_seed"
    page = library.generate_page(seed)
    assert isinstance(page, str)
    assert len(page) >= library.page_length


def test_generate_book_title(library):
    seed = "test_seed"
    title = library.generate_book_title(seed)
    assert isinstance(title, str)
    assert len(title) > 0


def test_generate_book(library):
    seed = "test_seed"
    book = library.generate_book(seed, num_pages=2)
    assert isinstance(book, dict)
    assert "title" in book
    assert "pages" in book
    assert isinstance(book["title"], str)
    assert isinstance(book["pages"], list)
    assert len(book["pages"]) == 2


def test_get_text_full_book(library):
    address = "Room1:Wall1:Shelf1:Volume1:Book1"
    text = library.get_text(address)
    assert isinstance(text, str)
    assert len(text) > 0


def test_get_text_single_page(library):
    address = "Room1:Wall1:Shelf1:Volume1:Book1:Page1"
    text = library.get_text(address)
    assert isinstance(text, str)
    assert len(text) > 0


def test_get_text_slice(library):
    address = "Room1:Wall1:Shelf1:Volume1:Book1:Page1:10:20"
    text = library.get_text(address)
    assert isinstance(text, str)
    assert len(text) == 10


def test_get_book_title(library):
    address = "Room1:Wall1:Shelf1:Volume1:Book1"
    title = library.get_book_title(address)
    assert isinstance(title, str)
    assert len(title) > 0


def test_generate_random_address(library):
    address = library.generate_random_address()
    assert isinstance(address, str)
    assert "Room" in address
    assert "Wall" in address
    assert "Shelf" in address
    assert "Volume" in address
    assert "Book" in address
    assert "Page" in address


def test_search_in_library(library):
    target_text = "test"
    result = library.search_in_library(target_text, max_attempts=100)
    if result:
        address, start, end = result
        assert isinstance(address, str)
        assert isinstance(start, int)
        assert isinstance(end, int)
        assert start >= 0
        assert end <= library.page_length


def test_search_in_titles(library):
    target_text = "test"
    result = library.search_in_titles(target_text, max_attempts=100)
    if result:
        assert isinstance(result, str)


def test_iterator(library):
    iterator = SmartBabylonLibraryIterator(library)
    for _ in range(10):
        address, title, text = next(iterator)
        assert isinstance(address, str)
        assert isinstance(title, str)
        assert isinstance(text, str)


def test_invalid_address(library):
    with pytest.raises(ValueError):
        library.get_text("InvalidAddress")


def test_page_number_out_of_range(library):
    with pytest.raises(ValueError):
        library.get_text("Room1:Wall1:Shelf1:Volume1:Book1:Page100")


def test_slice_out_of_range(library):
    with pytest.raises(ValueError):
        library.get_text("Room1:Wall1:Shelf1:Volume1:Book1:Page1:1000:2000")
