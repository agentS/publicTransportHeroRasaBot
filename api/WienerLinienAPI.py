from typing import Any, Dict, List, Text, Optional, Tuple
from enum import Enum, auto
import requests


WIENER_LINIEN_API_BASE_URL = 'https://www.wienerlinien.at/ogd_routing/'


class StationNameValidationResult(Enum):
    EXACT_MATCH = auto()
    LIST_OF_CANDIDATES = auto()
    NO_MATCH = auto()


def validate_station_name(station_name: Text) -> Tuple[StationNameValidationResult, Text]:
    response = requests.get(
        WIENER_LINIEN_API_BASE_URL + 'XML_TRIP_REQUEST2',
        params={
            'locationServerActive': '1',
            'sessionID': '0',
            'type_origin': 'any',
            'name_origin': station_name
        }
    )
    return (StationNameValidationResult.EXACT_MATCH, station_name)
