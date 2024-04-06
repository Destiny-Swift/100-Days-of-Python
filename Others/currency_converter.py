import requests

"""
This is a simple conversion tool that leverages a Google Sheet which leverages the GOOGLEFINANCE function.
Settings are optimized to convert from NGN to set currencies
"""

SHEET_ENDPOINT = 'https://api.sheety.co/59a6c6dc665a1b5959bdd313b8ec884b/currencyConversion/prices'
CURRENCY_FORMAT = 'GBP'


class CurrencyConverter:
    @staticmethod
    def convert(currency: CURRENCY_FORMAT, amount: float):
        response = requests.get(url=SHEET_ENDPOINT)
        # response.raise_for_status()
        for conversion in response.json()['prices']:
            if conversion['currency'] == currency:
                return round(conversion['ngn'] * amount, 2)


print(CurrencyConverter().convert(currency='EUR', amount=104.71))
