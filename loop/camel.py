#NOTE 1: Get user input
# NOTE 3: Loop through every letter
#NOTE 4 Check if letter is upper case
# NOTE 5 Print underscores and the letter in lowercase
# NOTE 6 Otherwise, print letter
# NOTE 7 Print space in the end

CamelCase = input("CamesCase: ")
for char in CamelCase:
    if char.isupper():
        print("_" + char.lower(), end="")
    else:
        print(char, end="")
print()                                 #This will intro a new line
