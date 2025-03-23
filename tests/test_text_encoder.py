# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smart_babylon_library.text_encoder import TextEncoder


def test_text_encoder_encode_text():
    encoder = TextEncoder()
    text = "test text"
    encoded_address = encoder.encode_text(text)
    assert isinstance(encoded_address, str)
    assert ":" in encoded_address


def test_text_encoder_decode_address():
    encoder = TextEncoder()
    text = "test text"
    encoded_address = encoder.encode_text(text)
    decoded_text = encoder.decode_address(encoded_address)
    assert isinstance(decoded_text, str)
    assert decoded_text == text


def test_text_encoder_sanitize_text():
    encoder = TextEncoder()
    text = "test text!@#"
    sanitized_text = encoder._sanitize_text(text)
    assert isinstance(sanitized_text, str)
    assert "!@#" not in sanitized_text


def test_text_encoder_text_to_num():
    encoder = TextEncoder()
    text = "test"
    number = encoder._text_to_num(text)
    assert isinstance(number, int)


def test_text_encoder_num_to_base62():
    encoder = TextEncoder()
    number = 12345
    base62 = encoder._num_to_base62(number)
    assert isinstance(base62, str)


def test_text_encoder_base62_to_num():
    encoder = TextEncoder()
    base62 = "3d7"
    number = encoder._base62_to_num(base62)
    assert isinstance(number, int)


def test_text_encoder_num_to_text():
    encoder = TextEncoder()
    number = 12345
    text_length = 5
    text = encoder._num_to_text(number, text_length)
    assert isinstance(text, str)
    assert len(text) == text_length
