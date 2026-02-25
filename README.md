# Binance Futures Testnet Trading Bot

## Objective
A simplified Python CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

---

## Project Structure

trading_bot/
  bot/
    client.py
    orders.py
    validators.py
    logging_config.py
  cli.py
  requirements.txt
  trading_bot.log

---

## Setup Instructions

1. Clone the repository

2. Create virtual environment
   python -m venv venv

3. Activate environment
   Windows:
   venv\Scripts\activate

4. Install dependencies
   pip install -r requirements.txt

5. Create a `.env` file in root directory:

   BINANCE_API_KEY=your_api_key
   BINANCE_SECRET_KEY=your_secret_key

6. Use Binance Futures Testnet:
   https://testnet.binancefuture.com


## Usage Examples

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 90000


## Logging

All API requests, responses, and errors are logged in:

trading_bot.log


## Assumptions

- User has a Futures Testnet account
- Minimum notional value rules are respected
- Leverage set to 10x before placing order