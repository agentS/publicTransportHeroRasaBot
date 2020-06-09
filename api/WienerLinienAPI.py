from typing import Any, Dict, List, Text, Optional, Tuple, Union
from enum import Enum, auto

import requests
import xml.dom.minidom
from datetime import datetime

from api.model.api_types import Route, PartialRoute, MeansOfTransport, MeansOfTransportType


WIENER_LINIEN_API_BASE_URL = 'https://www.wienerlinien.at/ogd_routing/'
TRIP_REQUEST_ENDPOINT = 'XML_TRIP_REQUEST2'


class StationNameValidationResult(Enum):
    EXACT_MATCH = auto()
    LIST_OF_CANDIDATES = auto()
    NO_MATCH = auto()


def validate_station_name(station_name: Text, allowed_locality_names=['Wien']) -> Tuple[StationNameValidationResult, Union[Text, List[Text]]]:
    station_name = station_name.lower()
    response = requests.get(
        WIENER_LINIEN_API_BASE_URL + TRIP_REQUEST_ENDPOINT,
        params={
            'locationServerActive': '1',
            'sessionID': '0',
            'type_origin': 'any',
            'name_origin': station_name
        }
    )
    response.encoding = 'UTF-8'
    print(response.url)

    dom = xml.dom.minidom.parseString(response.text)
    odv_elements = dom.getElementsByTagName('itdOdv')
    for odv_element in odv_elements:
        if odv_element.getAttribute('usage') == 'origin':
            odv_names = odv_element.getElementsByTagName('itdOdvName')
            if len(odv_names) == 1:
                odv_name = odv_names[0]
                identification_state = odv_name.getAttribute('state')
                if identification_state == 'identified':
                    name_element = odv_name.getElementsByTagName('odvNameElem')[0]
                    if name_element.getAttribute('locality') in allowed_locality_names:
                        return (
                            StationNameValidationResult.EXACT_MATCH,
                            name_element.getAttribute('objectName')
                        )
                    else:
                        return (StationNameValidationResult.NO_MATCH, None)
                elif identification_state == 'list':
                    candidates = []
                    for name_element in odv_name.getElementsByTagName('odvNameElem'):
                        if name_element.getAttribute('locality') in allowed_locality_names:
                            candidate_name = name_element.getAttribute('objectName').lower()
                            if candidate_name == station_name:
                                return (
                                    StationNameValidationResult.EXACT_MATCH,
                                    name_element.getAttribute('objectName')
                                )
                            else:
                                candidates.append(candidate_name)
                    return (StationNameValidationResult.LIST_OF_CANDIDATES, candidates)
                elif identification_state == 'notidentified':
                    return (StationNameValidationResult.NO_MATCH, None)
    return (StationNameValidationResult.NO_MATCH, None)


def lookup_routes(
    departure_station_name: Text,
    arrival_station_name: Text,
    departure_date_time: datetime
) -> List[Route]:
    response = requests.get(
        WIENER_LINIEN_API_BASE_URL + TRIP_REQUEST_ENDPOINT,
        params={
            'locationServerActive': '1',
            'type_origin': 'any',
            'name_origin': departure_station_name,
            'type_destination': 'any',
            'name_destination': arrival_station_name,
            'itdDate': departure_date_time.strftime('%Y%m%d'),
            'itdTime': departure_date_time.strftime('%H%M')
        }
    )
    response.encoding = 'UTF-8'
    print(response.url)

    dom = xml.dom.minidom.parseString(response.text)
    routes = []
    dom_route_list = dom.getElementsByTagName('itdRouteList')
    if len(dom_route_list) > 0:
        dom_route_list = dom_route_list[0]
        dom_routes = dom_route_list.getElementsByTagName('itdRoute')
        for dom_route in dom_routes:
            route = Route(
                departure_station_name,
                arrival_station_name
            )
            dom_partial_routes = dom_route.getElementsByTagName('itdPartialRoute')
            for dom_partial_route in dom_partial_routes:
                dom_points = dom_partial_route.getElementsByTagName('itdPoint')
                dom_departure_station = [point for point in dom_points if point.getAttribute('usage') == 'departure'][0]
                dom_departure_date_time = dom_departure_station.getElementsByTagName('itdDateTime')[0]
                dom_arrival_station = [point for point in dom_points if point.getAttribute('usage') == 'arrival'][0]
                dom_arrival_date_time = dom_arrival_station.getElementsByTagName('itdDateTime')[0]
                dom_means_of_transport = dom_partial_route.getElementsByTagName('itdMeansOfTransport')[0]
                means_of_transport_type_string = dom_means_of_transport.getAttribute('motType')
                means_of_transport_type = MeansOfTransportType.WALK
                if means_of_transport_type_string != '':
                    means_of_transport_type = MeansOfTransportType(int(means_of_transport_type_string))
                partial_route = PartialRoute(
                    dom_departure_station.getAttribute('nameWO'),
                    dom_arrival_station.getAttribute('nameWO'),
                    _convert_date_time(dom_departure_date_time),
                    _convert_date_time(dom_arrival_date_time),
                    MeansOfTransport(
                        dom_means_of_transport.getAttribute('shortname'),
                        dom_means_of_transport.getAttribute('productName'),
                        dom_means_of_transport.getAttribute('destination'),
                        means_of_transport_type
                    )
                )
                route.partial_routes.append(partial_route)
            routes.append(route)
    return routes


def _convert_date_time(dom_date_time: xml.dom.minidom.Element) -> datetime:
    dom_date = dom_date_time.getElementsByTagName('itdDate')[0]
    dom_time = dom_date_time.getElementsByTagName('itdTime')[0]
    return datetime(
        int(dom_date.getAttribute('year')),
        int(dom_date.getAttribute('month')),
        int(dom_date.getAttribute('day')),
        int(dom_time.getAttribute('hour')),
        int(dom_time.getAttribute('minute'))
    )
