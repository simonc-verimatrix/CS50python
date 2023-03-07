# DEALING WITH INT

#1 Default calculator that will treat inputs as strings as default behaviour
#x = input("What's x? ")
#y = input ("What's y? ")
#z = x + y               #By default all inputs are treated as strings and the output of this will be concatenation of x and y
#print(z)

# If x=1 and y=2, the output of this code will be 12.

#2 TO PREVENT THIS INPUT CONCATENATION, WE INTRODUSE THE VARIABLES AS INT USING THE INT() FUNCTION
#z = int(x) + int(y)
#print(z)

#3 ANOTHER OPTION
# x = int(input("What's x? "))
# y = int(input ("What's y? "))
# print(x + y)

#4 WORKING WITH FLOATS. THIS IS ANOTHER DATA TYPE; NUMBER WITH DECIMAL POINTS

# x = float(input("What's x? "))
# y = float(input ("What's y? "))
# print(x + y)

#5 WORKING WITH ROUND FUNCTION round(number[, ndigits])
# THIS WILLL ROUND TO "NUMBER" [OPTIONALLY], YOU CAN SPECIFY THE NUMBER OF DIGITS BY "N"

# x = float(input("What's x? "))
# y = float(input ("What's y? "))
# z = round(x + y)
# print(z)

#6 FORMATING THE NUMBER TO MEET THE STANDARD NUMBERS , OR . EG 1,000 OR 1.000 

# x = float(input("What's x? "))
# y = float(input ("What's y? "))
# z = round(x + y)
# print(F"{z:,}")         #THIS WILL INTRODUCE , AFTER EVERY THOUSAND 

#7 WORKING WITH FLOAT AND ROUND TO SPECIFIC DECIMAL PLACES

# x = float(input("What's x? "))
# y = float(input ("What's y? "))
# z = round(x / y, 2)                    #round(number[, ndigits]) here rount to 2 DC places
# print(z)

#7 USING F STRING TO SPECIFY DECIMAL PLACES FOR FLOAT

x = float(input("What's x? "))
y = float(input ("What's y? "))
z = x / y
print(f"{z:.2f}")               #ANOTHER WAY OF SPECIFYING THE DC PLACES VIA F STRING