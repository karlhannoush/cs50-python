import pyfiglet
import sys
import random

s = sys.argv

if len(s) == 2:
    sys.exit("Too few arguments")
elif len(s) > 3:
    sys.exit("Too many arguments")

fonts_list = pyfiglet.FigletFont.getFonts()

if len(s) == 3:
    if s[1] not in ["-f","--font"] or s[2] not in fonts_list:
        sys.exit("Enter valid command-line arguments")
    else:
        user = input("Input: ")
        print(pyfiglet.figlet_format(user, font = s[2]))
else:
    choice = random.choice(fonts_list)
    user = input("Input: ")
    print(pyfiglet.figlet_format(user, font = choice))
