#CODE TO CHECK NAMES AND OUTPUT RESULTS

name = input("What's your name? ")


# if name == "Harry":
#     print ("Gryffindor")
# elif name == "Hermione":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")


#2 WE CON CONDENSE LINE 7 - 11 USING THE OR

# if name == "Harry" or name == "Hermione" or name == "Ron" :
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

#3 USING MATCH AND CASE TO IMPROVE THE CODE
#Requires python 3.10 and above https://docs.python.org/3/whatsnew/3.10.html
# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Hermione":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:                         #This handles exceptions like else
#         print("Who?")


#4 Further conpressing this code:

match name:
    case "Harry" | "Hermione" | "Ron":      # HERE WE ARE USING THE | SYMBOL AS OR
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:                         #This handles exceptions like else
        print("Who?")
      

