txt = input("Text: ")
#print(txt.isalnum())
#print(txt.isdigit())
for char in txt:
    if char.isdigit():
        index = txt.index(char)
        print(index)
    else:
        print("Nothing")


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# txt = input("Text: ")             Simon will be True
# print(txt.isalnum())              simon. will be False

def is_valid(s):
     while True:
         l = len(s)
         if 2 <= l <= 6:
             if s[:2].isalpha() and s.isalnum():        
                return s
         break


main()


def is_valid(s):
    if check_length(s) and check_begin(s) and check_spec(s) and check_numbers(s):
        return True
    else:
        return False



def check_numbers(s):
    firstnum = None
    for c in s:
        if c.isdigit():
            firstnum = c
            break
    if firstnum == None:
        return True
    if int(firstnum) == 0:
        return False
    index = s.index(firstnum)
    position = len(s) - index
    for c in s[-position:]:
        if not c.isdigit():
            return False
    return True






    def is_valid(s):
    l = len(s)
    if 2 <= l <= 6 and s[:2].isalpha() and s.isalnum():
        for c in s:
            if c not in ["."," ", "?"]:
                return True and  