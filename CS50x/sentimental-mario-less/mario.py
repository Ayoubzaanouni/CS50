# TODO
from cs50 import get_int

height = get_int("Height: ")

while True:
    if 1 > height or height > 8:
        height = get_int("Height: ")
    else:
        break

for i in range(height):
    print(((height-i)-1)*" " + "#" * (i+1))