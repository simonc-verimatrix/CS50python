#USING MAIN TO DEFINE YOUR FUNCTIONS. NOT A REQUIREMENT BUT A CONVENTION
# def main():                                     #Define your main function                                     
#     name = input("Whats's your name? ")         
#     hello(name)                                 #Call your hello() funtion with the arguement even if you have not defined

# def hello(to="World"):                          #DEFINE YOUR HELLO() FUNCTION
#     print("hello", to)


#main()                                


#2 ERROR DUE TO SCOPE. IS WHEN YOU ARE CALLING A VARIABLE OUTSIDE THE SCOPE IT IS DEFINED

def main():                                     #Define your main function                                     
    name = input("Whats's your name? ")         
    hello()                                 #Call your hello() funtion with the arguement even if you have not defined

def hello():                          #DEFINE YOUR HELLO() FUNCTION
    print("hello", name)

main()                                  #HERE IN THE SCOPE OF DEFINED hell(), name is not defined and the function takes 0 input