import os
from dotenv import load_dotenv
load_dotenv()

import requests
from datetime import datetime
import time
from cachetools import cached, TTLCache

# Load API key from environment
API_KEY = os.environ.get('EXCHANGERATE_API_KEY')

# Cache up to 100 items for 1 hour
cache = TTLCache(maxsize=100, ttl=3600)


@cached(cache=cache)
def get_exchange_rate(base_currency, target_currency):
    if not API_KEY:
        raise RuntimeError("EXCHANGERATE_API_KEY is not set. Set it in the environment or in a .env file.")
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return (data.get('conversion_rates', {}).get(target_currency),
            data.get('time_last_update_utc'),
            data.get('time_last_update_unix'))

def calculate_conversion(amount, rate):
    return amount * rate

def get_relative_time(unix_timestamp):
    """Convert unix timestamp to relative time (e.g., '19 hours ago')"""
    current_time = time.time()
    elapsed_seconds = current_time - unix_timestamp
    
    if elapsed_seconds < 60:
        return f"{int(elapsed_seconds)} seconds ago"
    elif elapsed_seconds < 3600:
        minutes = int(elapsed_seconds // 60)
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    elif elapsed_seconds < 86400:
        hours = int(elapsed_seconds // 3600)
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    elif elapsed_seconds < 604800:
        days = int(elapsed_seconds // 86400)
        return f"{days} day{'s' if days != 1 else ''} ago"
    else:
        weeks = int(elapsed_seconds // 604800)
        return f"{weeks} week{'s' if weeks != 1 else ''} ago"
@cached(cache=cache)
def get_all_supported_currencies():
    """Fetch all supported currency codes and names from the API"""
    if not API_KEY:
        print("EXCHANGERATE_API_KEY is not set. Cannot fetch supported currencies.")
        return []

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/codes"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if data.get('result') == 'success':
        return data.get('supported_codes', [])
    else:
        print(f"Error: {data.get('error-type')}")
        return []

if __name__ == "__main__":
    base_currency = input("Enter base currency (e.g., USD): ")
    target_currency = input("Enter target currency (e.g., EUR): ")
    amount = float(input("Enter amount to convert: "))

    rate = get_exchange_rate(base_currency, target_currency)[0]
    last_updated = get_exchange_rate(base_currency, target_currency)[1]
    last_updated_unix = get_exchange_rate(base_currency, target_currency)[2]
    if rate:
        converted_amount = calculate_conversion(amount, rate)
        print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency} at an exchange rate of {rate}.")
        relative_time = get_relative_time(last_updated_unix)
        print(f'last updated exchange rate from {base_currency} to {target_currency} is {relative_time}')
    else:
        print(f"Exchange rate for {target_currency} not found.")