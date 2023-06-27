import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
figlet.getFonts()

if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in figlet.getFonts():
    isRandomFont = False
else:

    sys.exit("Invalid usage")

txt = input("Input: ")

#figlet.setFont(font='slant')
for font in figlet.getFonts():
    if isRandomFont == False:
        try:
            figlet.setFont(font = sys.argv[2])
            print(f"Output:\n {figlet.renderText(txt)}")
            break

        except:

            sys.exit("Invalid usage")
    else:
        figlet.setFont(font = random.choice(figlet.getFonts()))
        print(f"Output:\n {figlet.renderText(txt)}")




