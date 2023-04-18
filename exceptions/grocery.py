# define an empty dict to store grocery items
grocery_list = {}

# prompt the user to enter grocery items, and add each item to the list
while True:
    try:
        item = input().upper()
    except EOFError:
        print()
        break
# print out the grocery list
    #print("Your grocery list:", grocery_list)
    if item in grocery_list:
        grocery_list[item] += 1
    else:
        grocery_list[item] = 1
#Make sure you sort the keys before iteration
sortedkeys = sorted(grocery_list.keys())
# print(grocery_list)
# print(sortedkeys)
for item in sortedkeys:
    print(grocery_list[item], item)
