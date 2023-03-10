# Modulo
# In mathematics, parity refers to whether a 
# number is either even or odd.
# The modulo % operator in programming allows one to 
# see if two numbers divide evenly 
# or divide and have a remainder.
# For example, 4 % 2 would result in zero, because it evenly divides. 
# However, 3 % 2 does not divide evenly and would result in a number 
# other than zero!
# +
# *
# /
# % >>> This is the modulus operation. The remainder after divison.This is useful in 
# checking if a number is even or odd. 

x = int(input("What's x? "))
if x % 2 ==0:
    print("Even")
else:
    print("Odd")


