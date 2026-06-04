import requests
import sys

currency = input("Cryptocurrency: ").strip().lower()

response = requests.get(
    "https://api.coingecko.com/api/v3/simple/price?ids=" + currency + "&vs_currencies=usd"
)

data = response.json()
try:
    value = float(data[currency]["usd"])
except KeyError:
    sys.exit("Cryptocurrency not valid")
else:
    try:
        amount = float(input("Amount: "))
    except ValueError:
        sys.exit("Enter a valid amount")
    else:
        price = value*amount
        print(f"{amount} {currency} cost ${price:.2f}")


