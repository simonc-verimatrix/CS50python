#Hogwarts students in a list
#NOTE 1
students = ["Hermione", "Harry", "Ron"]

# print(students[0])
# print(students[1])
# print(students[2])

#NOTE 2 Using a loop in the list to print all the students

# for student in students:
#     print(student)


#NOTE 3 Using a range to print the list. We need to use the len= lenght 
# of list so we can use range.
# print(len(students)) ----> 3 [0, 1, 2]
# for i in range(len(students)):
#     print(i)             # -----> This will print the range [0,1,2]


#NOTE 4 To print the list of students with their numbers

for i in range(len(students)):
    print(i +1 , students[i])            
