import typer
from rich.console import Console
from rich.table import Table

from bot.orders import (
    place_order,
    get_balance,
    open_orders,
    cancel_order,
)
from bot.validators import validate_order

app = typer.Typer(
    help="Binance Futures Testnet Trading Bot",
    add_completion=False,
)

console = Console()


@app.command()
def trade(
    symbol: str = typer.Option(..., help="Trading symbol (e.g. BTCUSDT)"),
    side: str = typer.Option(..., help="BUY or SELL"),
    order_type: str = typer.Option(..., "--type", help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., help="Order quantity"),
    price: float = typer.Option(None, help="Price (required for LIMIT orders)"),
):
    try:
        validate_order(symbol, side, order_type, quantity, price)

        request = Table(title="Order Request")

        request.add_column("Field", style="cyan")
        request.add_column("Value", style="green")

        request.add_row("Symbol", symbol.upper())
        request.add_row("Side", side.upper())
        request.add_row("Order Type", order_type.upper())
        request.add_row("Quantity", str(quantity))

        if order_type.upper() == "LIMIT":
            request.add_row("Price", str(price))

        console.print(request)

        success, result = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )

        if success:
            response = Table(title="Order Response")

            response.add_column("Field", style="cyan")
            response.add_column("Value", style="green")

            response.add_row("Order ID", str(result.get("orderId")))
            response.add_row("Status", str(result.get("status")))
            response.add_row("Executed Qty", str(result.get("executedQty")))
            response.add_row(
                "Average Price",
                str(result.get("avgPrice", "N/A")),
            )

            console.print(response)
            console.print("[bold green]Order placed successfully.[/bold green]")

        else:
            console.print(f"[bold red]{result}[/bold red]")

    except Exception as e:
        console.print(f"[bold red]{e}[/bold red]")


@app.command()
def balance():
    success, result = get_balance()

    if success:
        table = Table(title="Account Balance")

        table.add_column("Type", style="cyan")
        table.add_column("USDT", style="green")

        table.add_row("Wallet Balance", result["wallet"])
        table.add_row("Available Balance", result["available"])

        console.print(table)

    else:
        console.print(f"[red]{result}[/red]")


@app.command()
def orders(symbol: str):
    success, result = open_orders(symbol)

    if not success:
        console.print(f"[red]{result}[/red]")
        return

    if len(result) == 0:
        console.print("[yellow]No open orders found.[/yellow]")
        return

    table = Table(title=f"Open Orders ({symbol.upper()})")

    table.add_column("Order ID")
    table.add_column("Side")
    table.add_column("Type")
    table.add_column("Price")
    table.add_column("Quantity")
    table.add_column("Status")

    for order in result:
        table.add_row(
            str(order["orderId"]),
            order["side"],
            order["type"],
            order["price"],
            order["origQty"],
            order["status"],
        )

    console.print(table)


@app.command()
def cancel(
    symbol: str,
    order_id: int,
):
    success, result = cancel_order(symbol, order_id)

    if success:
        console.print("[bold green]Order cancelled successfully.[/bold green]")
    else:
        console.print(f"[bold red]{result}[/bold red]")


if __name__ == "__main__":
    app()