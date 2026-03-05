import requests
import rich
import yfinance as yf
from rich.console import Console
from rich.table import Table

crypto_console = Console()
stock_console = Console()


def get_crypto_price(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids={crypto}"
    request = requests.get(url)
    output = request.json() #Dictionary for ex: {'bitcoin': {'usd': 72731}}
    return output[crypto]['usd']




def get_stock_price(stock):
    ticker = yf.Ticker(stock)
    current_price = ticker.info.get('currentPrice')
    return current_price



def crypto_vs_stock(choice):
    if choice == 'crypto':
        crypto_table = Table(title = "Crypto Price Tracker")

        crypto_table.add_column("Cryptocurrency", justify="center", style="cyan", no_wrap=True)
        crypto_table.add_column("Price (USD)", justify="center", style="magenta")

        currency_choice = input("Enter the cryptocurrency you want to track (Type NONE to exit): ")
        coins = set()

        while currency_choice.lower() != "none":
            try:
                coin = currency_choice.lower()
                if coin not in coins:
                    crypto_table.add_row(currency_choice.capitalize(), f"${get_crypto_price(currency_choice.lower())}")
                    crypto_console.print(crypto_table)
                    coins.add(coin.lower())
                    currency_choice = input("Enter the cryptocurrency you want to track (Type NONE to exit): ")
                else:
                    crypto_console.print(f'[bold yellow]Warning:[/bold yellow] "{currency_choice}" is already being tracked. Please enter a different cryptocurrency name.')  
                    crypto_console.print(crypto_table)
                    currency_choice = input("Enter the cryptocurrency you want to track (Type NONE to exit): ")
            except KeyError:
                crypto_console.print(f'[bold red]Error:[/bold red] "{currency_choice}" is not a valid cryptocurrency. Please enter valid cryptocurrency name.')  
                crypto_console.print(crypto_table)
                currency_choice = input("Enter the cryptocurrency you want to track (Type NONE to exit): ")
    
    elif choice == 'stock':
        stock_table = Table(title = "Stock Price Tracker")
        stock_table.add_column("Stock", justify="center", style="cyan", no_wrap=True)
        stock_table.add_column("Price (USD)", justify="center", style="magenta")

        stock_choice = input("Enter the stock you want to track (Type NONE to exit): ")
        stock_choice = stock_choice.upper()
        stocks = set()

        while stock_choice.lower() != "none":
            stock = stock_choice
            price = get_stock_price(stock_choice)
            if price is None:
                stock_console.print(f'[bold red]Error:[/bold red] "{stock_choice}" is not a valid stock. Please enter valid stock name.')  
                stock_console.print(stock_table)
                stock_choice = input("Enter the stock you want to track (Type NONE to exit): ")
                stock_choice = stock_choice.upper()
            elif stock not in stocks:
                    stock_table.add_row(stock_choice, f"${get_stock_price(stock_choice)}")
                    stocks.add(stock_choice)
                    stock_console.print(stock_table)
                    stock_choice = input("Enter the stock you want to track (Type NONE to exit): ")
                    stock_choice = stock_choice.upper()
            else:
                stock_console.print(f'[bold yellow]Warning:[/bold yellow] "{stock_choice}" is already being tracked. Please enter a different stock symbol.')  
                stock_console.print(stock_table)
                stock_choice = input("Enter the stock you want to track (Type NONE to exit): ")
                stock_choice = stock_choice.upper()
            


while True:
    choice_input = input("Do you want to track cryptocurrency or stock prices? (Type 'crypto', 'stock', or 'quit'): ")
    if choice_input.lower() == 'quit':
        break
    elif choice_input.lower() == 'crypto':
        crypto_vs_stock('crypto')
    elif choice_input.lower() == 'stock':
        crypto_vs_stock('stock')
    else:
        print("Invalid choice. Please enter 'crypto' or 'stock'.")
