# import requests
import pandas as pd

SHEET_ENDPOINT = 'https://api.sheety.co/59a6c6dc665a1b5959bdd313b8ec884b/flightDeals/prices'
SHEETY_AUTH_KEY = 'Basic ZGVzdGlueTpJIGFtIElyb24gTWFu'

headers = {
    'Authorization': SHEETY_AUTH_KEY
}

sheet_url = 'https://docs.google.com/spreadsheets/d/11ORRxNLdnoV3XoQ6Hcfv8r9WesbygvXshyE0qrp1Y6c/export?format=csv'
email_list_url = 'https://docs.google.com/spreadsheets/d/1dGaAiQlX5mS8FmS9PTjVYxf4YoCemt6SWeZ85tPOx6g/export?format=csv'
email_list = pd.read_csv(email_list_url)


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.flight_deals = []
        self.get_sheet_data()
        self.email_list = email_list['Email Address']

    def get_sheet_data(self):
        # response = requests.get(url=SHEET_ENDPOINT, headers=headers)
        # self.flight_deals = response.json()['prices']

        # maxed out my monthly calls for this url
        # showing em how it's done with reading the sheet directly with pandas

        data = pd.read_csv(sheet_url)
        for index, city in enumerate(data['City']):
            self.flight_deals.append(
                {
                    'city': city,
                    'iataCode': data['IATA Code'][index],
                    'lowestPrice': int(str(data['Lowest Price'][index]).split('.')[0]),
                }
            )
