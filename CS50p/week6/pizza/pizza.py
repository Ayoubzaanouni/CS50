from tabulate import tabulate
import csv
# print(tabulate(table, headers, tablefmt="grid"))

import sys

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)

if (not sys.argv[1].endswith(".csv")):
    print("Not a CSV file")
    sys.exit(1)

try:
    with open(sys.argv[1]) as file:
        menu = []
        reader = csv.reader(file)
        for name,price_small,price_large in reader:
            menu.append({"name": name, "price_small": price_small, "price_large":price_large})
        print(tabulate(menu[1:], menu[0], tablefmt="grid"))
        
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)