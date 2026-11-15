from main import balance

def test_balance_one_deposit_one_withdrawal():
    assert balance("D:100;W:30") == (70, [])

def test_balance_one_deposit():
    assert balance("D:100") == (100, [])

def test_balance_no_input():
    assert balance("") == 0

def test_balance_overdraft():
    assert balance("D:100;W:150;D:20") == (120, [("W", 150)])

def test_balance_even():
    assert balance("D:100;D:20;W:120") == (0, [])


def test_balance_order():
    assert balance("D:100;W:120;D:20") == (120, [("W", 120)])