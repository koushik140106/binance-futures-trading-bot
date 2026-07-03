from bot.validators import validate_order


def test_market_order():
    assert validate_order(
        "BTCUSDT",
        "BUY",
        "MARKET",
        0.001,
    )


def test_limit_order():
    assert validate_order(
        "BTCUSDT",
        "SELL",
        "LIMIT",
        0.001,
        100000,
    )