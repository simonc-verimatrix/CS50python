# name = input("Please enter your name: ")

# message = "Hello {}, Welcome to Python scripting".format(name)  #NOTE: A way of parsing arguements to strings
# print(message)

#NOTE:2

#firstName = input("Please enter first name: ").

# LastName = input("Please enter Lsst name: ")

# FullName = "My full name is {} {}".format(firstName,LastName)

# print(FullName)

#NOTE: Spliting

# x = "Java Home Cloud".split()   #By default sep of split is "space"
# for data in x:                  #Saparate the strint by space separator
#     print(data)


# NOTE: Slicing: Extracting certian characters from a string.

# x = "Unhappy"

# mood = x[2:]  #Start from charater 2 : to the end

# print(mood)


# x = "1234567"
# altnum = x[::2]     #Start from begining to the end with a step of '2' 
#                     # Note that first index is 0!

# reverse = x[::-1]   # Start from the end, to the begining step of 1


# print(altnum)       
# print(reverse)


#NOTE: List
#       0, 1,  2,    3
# data = [1, 2, 'A', 10.4]

# for x in data:
#     print(x)

# data.append(34)         #This will append 34 at the end of the list.
# data.insert(0, "B") # This will insert the object "B" at index "0" and push the other index forward
# data.delete[0]      #This will delete the object at index 0.
# print(data)
#print(insert)


#NOTE: SLicing on list
# print(data[::])     #Start from the begining till the end with a step of 1

# print(data[0:2:])   #Start from 0 and stop at index 2. ==> 0 to 1.

# print(data[0::2])   #Start from 0 till the end with a step of 2


#NOTE: Sets in python       # Set is NOT ordered and it does not accept duplicates
                            # There is no index operations in Sets

#       0, 1,  2,    3
# data = {1, 2, 'A', 10.4, 2}
# data.add('AWS')
# print(data)

# for x in data:              #No dublicte is allowed in sets
#     print(x)

#NOTE: Dictionary++> Key:Value ordered data

# data = {"Apple":30, "orrages": 90, "Grapes": 120}

# print(data["Apple"])

# data["Mangoes"] = 25

# print(data["Mangoes"])


#NOTE Exceptions Handling

# #Basic block of exception:
# try:                # Put the code that causes exception in try block
#     pass            #
# except:             #Handling exception should be done it the except block
#     pass
# finally:            #This is a code block that is executed always.
#     pass

#No exception here.
# try:
#     data = {"A": 1, "B":2}
#     print(data["A"])
# except:
#     print("Exception in the code")
# finally:
#     print("Finally called ..")


#Code with exception since no key C exist:
# try:
#     data = {"A": 1, "B":2}
#     print(data["C"])
# except:
#     print("Exception in the code")
# finally:
#     print("Finally called ..")


# try:
#     data = {"A": 1, "B":2}
#     print(10/0)
# except KeyError:
#     print("Exception in the code")
# except ZeroDivisionError:
#     print("Zero Division Error")
# finally:
#     print("Finally called ..")



#NOTE Control Statements

# x = 10
# y = 20
# if x > y:
#     print("X is greater than Y")
# else:
#     print("Y is greater than X")

#NOTE: While loop

# data = 1
# while data <= 10:
#     print(data)
#     data = data + 1


#NOTE: Continue and Break Stataements

# data = [1,2,0,5,10]
# a = 1
# for x in data:
#     a = a*x             #When x is 0, all remaining iteration will be 0
#     print(a)            #This can be avoided by using an exception
# print("The value of a is {}".format(a))


#Using the contiue to skip a case

data = [1,2,0,5,10]
a = 1
for x in data:
    if x ==0:               #If x is 0, skip and continue
        continue            
    a = a*x             
    print(a)
print("The value of a is {}".format(a))