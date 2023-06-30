#With random, we are importing all random libraries.
# import random

# coin = random.choice(["heads", "tails"])
# print(coin)


#We can import only a part of the random libraries

# from random import choice
# coin = choice(["Heads", "Tails"])
# print(coin)

## NOTE: random.int

# import random
# number = random.randint(1, 10)
# print(number)

# import random
# cards = ["jack", "queen", "king"]
# #shuffle function itself only shuffles the card, there is no output
# random.shuffle(cards)
# print(mycard)
# for card in cards:
#     print(card)


#NOTE Statistics libraries
# import statistics
# print(statistics.mean([100, 90]))

#NOTE Command-line arguments
#This module allows you to parse arguements to your function at
#run time in your command line. In bash this will be the $0,1,2 ...


#NOTE: sys module also has a function called argv that can be used to to
#parse the command line arguement that are typed before the code
#is executed. This is the sys.argv module, this is a list.

import sys
#The [0] is the name of the program!
# print("hello, my name is", sys.argv[1])

#If there is no arguement, this code will flag an error. We can fix
#it by using an exception.

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")




