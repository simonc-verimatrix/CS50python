#INTROCUING A LIST AND USING A FOR LOOP ON THE FINIT LIST
#NOTE 1
# for i in [0, 1, 2]:         #WE USE [] TO REPRESENT A LIST
#     print("meow")

#NOTE 2
#IMPROVING THE CODE BY USING A RANGE FUNCTION WHICH WILL SPECIFY THE NUMBER
#IN THE LIST

# for i in range(4):         #range(3) means 3 times: 0, 1, 2.
#     print("meow")

#NOTE 3
#The variable i in this case is a variable that will never be used
#but important for the code.
# in Python, we can replace this variable i with _ and the code will stiil
#work.

# for _ in range(4):         #range(3) means 3 times: 0, 1, 2.
#     print("meow")


#NOTE 4
#Representing this in one line pythomically

#print("meow\n" * 3)             #NOTE THE \n. Without it, it will print
                                # all in one line.
                                # 
print("meow\n" * 3, end="")      #NOTE the end="" will override the default
                                #\n at the end of the above program                            