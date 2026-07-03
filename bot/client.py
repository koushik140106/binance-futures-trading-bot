from binance.client import Client

from bot.config import API_KEY, API_SECRET, BASE_URL
from bot.logging_config import logger

if not API_KEY or not API_SECRET:
    raise ValueError(
        "API credentials not found. Please check your .env file."
    )

client = Client(API_KEY, API_SECRET)

client.FUTURES_URL = f"{BASE_URL}/fapi"

logger.info("Binance Futures Testnet client initialized.")