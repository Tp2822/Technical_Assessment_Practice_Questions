Challenge 4: Password Validator

You're building the sign-up form for a new app.

Step 1: Basic Validation

is_valid(password) returns True only if the password:

is at least 8 characters
has at least one uppercase letter
has at least one lowercase letter
has at least one digit
python
is_valid("Passw0rdX")  # True
is_valid("password1")  # False (no uppercase)
is_valid("Pass1")      # False (too short)


Step 2: Explain the Failures

check(password) returns a list of the rules that failed, in this order: "length", "uppercase", "lowercase", "digit". Empty list if valid.

python
check("abc")        # ["length", "uppercase", "digit"]
check("Passw0rdX")  # []

Step 3: Special Characters and Banned Passwords

Add a fifth rule "special" (at least one of !@#$%^&*) and a "banned" rule: the password cannot contain "password" in any casing.

python
check("Password1!")  # ["banned"]
Step 4: Strength Score

Add strength(password) returning "weak" (0-2 rules passed), "medium" (3-4) or "strong" (all 5 and length >= 12).

Things to think about: empty string, unicode, spaces, a password containing PASSWORD in the middle, exactly 8 characters (boundary).