#NOTE IN THE CASE WE HAVE A DICTIONARY WITH 3 VALUES PAIRS, WE CAN PRGRAM 
#IT IN THIS CASE AS A {DICTIONARY} IN A LIST.

#       NAME          HOUSE           PATRONUS
#0      Hermione      Gryffindor      Otter
#1      Harry         Gryffindor      Stag
#2      Ron           Gryffindor      Jack Russell terrier
#3      Draco         Slytherin         

#NOTE below is the list of dictionary

students = [
    {"name":"Hermione", "house": "Gryffindor", "patronus": "Otter" },
    {"name": "Harry", "house": "Gryffindor", "patronus":"Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus":"Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus":None}                   #NOTE: None is value when there is no value for the key in dict
]

#NOTE To print all the dict with key:value pairs, 

# for student in students:
#     print(student)

#NOTE To print only the Value of the key name --> students

# for student in students:
#     print(student["name"])

#NOTE To print all the information for each student

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")