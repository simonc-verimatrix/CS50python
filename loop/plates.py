def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# txt = input("Text: ")             Simon will be True
# print(txt.isalnum())              simon. will be False

def is_valid(s):
    l = len(s)
    if 2 <= l <= 6 and s[:2].isalpha() and s.isalnum():
        if spec_cha(s):
            return True           
        
def spec_cha(s):
    for c in s:
        if c not in ["."," ", "?"]:
                if check_numbers(s):
                    return True
    
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


main()