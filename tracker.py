import os
import schedule
from dotenv import load_dotenv
import requests
import json

load_dotenv()

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": message})

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def track_prices():
    print("Tracking prices...")
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
            send_telegram(f"Ethereum price changed by {ethereum_change:.2f}%!")
        if abs(bitcoin_change) > 10:
            send_telegram(f"Bitcoin price changed by {bitcoin_change:.2f}%!")

    current_prices = {"bitcoin": bitcoin_price, "ethereum": ethereum_price}
    with open("previous_prices.json", "w") as file:
        json.dump(current_prices, file)


import time


track_prices()  # Run immediately on start

schedule.every(10).seconds.do(track_prices)  # Schedule to run every hour

while True:
    schedule.run_pending()
    time.sleep(60)  