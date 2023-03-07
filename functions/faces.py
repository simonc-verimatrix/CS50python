# txt = input()
# txt =txt.replace(":)", "😐").replace(":(", "🙁" )
# print(txt)

def main():
    txt = input()
    print(convert(txt))

def convert(txt):
    txt =txt.replace(":)", "😐").replace(":(", "🙁" )
    return txt

main()
