#1 DEFINE YOUR OWN FUNCTION USING DEF
# def hello():                #EVERYTHING UNDER THE : IDENTED IS PART OF THE FUNCTION
#     print("Simon")          # THE FUNCTION ONLY PRINTS SIMON

#hello()                     #CALLING THE FUNCTION


#2 DEFINE YOUR FUNCTION TO TAKE PARAMETER AS INPUT

# def hello(to):                #EVERYTHING UNDER THE : IDENTED IS PART OF THE FUNCTION
#     print("hello,", to)

# name = input("What's your name? ")
# hello(name)

#3 DEFINE YOUR FUNCTION TO TAKE PARAMETER AS INPUT WITH DEFAULT VALUE IF NOT PROVIDED
def hello(to="world"):                #EVERYTHING UNDER THE : IF NO INPUT VARIABLE IS PROVIDED, DEFAULT TO WORLD
    print("hello,", to)

name = input("What's your name? ")
hello()
hello(name)
