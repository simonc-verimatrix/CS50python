# implementing the Super Mario Bros Game using python main function
#Functions allows to create abstractions, that is the simplication of a 
#complicated ideas.

#NOTE: To create a #
                   #
                   #

# for _ in range(3):
#     print("#")

#NOTE: 2. Using a fucntion to implement this.

# def main():
#     print_column(3)

# def print_column(height):
#     for _ in range(height):
#         print("#")

# main()


#The beautiful thing is that you can use this function abstraction to 
#make changes in terms of improving the underlying component of
#your code without making changes to the main. This is particularly cool
# when people are using your fucntion code.

#NOTE 3. Improving the print_colum function code.

# def main():
#     print_column(3)

# def print_column(height): 
#     print("#\n" * height, end="") # We introduce the end="" to truncate the 
#                                   # default \n at the end of print()
# main()

#NOTE 4 To re-engineer this code to print  ###
#                                          ###
#                                          ###
#

# def main():
#     print_square(3)

# def print_square(size):
#     for i in range(size):
#         for j in range(size):
#             print("#", end="")
#         print()                     #This prints the new line at the end of ### 
#                                     #for the "for j in range(size)"
#                                     #Without it all will be in one line


# main()

#NOTE 4 Improving the print_square code without the mult for loops

# def main():
#     print_square(3)

# def print_square(size):
#     for i in range(size):
#         print("#" * size)

# main()

#NOTE 5. WE CAN FURTHER ABSTRACT THIS CODE BY INTRODUCING ANOTHER FUNCT
# THAT HANDLES THE PRINTING PART.

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()