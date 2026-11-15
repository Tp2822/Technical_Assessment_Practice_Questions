def encode(text: str) -> str:
    """Compress consecutive repeated characters 
    as the character followed by its count."""
    if text == "":
        return ""

    result = ""
    no_repeats_list = []

    for char in text:
        if char.isdigit():
            raise ValueError("No digits allowed!")
        if char not in no_repeats_list:
            no_repeats_list.append(char)
            occurrences = text.count(char)
            result += f"{char}{occurrences}"

    return result


def decode(code: str) -> str:
    """Reverse run-length encoding, including multi-digit counts."""
    if code == "":
        return ""

    result = ""
    i = 0
    while i < len(code):
        char = code[i]
        i += 1

        digits = ""
        while i < len(code) and code[i].isdigit():
            digits += code[i]
            i += 1

        result += char * int(digits)

    return result