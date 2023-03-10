# BANK PROGRAM
# hello -> $0
# h =! hello -> $20
# else -> $100
# ignore leading lines and 
# input is case insensitive 

txt = input("Greeting: ")
#txt = txt.lower()
txt = txt.strip().lower()
check = txt.find("hello")

first = txt.split(" ")[0]
index =first[0]

if check ==0:
    print("$0")
elif index == "h" and check != 0:
    print("$20")
else:
    print("$100")


