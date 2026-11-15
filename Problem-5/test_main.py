from main import basket_total, receipt

def test_basket_total_one_quantity():
    basket = "apple:1:0.50;bread:1:1.20"
    assert basket_total(basket) == 1.7

def test_basket_total_two_quantities():
    basket = "apple:2:0.50;bread:1:1.20"
    assert basket_total(basket) == 2.2

def test_basket_total_empty():
    basket = ""
    assert basket_total(basket) == 0.0

def test_basket_total_one_item():
    basket = "apple:1:0.50"
    assert basket_total(basket) == 0.5


def test_receipt():
    basket = ""
    assert receipt(basket) == ""


def test_receipt_multiple_items():
    basket = "apple:2:0.50;bread:1:1.20"
    assert receipt(basket) == "apple x2 = 1.00\nbread x1 = 1.20\nTOTAL = 2.20"


def test_receipt_one_item():
    basket = "apple:1:0.50"
    assert receipt(basket) == "apple x1 = 0.50\nTOTAL = 0.50"


def test_receipt_multiple_same_item():
    basket = "apple:1:0.50;bread:1:1.20;apple:2:0.50"
    assert receipt(basket) == "apple x3 = 1.50\nbread x1 = 1.20\nTOTAL = 2.70"


def test_receipt_multiple_same_item_one_entry():
    basket = "apple:1:0.50;apple:2:0.50"
    assert receipt(basket) == "apple x3 = 1.50\nTOTAL = 1.50"