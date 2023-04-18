
#Note 1.
# try:                                    # First attempt normally before introducing exceptions
#     x = int(input("Whats's x? "))       # Here x is expected as an integer 
#     print(f"x is {x}")                  # If the user supplies != integer, we get ValueError
# except ValueError:                      #Using error handling to give more info on the
#     print("x is not an integer")        # ValueError message.

#Note 2. Introducing else in the try|except|else
# try:                                    # First attempt normally before introducing exceptions
#     x = int(input("Whats's x? "))       # Here x is expected as an integer 
#                                         # If the user supplies != integer, we get ValueError
# except ValueError:                      #Using error handling to give more info on the
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

#Note: Introducing Loop not to break the code

# while True:
#     try:                                    # First attempt normally before introducing exceptions
#         x = int(input("Whats's x? "))       # Here x is expected as an integer 
#                                             # If the user supplies != integer, we get ValueError
#     except ValueError:                      #Using error handling to give more info on the
#         print("x is not an integer")
#     else:
#         break                               #Your testing stops here. If false
# print(f"x is {x}")                          # the loop continues, if true next line exc

#Note: Breaking immidiately after your true conditon

# while True:
#     try:                                    # First attempt normally before introducing exceptions
#         x = int(input("Whats's x? "))       # Here x is expected as an integer 
#         break                               #Break immediately after your test
#     except ValueError:                      #Using error handling to give more info on the
#         print("x is not an integer")                                           #Your testing stops here. If false
# print(f"x is {x}")

#Note Another option of handling the error without providing information
#to the user of what the problem is by simply using pass.

while True:
    try:                                    # First attempt normally before introducing exceptions
        x = int(input("Whats's x? "))       # Here x is expected as an integer 
        break                               #Break immediately after your test
    except ValueError:                                            #Your testing stops here. If false
        pass