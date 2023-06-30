import random

while True:
    try:
        n = int(input("Level: "))
        if n >= 1:
            choice= random.randint(1, n)
            break
    except:
        pass
#print(choice)

while True:
    try:
        guess =int(input("Guess: "))
        if choice < guess:
            print("Too large!")

        if choice > guess:
            print("Too small!")

        if choice == guess:
            print("Just right!")
            break
    except:
        pass