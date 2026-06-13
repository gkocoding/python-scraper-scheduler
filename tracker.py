import requests

response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=eur')
data = response.json()
ethereum_price = data["ethereum"]["eur"]
bitcoin_price = data["bitcoin"]["eur"]
print(f"Current Bitcoin price in EUR: {bitcoin_price}")
print(f"Current Ethereum price in EUR: {ethereum_price}")