VALID_SIDES = {
    "BUY",
    "SELL",
}

VALID_TYPES = {
    "MARKET",
    "LIMIT",
}


def validate_order(
    symbol,
    side,
    order_type,
    quantity,
    price=None,
):
    symbol = symbol.upper().strip()
    side = side.upper().strip()
    order_type = order_type.upper().strip()

    if not symbol:
        raise ValueError("Trading symbol is required.")

    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL.")

    if order_type not in VALID_TYPES:
        raise ValueError(
            "Order type must be MARKET or LIMIT."
        )

    if quantity <= 0:
        raise ValueError(
            "Quantity must be greater than zero."
        )

    if order_type == "LIMIT":
        if price is None:
            raise ValueError(
                "LIMIT orders require a price."
            )

        if price <= 0:
            raise ValueError(
                "Price must be greater than zero."
            )

    return True