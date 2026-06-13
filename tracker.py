import requests
import json


response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=eur')
data = response.json()
ethereum_price = data["ethereum"]["eur"]
bitcoin_price = data["bitcoin"]["eur"]
previous_prices = {"bitcoin": bitcoin_price, "ethereum": ethereum_price}

try:
    with open("previous_prices.json", "r") as file:
        previous_prices = json.load(file)
except FileNotFoundError:
    previous_prices = None

print(previous_prices)
print(f"Current Bitcoin price in EUR: {bitcoin_price}")
print(f"Current Ethereum price in EUR: {ethereum_price}")