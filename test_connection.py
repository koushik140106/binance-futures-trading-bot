from bot.client import client

try:
    account = client.futures_account()

    print("\nConnected Successfully")
    print("-" * 40)
    print("Wallet Balance :", account["totalWalletBalance"])
    print("Available      :", account["availableBalance"])

except Exception as e:
    print("Connection Failed")
    print(e)