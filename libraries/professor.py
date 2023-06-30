# In a file called professor.py, implement a program that:
# Prompts the user for a level, 
# . If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
#  digits. No need to support operations other than addition (+).
# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.

import random


def main():
    level = get_level()
    score = game(level)
    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <=3:
                break
        except:
            pass
    return level

def generate_integer(level):
    if level == 1:
        X = random.randint(0, 9)
        Y = random.randint(0, 9)
    elif level == 2:
        X = random.randint(10, 99)
        Y = random.randint(10, 99)
    else:
        X = random.randint(100, 999)
        Y = random.randint(100, 999)
    return X, Y

def cal(X, Y):
    i = 1
    while i <= 3:
        try:
            check = int(input(f"{X} + {Y} = "))
            if (X + Y) == check:
                return True

            else:
                i += 1
                print("EEE")
        except:
            i +=1
            print("EEE")
    print(f"{X} + {Y} = {X + Y}")
    return False

def game(level):
    rounds =1
    score =0
    while rounds <= 10:
        X, Y = generate_integer(level)
        response = cal(X,Y)
        if response == True:
            score += 1
        rounds += 1
    return score

if __name__ == "__main__":
    main()