Challenge 8: Bank Account Transactions
Input Format

"D:100;W:30;D:50" (D = deposit, W = withdrawal, then amount)

Step 1: Balance

balance(transactions) returns the final balance, starting from 0.

python
balance("D:100;W:30;D:50")  # 120
balance("")                 # 0



Step 2: Reject Overdrafts

A withdrawal that would take the balance below 0 is rejected (ignored). Return a tuple of (balance, rejected) where rejected is a list of (type, amount) tuples.

python
balance("D:100;W:150;D:20")  # (120, [("W", 150)])



Step 3: Statement

statement(transactions) returns a list of lines showing the running balance after each transaction, rejected ones marked as such:

python
statement("D:100;W:150;D:20")
# ["D 100 -> 100", "W 150 -> REJECTED", "D 20 -> 120"]




Step 4: Overdraft Limit

Add an optional overdraft parameter (default 0) that lets the balance go down to -overdraft.

Things to think about: invalid transaction types, negative or zero amounts, malformed strings, decimals.