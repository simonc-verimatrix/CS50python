import sys
from sayings import hello 

if len(sys.argv) == 2:
    hello(sys.argv[1])

#Because of the if __name__=="__main__" statement in the main function
#We can import only hello or goodbye function without invoking the
#the whole main function.
