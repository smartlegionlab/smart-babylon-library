import string

from smart_babylon_library.babylon_lib_with_books import BabylonLibraryWithBooks

RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def test_babylon_lib_with_books_generate_word():
    library = BabylonLibraryWithBooks()
    word = library.generate_word()

    assert isinstance(word, str)
    assert 1 <= len(word) <= 10

    if word[0] in RU:
        assert all(c in RU for c in word)
    elif word[0] in string.ascii_letters:
        assert all(c in string.ascii_letters for c in word)
    else:
        assert all(c in string.digits for c in word)


def test_babylon_lib_with_books_generate_sentence():
    library = BabylonLibraryWithBooks()
    sentence = library.generate_sentence()

    assert isinstance(sentence, str)
    assert sentence.rstrip()[-1] in [".", "!", "?"]

    words = sentence.rstrip()[:-1].split()

    for word in words:
        if word[0] in RU:
            assert all(c in RU for c in word)
        elif word[0] in string.ascii_letters:
            assert all(c in string.ascii_letters for c in word)
        else:
            assert all(c in string.digits for c in word)


def test_babylon_lib_with_books_generate_page():
    library = BabylonLibraryWithBooks()
    page = library.generate_page()
    assert isinstance(page, str)
    assert len(page) >= library.page_length


def test_babylon_lib_with_books_generate_book_title():
    library = BabylonLibraryWithBooks()
    title = library.generate_book_title()
    assert isinstance(title, str)
    assert title[0].isupper()


def test_babylon_lib_with_books_generate_book():
    library = BabylonLibraryWithBooks()
    book = library.generate_book(num_pages=5)
    assert isinstance(book, dict)
    assert "title" in book
    assert "pages" in book
    assert len(book["pages"]) == 5


def test_babylon_lib_with_books_add_book_to_library():
    library = BabylonLibraryWithBooks()
    book = library.generate_book(num_pages=5)
    address = library.add_book_to_library(book)
    assert isinstance(address, str)
    assert address.count(":") == 4


def test_babylon_lib_with_books_get_text():
    library = BabylonLibraryWithBooks()
    book = library.generate_book(num_pages=5)
    address = library.add_book_to_library(book)
    text = library.get_text(address)
    assert isinstance(text, str)


def test_babylon_lib_with_books_search_in_library():
    library = BabylonLibraryWithBooks()
    book = library.generate_book(num_pages=5)
    library.add_book_to_library(book)
    result = library.search_in_library("test")
    assert result in [None, tuple]


def test_babylon_lib_with_books_iterator():
    library = BabylonLibraryWithBooks()
    book = library.generate_book(num_pages=5)
    library.add_book_to_library(book)
    iterator = iter(library)
    address, title = next(iterator)
    assert isinstance(address, str)
    assert isinstance(title, str)
