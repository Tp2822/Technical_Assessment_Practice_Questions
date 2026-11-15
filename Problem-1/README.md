Challenge 1: Guest List Manager (original)

You've been tasked to build a guest list tool for John's Party co.!

Input Format

"Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;..."

Step 1: Process Guest List

Parse the guest list, normalise names to uppercase, sort by last name (then first name when last names match), and format as: "(LASTNAME, FIRSTNAME)(LASTNAME, FIRSTNAME)..."

Note: two distinct families with the same family name can have two people with the same first name too.

python
meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill")
# "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"

meeting("John:Bell;Ann:Kern")
# "(BELL, JOHN)(KERN, ANN)"
Step 2: Export Multiple Formats
"inline" (default): "(LASTNAME, FIRSTNAME)..."
"list": [("LASTNAME", "FIRSTNAME"), ...]
"csv": "LASTNAME,FIRSTNAME\nLASTNAME,FIRSTNAME\n..."
python
"Fred:Corwill;Alfred:Corwill", format="list"
# [("CORWILL", "ALFRED"), ("CORWILL", "FRED")]

"Fred:Corwill;Alfred:Corwill", format="csv"
# "CORWILL,ALFRED\nCORWILL,FRED\n"
Step 3: Filter by Family

Retrieve guests from only a specific family (last name).

python
"Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Jane:Tornbull"
# Corwill only -> "(CORWILL, FRED)(CORWILL, WILFRED)"
# Tornbull only, as csv -> "TORNBULL,BARNEY\nTORNBULL,JANE\n"