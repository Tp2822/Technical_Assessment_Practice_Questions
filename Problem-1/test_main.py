from main import sort_names
import pytest

def test_sort_names():
    names = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
    assert sort_names(names) == "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"


def test_sort_names_two_names():
    names = "John:Bell;Ann:Kern"
    assert sort_names(names) == "(BELL, JOHN)(KERN, ANN)"


def test_sort_names_empty_input():
    with pytest.raises(ValueError):
        names = ""
        sort_names(names)

