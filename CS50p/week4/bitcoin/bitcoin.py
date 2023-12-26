import json
import sys
import requests

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)
try:
    qte = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit(1)

o = response.json()

price = float(o["bpi"]["USD"]["rate"].replace(',',''))


print(f"${price*qte:,.4f}")