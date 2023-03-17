#NOTE WE USE {} FOR DICTIONARY VALUES. WE REPRESENT THE PAIRS
# AS "KEY": "VALUES"

#NOTE 1

students = {
    "Hermione":"Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(students["Hermione"])  #This will print the value for the key "Hermione"
print(students["Harry"])    ##This will print the value for the key "Harry"
print(students["Ron"])      #This will print the value for the key "Ron" -->Gryffindor
print(students["Draco"])    #This will print the value for the key "Draco" -->Slytherin


#NOTE 2.
# WE CAN USE A FOR LOOP TPO ITERATE THROUGH THE DICTIONARY AND RETURN
#ONLY THE KEYS AS SHOWN BELOW:

for student in students:
    print(student)

#NOTE 3
# WE CAN PRINT THE KEY:VALUE PAIRS ALSO USING THE FOR LOOP AS SHOWN BELOW

for student in students:
    print(student, students[student], sep= ", ") # We introduce the separator to 
                                                # to override the default space separator in 
                                                #print function