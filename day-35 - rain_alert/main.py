import requests
from twilio.rest import Client

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = '3046418815e0420d35562b2e1a14599a'
account_sid = 'AC5d701f98f98deb06a18944c0c5c3851a'
auth_token = '4a43d3ecbde6e50f187055a1511b18c0'

# the api used in the tutorial is now paid and I settled for this 3-hour forecast over 5 days period
# so instead of reading the entire hourly forecast for the next 12 hours and checking whether it'll rain;
# I read the 3-hour forecasts for 6am, 9am, 12pm, 3pm and 6pm 😎

weather_params = {
    'lat': 5.4890,
    'lon': 7.0175,
    'appid': api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data['list'][:5]

will_rain = False
rain_forecast = []

for forecast in weather_slice:
    condition_code = forecast['weather'][0]['id']

    if condition_code < 700:
        will_rain = True
        rain_forecast.append(forecast)

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain. Remember to bring an umbrella ☔☔☔"
             f"\n\nOr make it 3 😏\n\n{rain_forecast}",
        from_='+12569603009',
        to='+2347012222695'
    )

    print(message.sid)
