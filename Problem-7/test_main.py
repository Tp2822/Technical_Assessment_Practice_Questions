import pytest
from main import encode, decode

def test_encode_one_character():
    assert encode("a") == "a1"

def test_encode_multiple_character_one_repeat():
    assert encode("abcd") == "a1b1c1d1"

def test_encode_multiple_character_multiple_repeats():
    assert encode("aaabccdddd") == "a3b1c2d4"

def test_encode_no_entry():
    assert encode("") == ""

def test_encode_number():
    with pytest.raises(ValueError):
        encode("abc4")

def test_encode_over_ten_repeats():
    assert encode("aaaaaaaaaaaabb") == "a12b2"

def test_decode_one_character():
    assert decode("a1") == "a"

def test_decode_multiple_characters():
    assert decode("a3b1c2d4") == "aaabccdddd"

def test_decode_no_entry():
    assert decode("") == ""

def test_decode_number():
    with pytest.raises(ValueError):
        decode("abc")

def test_decode_over_ten():
    assert decode("a12b2") == "aaaaaaaaaaaabb"

def test_decode_multiple_over_ten():
    assert decode("a12b15") == "aaaaaaaaaaaabbbbbbbbbbbbbbb"