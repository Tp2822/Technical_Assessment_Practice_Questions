import pytest

from main import mexican_wave, bidirectional_mexican_wave

def test_mexican_wave_one_word():
    word = "hello"
    assert mexican_wave(word) == ["Hello", "hEllo", "heLlo", "helLo", "hellO"]


def test_mexican_wave_two_words():
    word = "two words"
    assert mexican_wave(word) == ["Two words", "tWo words", "twO words", \
                                  "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]


def test_mexican_wave_space_word():
    word = " gap "
    assert mexican_wave(word) == [" Gap ", " gAp ", " gaP "]


def test_mexican_wave_empty_input():
    word = ""
    assert mexican_wave(word) == []


def test_mexican_wave_capital():
    word = "helLo"
    assert mexican_wave(word) == ["Hello", "hEllo", "heLlo", "helLo", "hellO"]


def test_bidirectional_mexican_wave_three_letters():
    word = "abc"
    assert bidirectional_mexican_wave(word) == ["Abc", "aBc", "abC", "aBc", "Abc"]


def test_bidirectional_mexican_wave_two_letters():
    word = "go"
    assert bidirectional_mexican_wave(word) == ["Go", "gO", "Go"]



def test_bidirectional_mexican_wave_capitalized():
    word = "gO"
    assert bidirectional_mexican_wave(word) == ["Go", "gO", "Go"]



def test_bidirectional_mexican_wave_empty():
    word = ""
    assert bidirectional_mexican_wave(word) == []



def test_bidirectional_mexican_wave_two_words():
    word = "two words"
    assert bidirectional_mexican_wave(word) == ["Two words", "tWo words", "twO words", \
                                                "two Words", "two wOrds", "two woRds", \
                                                    "two worDs", "two wordS", "two worDs", \
                                                        "two woRds", "two wOrds", "two Words", \
                                                            "twO words", "tWo words", "Two words"]