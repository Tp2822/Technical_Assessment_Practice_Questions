Challenge 5: Shopping Basket

You're building the checkout for a corner shop.

Input Format

"apple:2:0.50;bread:1:1.20;milk:3:0.90" (name : quantity : unit price)

Step 1: Total

basket_total(basket) returns the total price rounded to 2 decimal places.

python
basket_total("apple:2:0.50;bread:1:1.20")  # 2.2
basket_total("")                           # 0.0



Step 2: Receipt

receipt(basket) returns one line per item, sorted alphabetically, then a total line:

"apple x2 = 1.00\nbread x1 = 1.20\nTOTAL = 2.20"




Step 3: Duplicate Items

The same item can appear more than once in the basket string. Merge them into one line with the combined quantity.

python
receipt("apple:1:0.50;bread:1:1.20;apple:2:0.50")
# "apple x3 = 1.50\nbread x1 = 1.20\nTOTAL = 2.70"


Step 4: Offers

Support a "3 for 2" deal on a given item: for every 3 of that item, the cheapest one is free. Take offers as an optional list of item names.

Things to think about: float rounding (look into round or Decimal), quantity 0, malformed items, 4 or 6 of an offer item.