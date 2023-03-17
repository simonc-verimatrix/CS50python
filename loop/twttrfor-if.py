str = input("Str: ")
result = ""
vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
for i in range(len(str)):
    if str[i] not in vowel:
        result = result + str[i]
    
print(result)                                 
