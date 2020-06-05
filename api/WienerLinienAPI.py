from typing import Any, Dict, List, Text, Optional, Tuple, Union
from enum import Enum, auto

import requests
import xml.dom.minidom


WIENER_LINIEN_API_BASE_URL = 'https://www.wienerlinien.at/ogd_routing/'


class StationNameValidationResult(Enum):
    EXACT_MATCH = auto()
    LIST_OF_CANDIDATES = auto()
    NO_MATCH = auto()


def validate_station_name(station_name: Text, allowed_locality_names=['Wien']) -> Tuple[StationNameValidationResult, Union[Text, List[Text]]]:
    station_name = station_name.lower()
    response = requests.get(
        WIENER_LINIEN_API_BASE_URL + 'XML_TRIP_REQUEST2',
        params={
            'locationServerActive': '1',
            'sessionID': '0',
            'type_origin': 'any',
            'name_origin': station_name
        }
    )
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
