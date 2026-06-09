def after_transaction(balance, transaction):
    if balance + transaction < 0:
        return balance
    else:
        return balance + transaction

print(after_transaction(500, 20))
print(after_transaction(300, -200))
print(after_transaction(3, -1000))
print(after_transaction(3, -4))
print(after_transaction(3, -3))
