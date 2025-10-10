📘 README — Token Alert Bot
Overview

This script continuously listens to the Solana blockchain for transactions involving a specified token mint address.

Given a token mint address, it can:

Track large transfers or wallet movements.

Alert when a top holder moves tokens above a defined threshold.

Notify about mint or burn events.

Save all activity to a CSV log for analysis or reporting.

Designed for researchers, traders, and auditors who want real-time insights into token activity or potential market risks.

⚙️ Features

✅ Real-time monitoring of token transfers
✅ Detect large transfers or whale activity
✅ Alert for mint/burn events
✅ Track movements of top holders
✅ Export all activity to CSV
✅ Configurable thresholds for alerts
✅ Works via Helius RPC or any Solana RPC URL

📦 Installation

Install dependencies

pip install requests websocket-client


Clone or copy the script

git clone <repo-url>
cd token-alert-bot


Set up config in script

Inside the script, modify:

RPC_URL = "https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY"
TOKEN_MINT = "YourTokenMintAddress"
TOP_HOLDERS = 20
TRANSFER_THRESHOLD = 100000  # Alert for transfers above this amount
PROJECT_FOLDER = r"c:\Users\<yourname>\Desktop\solana 30 day projects"


Replace with your own Helius API key, mint address, and project folder path.

🧠 Usage

Run the script in terminal:

python token_alert.py


The bot will:

Continuously monitor the blockchain for your token.

Display alerts in the console for significant transfers.

Log all activity to a CSV file in your project folder.

💾 Output Example

Console Output:

[ALERT] Whale Transfer Detected!
Token: BONK
From: Ghs...abc
To: 9Lp...xyz
Amount: 250,000,000
Timestamp: 2025-10-10 12:34:56 UTC

[INFO] Mint Event: 100,000,000 BONK minted by 7GZ...DsY
Snapshot saved as c:\Users\you\Desktop\solana 30 day projects\token_alert_log.csv


CSV Output:

Event,From,To,Amount,Timestamp
Transfer,Ghs...abc,9Lp...xyz,250000000,2025-10-10 12:34:56
Mint,7GZ...DsY,,100000000,2025-10-10 12:35:00
Burn,9Lp...xyz,,5000000,2025-10-10 12:36:01

⚠️ Notes & Tips

Helius API is recommended for faster, reliable event queries — free API keys available at https://helius.xyz
.

Large tokens with high transaction volume may produce many alerts; adjust TRANSFER_THRESHOLD to reduce noise.

CSV logs can be imported into Notion or Excel for analysis.

🧩 Example Config (Helius RPC)
RPC_URL = "https://mainnet.helius-rpc.com/?api-key=be754fa2-3136-4be2-87ac-2b4021cc350b"
TOKEN_MINT = "BONKTokenMintAddress"
TOP_HOLDERS = 20
TRANSFER_THRESHOLD = 100000
PROJECT_FOLDER = r"c:\Users\chadh\OneDrive\Desktop\solana 30 day projects"

🔍 Common Use Cases

Detecting large whale transfers before price impact.

Monitoring mint/burn events for tokens under audit.

Real-time alerts for suspicious token activity.

Logging token events for project research or dashboards.

🧰 Troubleshooting
Issue	Fix
No alerts triggered	Check mint address, RPC connection, threshold
CSV not saving	Verify PROJECT_FOLDER path exists
Errors connecting to RPC	Check API key or switch to mainnet RPC
Too many alerts/noisy output	Increase TRANSFER_THRESHOLD value
🛡️ Best Practices

Use validated mint addresses (check Solscan/Explorer).

Don’t spam public RPCs; use your Helius or Alchemy key.

Keep CSV logs organized by date/time for analysis.

Timestamp CSV files when running multiple sessions:

CSV_NAME = f"alert_{TOKEN_MINT[:4]}_{datetime.now():%Y%m%d_%H%M}.csv"

📄 License
MIT License
© 2025 Your Name

✅ Example Workflow

Identify the mint address of the token to monitor.

Run the Token Alert Bot.

Review console alerts for large transfers or mint/burn events.

Check CSV logs and document in Notion for your research/project folder.
