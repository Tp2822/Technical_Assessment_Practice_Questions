Challenge 7: Run-Length Encoding
Step 1: Encode

Compress consecutive repeated characters as the character followed by its count.

python
encode("aaabccdddd")  # "a3b1c2d4"
encode("a")           # "a1"
encode("")            # ""


Step 2: Decode

decode(s) reverses it.

python
decode("a3b1c2d4")  # "aaabccdddd"



Step 3: Multi-Digit Counts

Handle runs of 10 or more.

python
encode("a" * 12)  # "a12"
decode("a12b2")   # "aaaaaaaaaaaabb"





Step 4: Compact Mode

Add compact=True to encode, which omits the count when it's 1.

python
encode("aaabccdddd", compact=True)  # "a3bc2d4"
decode("a3bc2d4")                   # "aaabccdddd"

Things to think about: a round trip test (decode(encode(x)) == x) is a great one to include. Also: case sensitivity ("aA"), spaces, and what happens if the input contains digits (decide a rule and say it out loud to your interviewer).