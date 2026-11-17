import pytest

from main import encode, decode

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


def test_decode_two_words():
    assert decode("Khoor, Zruog!", 3) == "Hello, World!"

def test_encode_over_26():
    assert encode("abc", 27) == "bcd"


def test_encode_negative():
    assert encode("abc", -1) == "zab"


def test_encode_rotating_matches_spec_example():
    assert encode_rotating("abc", [1, 2]) == "bdd"