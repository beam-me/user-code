import math
import numpy as np
import os
import json
import requests
from html.parser import HTMLParser

def get_inputs():
    defaults = {"stock_symbol": "gdx", "source_website": "yahoo", "scrape_frequency": "90"}
    env_input = os.environ.get("BEAM_INPUTS")
    if env_input:
        try:
            overrides = json.loads(env_input)
            defaults.update(overrides)
        except Exception:
            pass
    return defaults

class YahooFinanceHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_price_tag = False
        self.price = None

    def handle_starttag(self, tag, attrs):
        if tag == 'fin-streamer':
            attrs_dict = dict(attrs)
            if attrs_dict.get('data-field') == 'regularMarketPrice':
                self.in_price_tag = True

    def handle_data(self, data):
        if self.in_price_tag:
            try:
                self.price = float(data.replace(',', ''))
            except ValueError:
                self.price = None
            self.in_price_tag = False

def scrape_stock_price(stock_symbol, source_website):
    if source_website.lower() == "yahoo":
        url = f"https://finance.yahoo.com/quote/{stock_symbol}"
        response = requests.get(url)
        if response.status_code == 200:
            parser = YahooFinanceHTMLParser()
            parser.feed(response.text)
            return parser.price
    return None

def solve():
    inputs = get_inputs()
    
    # --- MANDATORY CASTING BLOCK (DO NOT MODIFY) ---
    stock_symbol = str(inputs.get('stock_symbol', 'gdx'))
    source_website = str(inputs.get('source_website', 'yahoo'))
    scrape_frequency = float(inputs.get('scrape_frequency', 90))
    # -----------------------------------------------
    
    # --- CALCULATION SECTION ---
    # Use the variables defined above (e.g. stock_symbol)
    
    stock_price = scrape_stock_price(stock_symbol, source_website)
    if stock_price is not None:
        print(f"Calculated Result: {stock_price}")
    else:
        print("Calculated Result: Failed to retrieve stock price")

    return True

if __name__ == "__main__":
    solve()