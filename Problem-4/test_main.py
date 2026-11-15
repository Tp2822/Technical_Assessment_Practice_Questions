import pytest

from main import is_valid, failed_password, strength_score


# Step 1: is_valid
def test_is_valid_correct_password():
    assert is_valid("Passw0rdX!")


def test_is_valid_too_short():
    assert not is_valid("Pass1")


def test_is_valid_exactly_eight_characters():
    assert is_valid("Passw0r!")


def test_is_valid_seven_characters():
    assert not is_valid("Passw0r")


def test_is_valid_missing_uppercase():
    assert not is_valid("passw0rdx")


def test_is_valid_missing_lowercase():
    assert not is_valid("PASSW0RDX")


def test_is_valid_missing_digit():
    assert not is_valid("Passwordx")


def test_is_valid_empty_input_raises():
    with pytest.raises(ValueError):
        is_valid("")


# Step 2: failed_password
def test_failed_password_no_failures():
    assert failed_password("Passw0rdX!") == []

def test_failed_password_special_failure():
    assert failed_password("Passw0rdX") == ["special"]


def test_failed_password_three_failures_special_banned():
    assert failed_password("password1") == ["uppercase", "special", "banned"]


def test_failed_password_two_failures():
    assert failed_password("abc1!") == ["length", "uppercase"]


def test_failed_password_three_failures_in_spec_order():
    assert failed_password("passwor") == ["length", "uppercase", "digit", "special"]


def test_failed_password_empty_input_raises():
    with pytest.raises(ValueError):
        failed_password("")


# Step 4: strength_score
def test_strength_weak_one_rule_passed():
    assert strength_score("abc") == "weak"


def test_strength_weak_two_rules_passed():
    assert strength_score("abcdefgh") == "weak"


def test_strength_medium_three_rules_passed():
    assert strength_score("abcdefgH") == "medium"


def test_strength_medium_four_rules_passed():
    assert strength_score("Passw0rd") == "medium"


def test_strength_medium_all_rules_but_under_twelve():
    assert strength_score("Abcdefgh1!x") == "medium"


def test_strength_strong_exactly_twelve():
    assert strength_score("Abcdefgh1!xy") == "strong"


def test_strength_strong_long_password():
    assert strength_score("Tr0ub4dor&Horse") == "strong"


def test_strength_banned_password_is_not_strong():
    assert strength_score("Password1234!") == "medium"


def test_strength_empty_input_raises():
    with pytest.raises(ValueError):
        strength_score("")