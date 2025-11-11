# --- Updated get_stock_price with company name detection ---

import os
import requests
from dotenv import load_dotenv

load_dotenv(r"C:\Users\rahul\Desktop\Project_DSI\deploying-ai\05_src\.secrets_f")
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

# Mapping of company names to tickers
COMPANY_SYMBOLS = {
    "microsoft": "MSFT",
    "apple": "AAPL",
    "google": "GOOGL",
    "alphabet": "GOOGL",
    "amazon": "AMZN",
    "meta": "META",
    "facebook": "META",
    "tesla": "TSLA",
    "nvidia": "NVDA",
    "at&t": "T"
}

def get_stock_price(query: str) -> str:
    """Fetch live stock prices from Alpha Vantage based on user input."""
    if not API_KEY:
        return "⚠️ Alpha Vantage API key not found."

    # Step 1: Identify the symbol (from ticker or company name)
    symbol = None
    for name, code in COMPANY_SYMBOLS.items():
        if name.lower() in query.lower() or code.lower() in query.lower():
            symbol = code
            break

    if not symbol:
        return "⚠️ I couldn’t identify the company. Try including the stock symbol (like AAPL or TSLA)."

    # Step 2: Call Alpha Vantage
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Step 3: Parse the response
    try:
        price = float(data["Global Quote"]["05. price"])
        change_percent = data["Global Quote"]["10. change percent"]
        return f"{symbol} is currently trading at ${price:.2f}, with a daily change of {change_percent}."
    except KeyError:
        return f"⚠️ Could not retrieve stock data for {symbol} right now."




