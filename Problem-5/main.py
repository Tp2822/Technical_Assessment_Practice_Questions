def shopping_list(basket:str) -> list[str]:

    if basket == "":
            return []
    
    basket_list = basket.split(";")

    basket_list_tuple = []
    for item in basket_list:
        item_list = item.split(":")
        basket_list_tuple.append(item_list)

    return basket_list_tuple

def basket_total(basket: str) -> int:
    """Returns the total price of a basket."""

    if basket == "":
        return 0.0

    basket_list = shopping_list(basket)
    
    total = 0
    for item in basket_list:
        quantity = int(item[1])
        price = float(item[2])
        result = round(quantity * price, 2)
        total += result

    return total

def receipt(basket: str) -> str:
    """Returns the receipt of a basket of goods."""
    if basket == "":
         return ""
    
    total = basket_total(basket)
    basket_list = shopping_list(basket)


    basket_dict = {}
    for item in basket_list:
         grocery = item[0]
         quantity = int(item[1])
         price = float(item[2]) 
         
         if grocery in basket_dict:
            basket_dict[grocery]["quantity"] += quantity
            basket_dict[grocery]["price"] += quantity * price
         else:
            basket_dict[grocery] = {
                 "quantity": quantity,
                 "price": quantity * price
            }

    receipt_string = ""

    for grocery in sorted(basket_dict):
        quantity = basket_dict[grocery]["quantity"]
        price = basket_dict[grocery]["price"]

        receipt_string += f"{grocery.lower()} x{quantity} = {price:.2f}\n"

    receipt_string += f"TOTAL = {total:.2f}"

    return receipt_string
        



if __name__ == "__main__":
    print(basket_total("apple:2:0.50;bread:1:1.20"))
    print(basket_total(""))

    print(receipt("apple:2:0.50;bread:1:1.20"))
    print(receipt("apple:1:0.50;bread:1:1.20;apple:2:0.50"))