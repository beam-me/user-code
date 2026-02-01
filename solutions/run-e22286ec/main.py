import os
import json
import requests
import re

def get_inputs():
    defaults = {"stock_symbols": "GDX", "data_source": "Yahoo Finance", "scrape_frequency": "50"}
    env_input = os.environ.get("BEAM_INPUTS")
    if env_input:
        try:
            overrides = json.loads(env_input)
            defaults.update(overrides)
        except Exception:
            pass
    return defaults

def scrape_stock_price(stock_symbol, data_source):
    if data_source.lower() == "yahoo finance":
        url = f"https://finance.yahoo.com/quote/{stock_symbol}"
        response = requests.get(url)
        # Use regex to find the stock price in the HTML content
        match = re.search(r'"regularMarketPrice":{"raw":([\d.]+),', response.text)
        if match:
            return float(match.group(1))
    return None

def solve():
    inputs = get_inputs()
    
    # --- MANDATORY CASTING BLOCK (DO NOT MODIFY) ---
    stock_symbols = str(inputs.get('stock_symbols', 'GDX'))
    data_source = str(inputs.get('data_source', 'Yahoo Finance'))
    scrape_frequency = float(inputs.get('scrape_frequency', 50))
    # -----------------------------------------------
    
    # --- CALCULATION SECTION ---
    # Use the variables defined above (e.g. stock_symbols)
    
    stock_symbol_list = stock_symbols.split(',')
    stock_prices = {}
    
    for symbol in stock_symbol_list:
        price = scrape_stock_price(symbol.strip(), data_source)
        if price is not None:
            stock_prices[symbol.strip()] = price
    
    # Print the stock prices
    print(f"Calculated Result: {stock_prices}")
    return True

if __name__ == "__main__":
    solve()


### Explanation:
- The script fetches stock prices from Yahoo Finance using the `requests` library and parses the HTML content with a regular expression to extract the stock price.
- The mandatory casting block ensures that the input variables are correctly cast to their respective types.
- The `solve` function processes the stock symbols, fetches their prices, and prints the result.