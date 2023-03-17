#NOTE TO PROMPT OUR USER TO GIVE US THE NUMBER OF INT WE WANT TO MEOW
#BUT WE WANT THIS INPUT TO BE A POSITIVE NUMBER.
#WE CAN FIRST CHECK OUR INPUT NUMBER TO MAKE SURE IT MATCHES THIS
#CONDITION ELSE CONTINUE IN THE LOOP

#NOTE 1

# while True:
#     n = int(input("What's your number? "))
#     if n > 0:
#         break
# for _ in range(n):
#     print("meow")


#NOTE 2 Using the print method

while True:
    n = int(input("What's your number? "))
    if n > 0:
        print("meow\n" * n, end="")             #NOTE if you don't break
    break                                       #you will have infinite loop


