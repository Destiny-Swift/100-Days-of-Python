import requests
from datetime import datetime

# ISS Overhead Notifier Position
# response = requests.get('http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (longitude, latitude)
#
# print(iss_position)


# Sunset and Sunrise Times
parameters = {
    'lat': 5.391450,
    'lng': 7.003664,
    'formatted': 0,
}
response = requests.get('https://api.sunrise-sunset.org/json', params=parameters).json()
sunset = int(response['results']['sunset'].split('T')[1].split(':')[0]) + 1
sunrise = int(response['results']['sunrise'].split('T')[1].split(':')[0]) + 1

current_hour = datetime.now().hour

print(sunset)
print(sunrise)
print(current_hour)
