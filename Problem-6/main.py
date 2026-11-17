def encode(text: str, n: int) -> str:
    """Shifts each letter forward by n places."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    result = ""
    for char in text:
        if not char.isalpha():
            result += char
        elif char.isalpha() and char.isupper():
            position = alphabet.index(char.lower())
            new_letter = alphabet[(position + n) % 26]
            result += new_letter.upper()
        elif char.isalpha() and char.islower():
            position = alphabet.index(char)
            new_letter = alphabet[(position + n) % 26]
            result += new_letter

    return result


def decode(text: str, n: int) -> str:
    """Reverses an encoding"""
    return encode(text, -n)
    
def crack(text: str) -> tuple:
    """Tries to guess the shift by assuming the most common letter in the text is e."""

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    no_repeats_list = []
    result = []

    for char in text:
        if char not in no_repeats_list:
            no_repeats_list.append(char)
            occurrences = text.count(char)
            result_entry = (char, occurrences)
            result.append(result_entry)

    maximum_value = 0
    letter = ""
    for entry in result:
        let = entry[0]
        num = entry[-1]

        if num > maximum_value:
            maximum_value = num
            letter = let

    e_position = alphabet.index("e")
    e_replacement_position = alphabet.index(letter)

    n = e_replacement_position - e_position

    answer = decode(text, n)

    return (n, answer)

def encode_rotating(text: str, n: list[int]) -> str:
    """Encode a string using shift as a list."""


if __name__ == "__main__":
    print(encode("Hello, World!", 3))
    print(crack("gggcd"))
