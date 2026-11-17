Challenge 6: Caesar Cipher

You're building a tool for a puzzle magazine.

Step 1: Encode

encode(text, shift) shifts each letter forward by shift places, wrapping from z back to a. Preserve case. Leave non-letters unchanged.

python
encode("abc", 1)             # "bcd"
encode("xyz", 3)             # "abc"
encode("Hello, World!", 3)   # "Khoor, Zruog!"


Step 2: Decode

decode(text, shift) reverses an encoding. Support negative shifts and shifts larger than 26.

python
decode("Khoor, Zruog!", 3)  # "Hello, World!"
encode("abc", 27)           # "bcd"
encode("abc", -1)           # "zab"


Step 3: Crack It

crack(text) tries to guess the shift by assuming the most common letter in the text is e. Return (shift, decoded_text).

Step 4: Rotating Shift

encode_rotating(text, shifts) where shifts is a list, and the shift used cycles through the list for each LETTER (non-letters don't consume a shift).

python
encode_rotating("abc", [1, 2])  # "bdd"