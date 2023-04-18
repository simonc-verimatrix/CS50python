
while True:
    num = input("Fraction: ")
    index = num.find("/")
    try:    
        x = int(num[:index])
        y = int(num[index+1:])
        fraction = x/y
        if x > y: 
            continue     
        break
    except (ValueError, ZeroDivisionError):
        continue


percentage = fraction * 100
if fraction <= 0.1:
    print("E")
elif fraction >= 0.99:
    print("F")
else:
    print(f"{percentage:.0f}" + "%")