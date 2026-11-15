import pytest

from main import encode

def test_encode_forward():
    assert encode("abc", 1) == "bcd"

def test_encode_wrap_back():
    assert encode("xyz", 3) == "abc"

def test_encode_multiple_words():
    assert encode("Hello, World!", 3) == "Khoor, Zruog!"

def test_encode_no_shift():
    assert encode("abc", 0) == "abc"

def test_encode_no_text():
    assert encode("", 4) == ""