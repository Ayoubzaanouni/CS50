import sys

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)

if (not sys.argv[1].endswith(".py")):
    print("Not a Python file")
    sys.exit(1)

try:
    with open(sys.argv[1]) as file:
        lines = file.read().splitlines()
        length = len(lines)
        for line in lines:
            checks = line.strip().split('\n')
            for check in checks:
                if(len(check) < 1 or check.startswith('#')):
                    length-=1
        print(length)
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)