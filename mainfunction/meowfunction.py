#NOTE CREATING A FUNCTION THAT WILL MEOW


def main():
    num = get_num()
    meow(num)

def get_num():                          #THIS CHECKS THAT N IS POSITIVE
    while True:
        n = int(input("Whats's your n? "))
        if n > 0:
            break
    return n                               # IT RETURNS N TO BE USED MEOW()

def meow(n):
    for _ in range(n):
        print("meow")

main()