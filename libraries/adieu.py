import inflect
p = inflect.engine()

Names =[]
while True:
    try:
        Name =input("Name: ")
        Names.append(Name)
    except EOFError:
        #print(Names)
        break
#print("Available Names are", Names)
NameList = p.join(Names)
print("Adieu, adieu, to", NameList)