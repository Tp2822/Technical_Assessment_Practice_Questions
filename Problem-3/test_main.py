import pytest
from main import word_counter, top_words

def test_word_counter():
    words = "The cat and the hat"
    assert word_counter(words) == {"the": 2, "cat": 1, "and": 1, "hat": 1}


def test_word_counter_same_word():
    words = "Hello, hello! HELLO?"
    assert word_counter(words) == {"hello": 3}


def test_word_counter_empty():
    words = ""
    assert word_counter(words) == {}


def test_word_counter_invalid_number():
    with pytest.raises(ValueError):
        words = "Hello9, hello! HELLO?"
        word_counter(words)


def test_top_words():
    assert top_words("the cat and the hat", 2) == [("the", 2), ("and", 1)]

def test_top_words_empty():
    assert top_words("", 2) == []


def test_top_words_invalid():
    with pytest.raises(ValueError):
        top_words("the9 cat and the hat", 2)