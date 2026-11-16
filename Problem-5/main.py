def format_basket(basket: str) -> list[list]:
    """Formats a basket to be a list of lists."""

    basket_list = basket.split(";")

    formatted_basket = []
    for item in basket_list:
        item_list = item.split(":")
        formatted_basket.append(item_list)

    return formatted_basket

def basket_total(basket: str) -> float:
    """Returns the total price of a basket of goods."""

    formatted_basket = format_basket(basket)

    if basket == "":
        return 0.0

    total = 0

    for item in formatted_basket:
        quantity = int(item[1])
        price = float(item[2])

        total += round(quantity * price, 2)

    return total

def basket_dictionary(basket: str) -> dict:
    """Converts a basket of goods into a dictionary."""
    if basket == "":
        return ""

    formatted_basket = format_basket(basket)

    dict_basket = {}

    for item in formatted_basket:
        grocery = item[0].lower()
        quantity = int(item[1])
        price = float(item[2])
        quantity_price = quantity * price

        if grocery in dict_basket:
            dict_basket[grocery]["quantity"] += quantity
            dict_basket[grocery]["price"] += quantity_price
        else:
            dict_basket[grocery] = {
                "quantity": quantity,
                "price": quantity_price
            }

    return dict_basket

def receipt(basket: str) -> str:
    """Returns a basket of goods as a dictionary."""

    if basket == "":
        return ""
    
    total = basket_total(basket)
    basket_dict = basket_dictionary(basket)

    result = ""
    for item in basket_dict:
        grocery = item
        quantity = basket_dict[item]["quantity"]
        price = basket_dict[item]["price"]

        result += f"{grocery} x{quantity} = {price:.2f}\n"

    result += f"TOTAL = {total:.2f}"

    return result

if __name__ == "__main__":
    print(receipt("apple:1:0.50;bread:1:1.20;apple:2:0.50"))

        
    