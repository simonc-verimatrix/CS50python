
txt = input("What's your answer? ")

# if txt == "forty-two" or txt == "42" or txt == "forty two":
#     print("Yes")
# else:
#     print("No")


#USING CASE TO SOLVE THIS

match txt:
    case "forty-two" | "42" | "forty two":
        print("Yes")
    case _:
        print("No")