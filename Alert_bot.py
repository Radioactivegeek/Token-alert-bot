from flask import Flask, request, jsonify
import requests
import json
import os

app = Flask(__name__)

# -------------- CONFIG --------------
USD_THRESHOLD = 10000  # swap size trigger

# Telegram setup
TELEGRAM_BOT_TOKEN = "8351070816:AAFUIua7DBUavXwu6mc36jrJ1r4iAlQv_eE"
TELEGRAM_CHAT_ID = "5107968823"

# Discord setup
DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"

# Path to watchlist file
WATCHLIST_FILE = "watchlist.json"

# Load mints from file
def load_watchlist():
    if os.path.exists(WATCHLIST_FILE):
        with open(WATCHLIST_FILE, "r") as f:
            return json.load(f)
    return {}

WATCHLIST_MINTS = load_watchlist()
# ------------------------------------


def send_telegram_message(text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    requests.post(url, json=payload)


def send_discord_message(text: str):
    payload = {"content": text}
    requests.post(DISCORD_WEBHOOK_URL, json=payload)


@app.route("/helius-webhook", methods=["POST"])
def helius_webhook():
    data = request.json

    for txn in data.get("transactions", []):
        swap = txn.get("events", {}).get("swap")
        if not swap:
            continue

        # Extract swap details
        usd_value = (
            swap.get("nativeInput", {}).get("usdAmount", 0)
            + swap.get("nativeOutput", {}).get("usdAmount", 0)
        )

        mint_in = swap.get("nativeInput", {}).get("mint")
        mint_out = swap.get("nativeOutput", {}).get("mint")
        tx_sig = txn.get("signature")

        # Filter: only swaps involving our watchlist mints
        if mint_in not in WATCHLIST_MINTS and mint_out not in WATCHLIST_MINTS:
            continue

        # Filter: only big swaps
        if usd_value < USD_THRESHOLD:
            continue

        # Format message
        message = (
            f"🚨 Whale Swap Alert!\n"
            f"Value: ${usd_value:,.2f}\n"
            f"From: {WATCHLIST_MINTS.get(mint_in, mint_in)}\n"
            f"To: {WATCHLIST_MINTS.get(mint_out, mint_out)}\n"
            f"Tx: https://solscan.io/tx/{tx_sig}"
        )

        # Send alerts
        send_telegram_message(message)
        if DISCORD_WEBHOOK_URL:
            send_discord_message(message)

    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    print(f"Loaded watchlist mints: {WATCHLIST_MINTS}")
    app.run(port=5000, debug=True)
