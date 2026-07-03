from binance.exceptions import BinanceAPIException, BinanceOrderException
from bot.client import client
from bot.logging_config import logger


def place_order(symbol, side, order_type, quantity, price=None):
    try:
        symbol = symbol.upper()
        side = side.upper()
        order_type = order_type.upper()

        logger.info(
            f"Order Request | Symbol={symbol} | Side={side} | Type={order_type} | Quantity={quantity} | Price={price}"
        )

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        response = client.futures_create_order(**params)

        logger.info(f"Order Response | {response}")

        return True, response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error | {e}")
        return False, str(e)

    except BinanceOrderException as e:
        logger.error(f"Binance Order Error | {e}")
        return False, str(e)

    except Exception as e:
        logger.exception("Unexpected Error")
        return False, str(e)


def get_balance():
    try:
        account = client.futures_account()

        data = {
            "wallet": account["totalWalletBalance"],
            "available": account["availableBalance"],
        }

        logger.info(f"Balance Request | {data}")

        return True, data

    except Exception as e:
        logger.error(f"Balance Error | {e}")
        return False, str(e)


def open_orders(symbol):
    try:
        orders = client.futures_get_open_orders(
            symbol=symbol.upper()
        )

        logger.info(f"Open Orders | Symbol={symbol}")

        return True, orders

    except Exception as e:
        logger.error(f"Open Orders Error | {e}")
        return False, str(e)


def cancel_order(symbol, order_id):
    try:
        response = client.futures_cancel_order(
            symbol=symbol.upper(),
            orderId=order_id,
        )

        logger.info(
            f"Cancel Order | Symbol={symbol} | OrderID={order_id}"
        )

        return True, response

    except Exception as e:
        logger.error(f"Cancel Order Error | {e}")
        return False, str(e)


def get_order(symbol, order_id):
    try:
        response = client.futures_get_order(
            symbol=symbol.upper(),
            orderId=order_id,
        )

        logger.info(
            f"Get Order | Symbol={symbol} | OrderID={order_id}"
        )

        return True, response

    except Exception as e:
        logger.error(f"Get Order Error | {e}")
        return False, str(e)


def positions():
    try:
        response = client.futures_position_information()

        active_positions = [
            position
            for position in response
            if float(position["positionAmt"]) != 0
        ]

        logger.info("Fetched Open Positions")

        return True, active_positions

    except Exception as e:
        logger.error(f"Positions Error | {e}")
        return False, str(e)


def account_info():
    try:
        account = client.futures_account()

        info = {
            "wallet": account["totalWalletBalance"],
            "available": account["availableBalance"],
            "unrealized": account["totalUnrealizedProfit"],
            "margin": account["totalMarginBalance"],
        }

        logger.info("Fetched Account Information")

        return True, info

    except Exception as e:
        logger.error(f"Account Info Error | {e}")
        return False, str(e)