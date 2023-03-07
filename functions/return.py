def main():                             #DEFINE YOUR MAIN FUNCTION
    x = int(input("What's x ? "))       
    print("x squared is ", square(x))   # CALLING A FUNCTION square() which takes an argument


def square(n):
    return n * n                        # THE RETURN HERE MAKES SURE YOU CAN PARSE THE RETURNED VALUE TO THE FUNCTION
   #return n ** 2                       # ANOTHER WAY OF RAISING A NUMBER TO 2
   #return pow(n, 3)                   # ANOTHER WAY OF USING A pow() to raise a number to a number
main()
