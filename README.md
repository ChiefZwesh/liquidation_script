# Binance Liquidation WebSocket Script

This script connects to the Binance WebSocket and retrieves real-time liquidation data for all trading pairs using the "!forceOrder@arr" stream.

## Prerequisites

- Python 3.7 or higher

## Installation

No installation is required. The script only uses the standard Python libraries.

## Usage

1. Simply run the script using Python:

```bash
python script.py
```

2. The script will establish a WebSocket connection to Binance and start receiving liquidation messages.

3. Each message will be printed to the console in JSON format.

4. You can customize the script to perform additional processing on the liquidation data, such as saving it to a database, analyzing the data, or triggering certain actions based on liquidation events.

5. To stop the script, use `Ctrl + C` in the terminal.

## Disclaimer

This script is for educational and informational purposes only. Binance liquidation data can be highly volatile and may not be suitable for making trading decisions. Always conduct thorough research and consider seeking professional advice before making any financial decisions.

---
*Disclaimer: Trading involves risk, and the content provided here does not constitute financial advice. The author and the script contributors are not responsible for any losses or damages incurred while using this script. Use it at your own risk.*
