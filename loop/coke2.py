def main():
 #   print("Amount Due: 50")
    coin = check_coin()
    Amount_Due = 50
    coin_added = 0
    while True:
        Amount_Due = Amount_Due - coin
        coin_added = coin_added + coin
        if coin_added <= 50:
            print("Amount Due:", Amount_Due)
            coin = int(input("Insert coin: "))
            
        else:
            None
            

def check_coin():
    while True:
        print("Amount Due: 50")
        coin = int(input("Insert coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            
            return coin
            break
        else:
            None    #     coin = int(input("Insert coin: "))

    







main()