Challenge 3: Word Frequency Counter

You're building a text analysis tool for a small publishing company.

Step 1: Count Words

Given a string of text, return a dict of word counts. Normalise to lowercase and ignore punctuation (. , ! ? ;).

python
count_words("The cat and the hat")
# {"the": 2, "cat": 1, "and": 1, "hat": 1}

count_words("Hello, hello! HELLO?")
# {"hello": 3}

count_words("")
# {}
Step 2: Top N

Add top_words(text, n) returning the n most common words as a list of (word, count) tuples, sorted by count descending, then alphabetically for ties.

python
top_words("the cat and the hat", 2)
# [("the", 2), ("and", 1)]




Step 3: Stop Words

Add an optional ignore list of words to exclude from counts.

python
top_words("the cat and the hat", 2, ignore=["the", "and"])
# [("cat", 1), ("hat", 1)]



Step 4: Output Formats

Support format="dict" (default), "list" (sorted tuples) and "csv" ("word,count\n...").

