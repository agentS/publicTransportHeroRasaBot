from typing import Any, Dict, List, Text, Optional, Tuple, Union
from datetime import datetime
from enum import Enum, auto, unique


@unique
class MeansOfTransportType(Enum):
    TRAIN = 0
    SUBURBAN_RAILWAY = 1
    SUBWAY = 2
    LIGHT_RAIL = 3
    TRAMWAY = 4
    CITY_BUS = 5
    REGIONAL_BUS = 6
    EXPRESS_BUS = 7
    WALK = 99


class MeansOfTransport:
    def __init__(
        self,
        short_name: Text,
        product_name: Text,
        destination: Text,
        means_of_transport_type: MeansOfTransportType
    ):
        self.short_name = short_name
        self.product_name = product_name
        self.destination = destination
        self.means_of_transport_type = means_of_transport_type

    def __str__(self):
        return self.product_name + ' ' + self.short_name + ' towards ' + self.destination


class PartialRoute:
    def __init__(
        self,
        departure_station: Text, arrival_station: Text,
        departure_time: datetime, arrival_time: datetime,
        means_of_transport: MeansOfTransport
    ):
        self.departure_station = departure_station
        self.arrival_station = arrival_station
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.means_of_transport = means_of_transport

    def __str__(self):
        if self.means_of_transport.means_of_transport_type != MeansOfTransportType.WALK:
            return self.departure_station + ' to ' + self.arrival_station + ' with ' + str(self.means_of_transport) + ' departure from ' + str(self.departure_time) + ' arrival at ' + str(self.arrival_time)
        else:
            return 'Walk to ' + self.arrival_station + ' from ' + str(self.departure_time) + ' until ' + str(self.arrival_time)


class Route:
    def __init__(self, departure_station: Text, arrival_station: Text):
        self.departure_station = departure_station
        self.arrival_station = arrival_station
        self.partial_routes = []

    def __str__(self):
        partial_routes_string = ''
        for partial_route in self.partial_routes:
            partial_routes_string = partial_routes_string + str(partial_route) + '\n'
        return f'In order to get from {self.departure_station} to {self.arrival_station} take the following routes:\n{partial_routes_string}'
