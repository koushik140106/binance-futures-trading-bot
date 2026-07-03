from bot.orders import place_order

response = place_order(
    symbol="BTCUSDT",
    side="BUY",
    order_type="MARKET",
    quantity=0.001
)

print(response)