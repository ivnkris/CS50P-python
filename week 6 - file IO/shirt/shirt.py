import sys
import os

import PIL
from PIL import Image

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command line arguments")

if ((sys.argv[1].lower().endswith(".jpg") or sys.argv[1].lower().endswith(".jpeg") or sys.argv[1].lower().endswith(".png")) == False) or ((sys.argv[2].lower().endswith(".jpg") or sys.argv[2].lower().endswith(".jpeg") or sys.argv[2].lower().endswith(".png")) == False):
    sys.exit("Invalid input")

if os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
    sys.exit("Input and output have different extensions")

try:
    shirt = Image.open("shirt.png")
    size = shirt.size
    avatar = Image.open(sys.argv[1])
    resized = PIL.ImageOps.fit(avatar, size)
    resized.paste(shirt, shirt)
    resized.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("File cannot be opened")