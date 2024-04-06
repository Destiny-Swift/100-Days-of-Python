# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_deals = data_manager.flight_deals
email_list = data_manager.email_list
print(email_list)

flight_search = FlightSearch()
flight_data = FlightData()
notifier = NotificationManager()


for index, flight_deal in enumerate(flight_deals):
    result = flight_search.search(flight_deal['iataCode'])
    flight_data.add_flight(flight=result)
    print(f"{index + 1}/{len(flight_deals)}: {flight_deal} / Best Price:"
          f"{[flight.price for flight in flight_data.flights if flight.cityCodeTo == flight_deal['iataCode']][0]}")


for index, flight in enumerate(flight_data.flights):
    if flight.price <= flight_deals[index]['lowestPrice']:
        message = notifier.create_message(
            price=flight.price,
            city_from=flight.cityFrom,
            fly_from=flight.flyFrom,
            city_to=flight.cityTo,
            fly_to=flight.flyTo,
            departure_date=flight.departure_date,
            return_date=flight.return_date,
            book_link=flight.book_link,
        )

        notifier.send_emails(email_list, message)

        print(f"Email Sent: "
              f"{[flight_deal for flight_deal in flight_deals if flight_deal['city'] == flight.cityTo][0]}")
