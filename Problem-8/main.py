def balance(transactions: str) -> int:
    """Returns the final balance."""
    if transactions == "":
        return 0

    transaction_list = transactions.split(";")

    formatted_list = []
    for transaction in transaction_list:
        formatted_transaction = transaction.split(":")
        formatted_list.append(formatted_transaction)

    result = 0
    overdraft = []
    for transaction in formatted_list:
        deposit_withdrawal = transaction[0]
        amount = int(transaction[1])

        if deposit_withdrawal == "D":
            result += amount
        elif deposit_withdrawal == "W" and amount <= result:
            result -= amount
        elif deposit_withdrawal == "W" and amount > result:
            overdraft.append((deposit_withdrawal, amount))
    return (result, overdraft)



if __name__ == "__main__":
    print(balance("D:100;W:30;D:50"))
    print(balance("D:100;D:20;W:120"))