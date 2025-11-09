import requests

def currency_converter(base_currency, target_currency, amount):
    """
    Convert currency using live exchange rates from ExchangeRate API
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency.upper()}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching exchange rates. Please check your internet or currency code.")
        return

    data = response.json()
    rates = data.get("rates")

    if target_currency.upper() not in rates:
        print("Invalid target currency code.")
        return

    rate = rates[target_currency.upper()]
    converted_amount = amount * rate

    print(f"\n💱 {amount:.2f} {base_currency.upper()} = {converted_amount:.2f} {target_currency.upper()}")
    print(f"Exchange Rate: 1 {base_currency.upper()} = {rate:.4f} {target_currency.upper()}")

# Main program
if __name__ == "__main__":
    print("=== Currency Converter Using API ===")
    base = input("Enter base currency (e.g. USD, EUR, INR): ").strip()
    target = input("Enter target currency: ").strip()
    try:
        amount = float(input("Enter amount to convert: "))
        currency_converter(base, target, amount)
    except ValueError:
        print("Please enter a valid number for amount.")
