import requests
from datetime import datetime, timedelta
from pprint import pprint

DEPARTURE_AIRPORT = 'LOS'  # IATA for Murtala Muhammed International Airport, Lagos, Nigeria
TEQUILA_API_KEY = 'tNyWv70zzC9NHWbnUfJLaMVvbE85JcSv'
TEQUILA_ENDPOINT = 'https://api.tequila.kiwi.com/v2/search/'
DATE_FROM = datetime.now().strftime('%d/%m/%Y')
DATE_TO = (datetime.now() + timedelta(weeks=24)).strftime('%d/%m/%Y')  # 6 months or 24 weeks


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.headers = {}
        self.flight_data = {}

    def search(self, destination):
        self.flight_data = {
            'fly_from': DEPARTURE_AIRPORT,
            'fly_to': destination,
            'date_from': DATE_FROM,
            'date_to': DATE_TO,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 21,
            'curr': 'NGN'
        }

        self.headers = {
            'apikey': TEQUILA_API_KEY
        }

        response = requests.get(
            url=TEQUILA_ENDPOINT,
            params=self.flight_data,
            headers=self.headers,
        )
        response.raise_for_status()

        if response.json()['data']:
            return response.json()['data'][0]  # first is cheapest by experience


if __name__ == '__main__':
    pprint(FlightSearch().search('DPS'))
