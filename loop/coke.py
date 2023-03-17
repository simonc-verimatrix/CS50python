print("Amount Due: 50")
amount_due = 50
coins_added = 0

while True:
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        amount_due = amount_due - coin
        coins_added = coins_added + coin
    if coins_added >= 50:
        print(f"Change owed: {coins_added - 50}")
        break
    else:
        print(f"Amount Due: {amount_due}")