import requests
import json


response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=eur')
data = response.json()
bitcoin_price = data["bitcoin"]["eur"]
ethereum_price = data["ethereum"]["eur"]

try:
    with open("previous_prices.json", "r") as file:
        previous_prices = json.load(file)
except FileNotFoundError:
    previous_prices = None

if previous_prices is not None:
    bitcoin_change = (bitcoin_price - previous_prices["bitcoin"]) / previous_prices["bitcoin"] * 100
    ethereum_change = (ethereum_price - previous_prices["ethereum"]) / previous_prices["ethereum"] * 100
    if abs(ethereum_change) > 10:
        print(f"Ethereum price changed by {ethereum_change:.2f}% since the last check.")
    if abs(bitcoin_change) > 10:
        print(f"Bitcoin price changed by {bitcoin_change:.2f}% since the last check.")

print(previous_prices)
print(f"Current Bitcoin price in EUR: {bitcoin_price}")
print(f"Current Ethereum price in EUR: {ethereum_price}")