from typing import Any, Dict, List, Text, Optional, Tuple, Union
from datetime import datetime
from enum import Enum, auto, unique


DATE_TIME_STRING_FORMAT = '%Y-%m-%dT%H:%M:%S'


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

    def to_serializable(self):
        serializable = vars(self)
        serializable['means_of_transport_type'] = self.means_of_transport_type.value
        return serializable


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

    def to_serializable(self):
        means_of_transport = self.means_of_transport.to_serializable()
        serializable = vars(self)
        serializable['means_of_transport'] = means_of_transport
        serializable['departure_time'] = self.departure_time.strftime(DATE_TIME_STRING_FORMAT)
        serializable['arrival_time'] = self.arrival_time.strftime(DATE_TIME_STRING_FORMAT)
        return serializable


class Route:
    def __init__(
        self,
        departure_station: Text,
        arrival_station: Text,
    ):
        self.departure_station = departure_station
        self.arrival_station = arrival_station
        self.partial_routes = []

    def __str__(self):
        partial_routes_string = ''
        for partial_route in self.partial_routes:
            partial_routes_string = partial_routes_string + str(partial_route) + '\n'
        return f'In order to get from {self.departure_station} to {self.arrival_station} take the following routes:\n{partial_routes_string}'

    def to_serializable(self):
        serializable = vars(self)
        partial_routes = [partial_route.to_serializable() for partial_route in self.partial_routes]
        serializable['partial_routes'] = partial_routes
        return serializable


class JourneyStop():
    def __init__(
        self,
        departure_station: Text,
        arrival_station: Text,
        desired_date_time: datetime,
        routes: List[Route]
    ):
        self.departure_station = departure_station
        self.arrival_station = arrival_station
        self.desired_date_time = desired_date_time
        self.routes = routes

    def to_serializable(self):
        serializable = vars(self)
        serializable['desired_date_time'] = self.desired_date_time.strftime(DATE_TIME_STRING_FORMAT)
        routes = [route.to_serializable() for route in self.routes]
        serializable['routes'] = routes
        return serializable


def create_journey_route_from_json(route_json: Dict) -> Route:
    route = Route(
        route_json['departure_station'],
        route_json['arrival_station']
    )
    for partial_route_json in route_json['partial_routes']:
        partial_route = PartialRoute(
            partial_route_json['departure_station'],
            partial_route_json['arrival_station'],
            datetime.strptime(partial_route_json['departure_time'], DATE_TIME_STRING_FORMAT),
            datetime.strptime(partial_route_json['arrival_time'], DATE_TIME_STRING_FORMAT),
            MeansOfTransport(
                partial_route_json['means_of_transport']['short_name'],
                partial_route_json['means_of_transport']['product_name'],
                partial_route_json['means_of_transport']['destination'],
                MeansOfTransportType(partial_route_json['means_of_transport']['means_of_transport_type'])
            )
        )
        route.partial_routes.append(partial_route)
    return route


def create_journey_stop_from_json(route_stop_json: List[Dict]) -> List[Route]:
    return JourneyStop(
        route_stop_json['departure_station'],
        route_stop_json['arrival_station'],
        datetime.strptime(route_stop_json['desired_date_time'], DATE_TIME_STRING_FORMAT),
        [create_journey_route_from_json(route_json) for route_json in route_stop_json['routes']]
    )
