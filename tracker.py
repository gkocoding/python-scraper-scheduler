import os
import asyncio
from telegram import Bot
from dotenv import load_dotenv
import requests
import json

load_dotenv()

async def send_telegram(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

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

asyncio.run(send_telegram(f"Bitcoin price changed by {bitcoin_change:.2f}%!"))
asyncio.run(send_telegram(f"Ethereum price changed by {ethereum_change:.2f}%!"))

current_prices = {"bitcoin": bitcoin_price, "ethereum": ethereum_price}
with open("previous_prices.json", "w") as file:
    json.dump(current_prices, file)