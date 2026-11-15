def encode(text: str, n: int) -> str:
    """Shifts each letter forward by n places."""
    if text == "":
        return ""

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    result = ""
    for char in text:
        if not char.isalpha():
            result += char
        position = alphabet.index(char)
        if position + n > len(alphabet) - 1:
            new_position = abs(len(alphabet) - position - n)
            result += alphabet[new_position]
        else:
            new_char = alphabet[position + n]
            result += new_char
    return result