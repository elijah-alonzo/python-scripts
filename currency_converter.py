import requests
import sys

def convert(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)
    if response.status_code == 200:
        rates = response.json()["rates"]
        if to_currency.upper() in rates:
            converted = amount * rates[to_currency.upper()]
            print(f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
        else:
            print("Currency not found.")
    else:
        print("Error fetching exchange rates.")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python currency_converter.py <amount> <from_currency> <to_currency>")
    else:
        convert(float(sys.argv[1]), sys.argv[2], sys.argv[3])
