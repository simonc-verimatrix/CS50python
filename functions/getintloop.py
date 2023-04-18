

def main():
    x = get_int()
    print(f"x is {x}")


# def get_int():

#     while True:
#         try:                                    # First attempt normally before introducing exceptions
#             x = int(input("Whats's x? "))       # Here x is expected as an integer 
#             break                               #Break immediately after your test
#         except ValueError:                      #Using error handling to give more info on the
#             print("x is not an integer")                                           #Your testing stops here. If false
#     return x

#Note: Optimizing my get function:

def get_int():

    while True:
        try:                                    
            return int(input("Whats's x? "))                                                 
        except ValueError:                      
            print("x is not an integer")                                        

main()