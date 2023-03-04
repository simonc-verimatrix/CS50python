#   print ("hello, world")    Print Funtion >> print(*objects, sep=' ', end='\n', file=None, flush=False) Everything inside are the parameters.
# . Ask user for their name

# 1 INPUT VARIABLE FROM CLI
# name = input("Whats your name? ")            # Use variable to assign your input function
# print("hello," , name)                       # Parse your input variable in your print fiunction. Note no "" using the , option
# print("hello, " + name)                      # Using the + concatenation symbol
# Pseudocode: Is a way of outlining or structuring your codes without actually wrting your code.
# 2 USE TWO PRINT STATEMENTS AND BYPASS THE DEFAULT \N NEW LINE IN PRINT() FUNCTION
# Print Funtion >> print(*objects, sep=' ', end='\n', file=None, flush=False) to bypass the default newline in print statement:

# print("hello, ", end="")                    # Hello here is a POTIONAL PARAMETERS
# print(name)                                 # while END= is a NAMED PARAMETERS which are optional and can be passed at the end of your print function

# 3 HOW TO PRINT "" IN THE CODE OPTION 1
# print("hello, \"FRINED\"")

# OPTION 2
# print('hello, "FRINED"')                    # YOU CAN USE "" OR '' but you must be consistent.

# 4 BEST WAY OF PARSING ASSIGNED VARIABLE TO PRINT FUNCTION
# print(f"hello, {name}")                        # Use {} to hold your variables and introduce f at the beginning of the function print


# 6 TO STRIP OUT WHITE SPACES THAT MAY BE INTRODUCED DUE IN INPUTING THE VARIABLE IS THE INPUT FUCTION, WE CAN USE THE strip() function
# To remove white spaces in the right and in the left. Not in the middle!

# name = input("Whats your name? ")
# Remove whitespaces from the str
# name = name.strip()
# print(f"hello, {name}")


# 7 Capitalize The First Name: This will Capitalize only the first name
# name = name.capitalize()
# print(f"hello, {name}")

# 8 To Capitalize all the Names, we use the title() function: This will capitalize all words
# name = name.title()
# print(f"hello, {name}")

# 9 We can Strip whitespace and Capitalize by Title function in one function:
# name = name.strip().title()
# print(f"hello, {name}")

# 10 We can combine all in one line of code:
name = input("Whats your name? ").strip().title()
#print(f"hello, {name}")

#11 WE CAN USE SPLIT TO SPLIT THE NAMES BY CHARACTER AND ASSIGN IT.
first, last = name.split(" ")            # THIS SPLIT THE INPUT INTO TWO ASSIGNING THEM TO THE VARIABLES "first" and "last" using space "" as separator
print(f"hello, {first}")