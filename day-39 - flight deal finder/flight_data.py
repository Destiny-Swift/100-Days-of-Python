class FlightObject:
    # This class serves for making flight data into objects before being passed to the FlightDatas storage
    def __init__(self, flight_data):
        self.price = flight_data['price']
        self.cityFrom = flight_data['cityFrom']
        self.cityCodeFrom = flight_data['cityCodeFrom']
        self.flyFrom = flight_data['flyFrom']
        self.cityTo = flight_data['cityTo']
        self.cityCodeTo = flight_data['cityCodeTo']
        self.flyTo = flight_data['flyTo']
        self.departure_date = flight_data['local_departure'].split('T')[0]
        self.return_date = [route for route in flight_data['route']
                            if route['return'] == 1][-1]['local_arrival'].split('T')[0]
        self.book_link = flight_data['deep_link']


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(FlightObject(flight))
