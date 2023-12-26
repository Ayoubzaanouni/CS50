import random
import sys

def get_level():
    try:
        level = int(input("Level: "))
        return level
    except ValueError:
        return get_level()

while True:
    try:
        level = get_level()
        if(level > 0):
            break
    except TypeError:
        level = get_level()

answer = random.randint(1,level)
inp = -1
while answer != inp:
    try:
        if(inp < 1 or not isinstance(inp, int)):
            inp = int(input("Guess: "))
        elif(inp > answer):
            print("Too large!")
            inp = int(input("Guess: "))
        elif(inp < answer):
            print("Too small!")
            inp = int(input("Guess: "))
    except ValueError:
        inp = int(input("Guess: "))

print("Just right!")
sys.exit(1)
