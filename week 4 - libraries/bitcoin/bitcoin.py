import requests

import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    bitcoin_amount = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit("An error occured during the request from third party API")

amount = o["bpi"]["USD"]["rate_float"] * bitcoin_amount
print(f"${amount:,.4f}")