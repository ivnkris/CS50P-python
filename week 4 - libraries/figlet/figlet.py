from pyfiglet import Figlet

import random
import sys

figlet = Figlet()

if len(sys.argv) > 1 and sys.argv[1] != "-f" and sys.argv[1] != "--font":
    sys.exit("Invalid usage")

fonts = figlet.getFonts()

if len(sys.argv) > 1:
    is_font = sys.argv[2] in fonts
    if is_font != True:
        sys.exit("Invalid usage")

str = input("Input: ")

if len(sys.argv) == 1:
    random_font_index = random.randint(0, len(fonts))
    set_font = fonts[random_font_index]

if len(sys.argv) == 3:
    set_font = sys.argv[2]

figlet.setFont(font=set_font)
print(figlet.renderText(str))