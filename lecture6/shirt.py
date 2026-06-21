from PIL import Image
from PIL import ImageOps
import sys

if len(sys.argv) < 3:
    sys.exit("Too few arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many arguments")
elif not sys.argv[1].lower().endswith((".jpg",".jpeg",".png")) or not sys.argv[2].lower().endswith((".jpg",".jpeg",".png")):
    sys.exit("Enter an image file")
elif sys.argv[1].split(".")[-1] != sys.argv[2].split(".")[-1]:
    sys.exit("Enter files of the same extension")

try:
    file = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Image not found")
else:
    shirt = Image.open("shirt.png")
    resized = ImageOps.fit(file, shirt.size)
    resized.paste(shirt, mask = shirt)
    resized.save(sys.argv[2])

