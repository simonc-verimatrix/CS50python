#Write your result to a file and print the file at the end.

CamelCase = input("CamesCase: ")
snake_case = ""
for i in range(len(CamelCase)):
    if CamelCase[i].isupper():
       snake_case = snake_case + '_' + CamelCase[i].lower()

    else:
        snake_case = snake_case + CamelCase[i]
print("snake Case: ", snake_case)