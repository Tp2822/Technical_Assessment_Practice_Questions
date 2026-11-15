def word_counter(words: str) -> dict:
    """Count the frequency of words."""
    for char in words:
        if char.isdigit():
            raise ValueError("Invalid input, no numbers allowed!")

    normalized_words = words.lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(";", "")
    normalized_words_list = normalized_words.split()

    result = {}
    no_repeats = []

    for word in normalized_words_list:
        if word not in no_repeats:
            no_repeats.append(word)
            occurrences = normalized_words.count(word)
            result[word] = occurrences

    return result

# My version
def top_words(words: str, n:int) -> list:
    """Returns the n most common words as a list, sorted by count."""
    counts = word_counter(words)
    result = list(counts.items())

    answer = []

    for word in result:
        num = word[-1]
        if len(answer) < n:
            answer.append(word)
        if len(answer) == n:
            for tuple in answer:
                tuple_word = tuple[0]
                tuple_number = tuple[-1]
                if tuple_word != word and num > tuple_number:
                    answer.replace(tuple, word)
    return answer

# Answer
def top_words(words: str, n: int) -> list:
    """Return the n most common words as (word, count) tuples."""
    counts = word_counter(words)
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ranked[:n]




if __name__ == "__main__":
    print(word_counter("Hello, hello! HELLO?"))
    print(top_words("the cat and the hat", 2))