
# x is an integer
# y is +, -, *, or /
# z is an integer
expression = input("What's your expression: ")
x = expression.split(" ")[0]
y = expression.split(" ")[1]
z = expression.split(" ")[2]
x = int(x)
z = int(z)

if y == "+":
    print(f"{x + z:.1f}")
elif y == "-":
    print(f"{x - z:.1f}")
elif y == "*":  
    print(f"{x * z:.1f}")
elif y == "/":
    print(f"{x / z:.1f}")
else:
    print("No solution found")
