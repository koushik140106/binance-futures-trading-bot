import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("TradingBot")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler = logging.FileHandler(
    "logs/trading_bot.log",
    encoding="utf-8",
)

file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)