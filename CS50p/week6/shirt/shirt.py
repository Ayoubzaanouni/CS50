from PIL import Image, ImageOps
import sys

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
extentions = ["jpg","jpeg","png"]
arg1 = sys.argv[1].split('.')
arg2 = sys.argv[2].split('.')
if (arg1[1] not in extentions ):
    print("Invalid Input")
    sys.exit(1)

if (arg1[1] not in extentions ):
    print("Invalid output")
    sys.exit(1)

if(arg1[1] != arg2[1]):
    print("Input and output have different extensions")
    sys.exit(1)

try:
    shirt = Image.open("shirt.png")
    size = shirt.size
    face = Image.open(sys.argv[1])
    face = ImageOps.fit(face, size, Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    face.paste(shirt, box=None, mask=shirt)
    face.save(sys.argv[2])

except FileNotFoundError:
    print("Could not read "+sys.argv[1])
    sys.exit(1)
