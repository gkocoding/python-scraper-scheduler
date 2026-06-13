# 📈 Crypto Price Tracker with Telegram Alerts

> Automated Bitcoin & Ethereum price monitor that sends instant Telegram alerts on significant market moves.

---

## 🚀 Overview

This bot runs in the background, checking live crypto prices every hour via the **CoinGecko API**. If Bitcoin or Ethereum moves more than **10%** since the last check, you get an instant **Telegram notification** — no manual monitoring needed.

---

## ⚙️ How It Works

1. Fetches live BTC & ETH prices in EUR from CoinGecko
2. Compares them to the last saved prices (`previous_prices.json`)
3. If change > 10% → sends a Telegram alert
4. Saves current prices for the next comparison
5. Repeats every hour automatically

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| requests | API calls |
| schedule | Automated scheduling |
| python-dotenv | Secure credential management |
| CoinGecko API | Live crypto prices (no API key needed) |
| Telegram Bot API | Price change notifications |

---

## 📦 Installation

1. **Clone the repository**
```bash
   git clone https://github.com/gkocoding/python-scraper-scheduler.git
   cd python-scraper-scheduler
```

2. **Create and activate virtual environment**
```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Create `.env` file** in the root folder
TELEGRAM_TOKEN=your_telegram_bot_token

TELEGRAM_CHAT_ID=your_chat_id

5. **Run the tracker**
```bash
   python tracker.py
```

---

## 🔑 Getting Telegram Credentials

**Bot Token:**
- Open Telegram and search for [@BotFather](https://t.me/BotFather)
- Send `/newbot` and follow the instructions
- Copy the token you receive

**Chat ID:**
- Start your bot and send it any message
- Visit: `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`
- Find `"chat": {"id": ...}` in the response

---

## 📁 Project Structure
python-scraper-scheduler/

│

├── tracker.py            # Main script

├── previous_prices.json  # Auto-generated, stores last known prices

├── requirements.txt      # Dependencies

├── .env                  # Secret credentials (not tracked by git)

└── README.md

---

## 💡 Example Alert
Bitcoin price changed by 12.45%!

---

*Built as a portfolio project — part of a Python freelance development journey.*