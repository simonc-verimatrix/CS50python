#task: https://cs50.harvard.edu/python/2022/psets/4/figlet/

from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
#To list all the functions in this package and their attributes
#and methods
##print(dir(Figlet()))

#To list all the available fonts in the getFonts()
fonts = figlet.getFonts()
#print(fonts)

# figlet.setFont(font="alphabet")
# text = "hello, world"
# print(figlet.renderText(text))

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))
elif len(sys.argv) == 3 and sys.argv[2] in fonts and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

text = input("Input: ")
print(figlet.renderText(text))
