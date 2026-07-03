# Binance Futures Trading Bot

A simple Python command-line application that places BUY and SELL MARKET/LIMIT orders on the Binance USDT-M Futures Testnet.

This project was built as part of a Python Developer application task. The focus is on clean code structure, input validation, logging, and proper error handling while interacting with the Binance Futures Testnet API.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL
- Command-line interface using Typer
- Input validation
- API request/response logging
- Exception handling
- Modular and reusable code structure

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── config.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── trading_bot.log
│
├── .env.example
├── .gitignore
├── cli.py
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Requirements

- Python 3.10+
- Binance Futures Testnet Account
- Binance Testnet API Key & Secret

---

## Installation

### Clone the repository

```bash
git clone https://github.com/koushik140106/binance-futures-trading-bot.git

cd binance-futures-trading-bot
```

### Create a virtual environment

Windows

```bash
python -m venv venv
```

or

```bash
py -m venv venv
```

Activate it

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Binance Testnet Setup

1. Open Binance Futures Testnet.
2. Create a Testnet account (or log in).
3. Generate a new API Key and Secret.
4. Copy both credentials.

Create a `.env` file in the project root.

Example:

```env
API_KEY=YOUR_API_KEY
API_SECRET=YOUR_SECRET_KEY
BASE_URL=https://testnet.binancefuture.com
```

---

## Running the Application

### MARKET BUY

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### MARKET SELL

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

---

### LIMIT BUY

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

---

### LIMIT SELL

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

## Sample Output

```
========== ORDER REQUEST ==========

Symbol      : BTCUSDT
Side        : BUY
Type        : MARKET
Quantity    : 0.001

Sending order...

Order Placed Successfully

Order ID      : 18708085017
Status        : NEW
Executed Qty  : 0.0000
Average Price : N/A
```

---

## Logging

All API requests, responses, and errors are automatically written to:

```
logs/trading_bot.log
```

Example log entry

```
2026-07-03 20:17:51 | INFO | Order Request | Symbol=BTCUSDT Side=BUY Type=MARKET Qty=0.001
2026-07-03 20:17:52 | INFO | Order Response | {'orderId': 18708085017, 'status': 'NEW'}
```

---

## Error Handling

The application handles common errors such as:

- Invalid order type
- Invalid side
- Missing price for LIMIT orders
- Invalid quantity
- Binance API errors
- Network-related exceptions
- Unexpected runtime errors

---

## Assumptions

- The application is intended for Binance USDT-M Futures Testnet.
- Valid Testnet API credentials are required.
- LIMIT orders use `GTC` (Good Till Cancelled).
- Average price may not be available immediately after placing an order.

---

## Technologies Used

- Python
- python-binance
- Typer
- Rich
- python-dotenv

---

## Future Improvements

Some possible enhancements include:

- Stop-Limit order support
- Interactive CLI menu
- Order history
- Position monitoring
- Cancel open orders
- Account balance command
- Docker support
- Unit tests

---

## License

This project is licensed under the MIT License.

---

## Author

**Koushik Amarendra**

B.Tech CSE (Cyber Security)

Python Developer | Cyber Security Enthusiast