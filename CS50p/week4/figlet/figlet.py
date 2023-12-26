from pyfiglet import Figlet
from random import choice
import sys

if (len(sys.argv) not in [1,3]):
    print("Invalid usage")
    sys.exit(1)

figlet = Figlet()
list_fig = figlet.getFonts()
if len(sys.argv) == 1:
    font = choice(list_fig)
    figlet.setFont(font=font)
    print(figlet.renderText(input("Input: ")))
else:
    if(sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        if(sys.argv[2] in list_fig):
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(input("Input: ")))
        else:
            print("Invalid usage")
            sys.exit(1)
    else:
        print("Invalid usages")
        sys.exit(1)