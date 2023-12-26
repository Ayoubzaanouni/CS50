import sys
import csv

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)

if (not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv")):
    print("Not a CSV file")
    sys.exit(1)


try:
    with open(sys.argv[1]) as input:
        with open(sys.argv[2],'w') as output:
            fieldnames = ['first', 'last','house']
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()
            reader = csv.DictReader(input)
            for row in reader:
                last,first = row['name'].split(", ")
                writer.writerow({'first': first, 'last': last, 'house': row['house']})
except FileNotFoundError:
    print("Could not read "+sys.argv[1])
    sys.exit(1)

