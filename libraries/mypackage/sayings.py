def main():
    hello("world")
    goodbye("world")
   
def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")
#The bello if statement gives the main function call conditons
#esp if you want to import only a function from all the functions
#contained in the main function
if __name__=="__main__":
    main()