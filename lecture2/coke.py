amount_due = 50
while amount_due > 0:
    coin = -1
    while coin < 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert a coin: "))
    if coin in [25,10,5]:
        amount_due -= coin
print(f"Change Owed: {-amount_due}")
