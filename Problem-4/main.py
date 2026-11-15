def verification_list(password: str) -> list[str]:
    """Returns the rules a password passes."""
    if password == "":
        raise ValueError("Password cannot be empty!")

    verification = []
    special = ["!", "@", "#", "$", "%", "^", "&", "*"]

    if len(password) >= 8:
        verification.append("Length")

    for char in password:
        if char.islower():
            verification.append("Lower")
            break

    for char in password:
        if char.isupper():
            verification.append("Upper")
            break

    for char in password:
        if char.isdigit():
            verification.append("Digit")
            break

    for char in password:
        if char in special:
            verification.append("Special")
            break

    return verification


def banned_password(password: str) -> bool:
    """Returns True if the password contains 'password' in any casing."""
    return "password" in password.lower()


def failed_password(password: str) -> list[str]:
    """Returns a list of missing characteristics in a password."""
    verification = verification_list(password)
    result = []
    if "Length" not in verification:
        result.append("length")
    if "Upper" not in verification:
        result.append("uppercase")
    if "Lower" not in verification:
        result.append("lowercase")
    if "Digit" not in verification:
        result.append("digit")
    if "Special" not in verification:
        result.append("special")
    if banned_password(password):
        result.append("banned")

    return result


def is_valid(password: str) -> bool:
    """A password is valid if it fails no rules."""
    return failed_password(password) == []


def strength_score(password: str) -> str:
    """Return 'weak', 'medium' or 'strong'."""
    failed = failed_password(password)
    character_rules_failed = [rule for rule in failed if rule != "banned"]
    passed = 5 - len(character_rules_failed)

    if passed <= 2:
        return "weak"
    if passed == 5 and len(password) >= 12 and "banned" not in failed:
        return "strong"
    return "medium"


if __name__ == "__main__":
    print(is_valid("Passw0rdX!"))
    print(failed_password("abc"))
    print(strength_score("Tr0ub4dor&Horse"))