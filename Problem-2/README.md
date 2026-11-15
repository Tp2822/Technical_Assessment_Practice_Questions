Challenge 2: Mexican Wave Generator (original)
Step 1: Simple Wave

Turn a string into a Mexican wave: return a list where an uppercase letter is a person standing up.

Input is always lowercase but may be empty
Whitespace is an empty seat: skip over it
python
wave("hello")     # ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
wave("two words") # ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
wave(" gap ")     # [" Gap ", " gAp ", " gaP "]
wave("")          # []
Step 2: Bidirectional Wave

Wave goes start to end, then reverses back. Spaces still skipped.

python
# "abc" -> ["Abc", "aBc", "abC", "aBc", "Abc"]
# "go"  -> ["Go", "gO", "Go"]
Step 3: Multiple Simultaneous Waves

Several waves start at different positions at the same time, each moving one direction, no overlaps. Whitespace still skipped.

python
# "hello", starting at 0 and 2
# Frame 1: "HeLlo"
# Frame 2: "hElLo"
Step 4: Multiple Simultaneous Waves in Both Directions

Extend to bidirectional waves and handle what happens when they overlap.