import requests
from datetime import datetime
import smtplib
import time

my_lat = 5.3914  # 5.391450
my_lng = 7.0036  # 7.003664

my_position = (my_lat, my_lng)

# Sunset and Sunrise Times
parameters = {
    'lat': my_lat,
    'lng': my_lng,
    'formatted': 0,
}


response = requests.get('https://api.sunrise-sunset.org/json', params=parameters).json()
sunrise = int(response['results']['sunrise'].split('T')[1].split(':')[0]) + 1
sunset = int(response['results']['sunset'].split('T')[1].split(':')[0]) + 1
# can't have the api in a while loop...limits to api call within specified time

while True:
    current_hour = datetime.now().hour
    # print(sunset, sunrise, current_hour)

    # ISS Overhead Notifier Position
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data = response.json()
    iss_lat = float(data['iss_position']['latitude'])
    iss_lng = float(data['iss_position']['longitude'])

    iss_position = (iss_lat, iss_lng)

    # conditionals

    def iss_is_overhead():
        return my_lat - 2 <= iss_lat <= my_lat + 2 and my_lng - 2 <= iss_lng <= my_lng + 2


    def iss_at_latitude():
        return my_lat - 2 <= iss_lat <= my_lat + 2


    def iss_at_longitude():
        return my_lng - 2 <= iss_lng <= my_lng + 2


    def is_night():
        return sunset <= current_hour or current_hour <= sunrise


    # send email if ISS Overhead Notifier is overhead
    sender_email = 'goldenswiftmk1@gmail.com'
    password = 'koqf vilr ptqk qeno'
    recipient_email = 'reubenchimadestiny@gmail.com'

    if iss_is_overhead() and is_night():
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:  # send email
            connection.login(sender_email, password)

            connection.sendmail(
                from_addr=sender_email,
                to_addrs=recipient_email,
                msg=f'Subject: ISS Overhead \n\nLook Up👆\nThe ISS is above you in the sky at position {my_position}'
            )

        print("ISS spotted!")
    print(f'Running...   ISS at {iss_position}')

    # some hope, lol
    if iss_at_latitude():
        print('Hooray...the ISS is at your latitude')
        break
    if iss_at_longitude():
        print('Hey!!\nThe ISS is at your longitude')
        break

    time.sleep(30)

# Calculate for degree of freedom for lat (based on field of view of horizon) and corresponding lng
