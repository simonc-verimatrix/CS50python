#PARITY IMPLEMENTATION USING BOOL DATA TYPE

# x = int(input("What's x? "))
# if x % 2 ==0:
#     print("Even")
# else:
#     print("Odd")

#1 IMPLEMENTING THIS EVEN ODD CHECK BY CREATING A FUNCTION:
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

#2 NOW WE MUST DEFINE OUR IS_EVEN()
# def is_even(n):
#     if n % 2 ==0:
#         return True
#     else:
#         return False

# main()

#3 IMPROVING THE is_even() CODE IN A PYTHONIC WAY:

# def is_even(n):
#     return True if n % 2 == 0 else False

# main() 

#4 WE CAN FURTHER COMPRESS THIS CODE BASED ON BOOLIAN CONDITION

def is_even(n):
    return (n % 2 == 0)

main() 
