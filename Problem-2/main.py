def mexican_wave(word: str) -> list[str]:
    """Turn a string into a Mexican wave."""
    if word == "":
        return []
    formatted_word = word.lower()

    result = ""
    for i in range(len(formatted_word)):
        char = formatted_word[i]
        if char.isalpha() and i+1 <= len(formatted_word):
            mexican_word = f"{formatted_word[0:i]}{char.upper()}{formatted_word[i+1:]},"
            result += mexican_word

        result_list = (result.strip(",")).split(",")
    return result_list


def bidirectional_mexican_wave(word: str) -> list[str]:
    """Turn a string into a bidirectional Mexican wave."""
    wave = mexican_wave(word)

    wave_no_last_input = wave[:-1]
    reverse_wave = wave_no_last_input[::-1]

    return wave + reverse_wave


