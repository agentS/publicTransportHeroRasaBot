from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from api.WienerLinienAPI import validate_station_name, StationNameValidationResult, lookup_routes
from api.model.api_types import Route, MeansOfTransportType
from datetime import datetime
import re


class JourneyDetailsForm(FormAction):

    def name(self):
        return 'journey_details_form'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['arrival_date', 'first_station']

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            'arrival_date': [self.from_entity(entity='time')],
            'first_station': [self.from_entity(entity='station', intent=['select_first_station'])],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ):
        dispatcher.utter_template('utter_submit_journey_details', tracker)
        return []


class SingleConnectionForm(FormAction):

    def name(self):
        return 'lookup_single_connection_form'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['departure_station', 'arrival_station', 'departure_date_time']

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            'departure_station': [self.from_entity(
                entity='station',
                role='departure',
                intent=['specify_departure_and_arrival_station']
            )],
            'arrival_station': [self.from_entity(
                entity='station',
                role='arrival',
                intent=['specify_departure_and_arrival_station']
            )],
            'departure_date_time': [self.from_entity(entity='time')],
        }

    def validate_departure_station(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if isinstance(value, list):
            departure_station_name = self._validate_single_departure_station(
                value[0], dispatcher, tracker, domain
            )
            arrival_station_name = self._validate_single_arrival_station(
                value[1], dispatcher, tracker, domain
            )
            if departure_station_name is not None and arrival_station_name is not None:
                return {
                    'departure_station': departure_station_name,
                    'arrival_station': arrival_station_name,
                }
            else:
                return {'departure_station': None, 'arrival_station': None}
        else:
            departure_station_name = self._validate_single_departure_station(
                value, dispatcher, tracker, domain
            )
            if departure_station_name is not None:
                return {'departure_station': departure_station_name}
            else:
                return {'departure_station': None, 'arrival_station': None}

    def _validate_single_departure_station(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Any:
        dispatcher.utter_message('Ich überprüfe schnell die von dir gewählte Abfahrtsstation.')

        (validation_result, matched_station_name) = validate_station_name(value)
        if validation_result == StationNameValidationResult.EXACT_MATCH:
            return value
        elif validation_result == StationNameValidationResult.LIST_OF_CANDIDATES:
            dispatcher.utter_message('Für die von dir gewählte Abfahrtsstation habe ich direkten Treffer, aber mehrere mögliche gefunden. Du musst die Abfrage leider noch einmal eingeben, da ich mir nicht sicher sein kann, welche Station gemeint ist. Die möglichen Treffer lauten: ' + (', '.join(matched_station_name)))
            return None
        elif validation_result == StationNameValidationResult.NO_MATCH:
            dispatcher.utter_message('Leider konnte ich für die von dir gewählte Abfahrtsstation keinen Treffer finden.')
            return None

    def validate_arrival_station(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if isinstance(value, list):
            arrival_station_name = self._validate_single_arrival_station(
                value[1], dispatcher, tracker, domain
            )
            departure_station_name = self._validate_single_departure_station(
                value[0], dispatcher, tracker, domain
            )
            if departure_station_name is not None and arrival_station_name is not None:
                return {
                    'arrival_station': arrival_station_name,
                    'departure_station': departure_station_name,
                }
            else:
                return {'departure_station': None, 'arrival_station': None}
        else:
            arrival_station_name = self._validate_single_arrival_station(
                value, dispatcher, tracker, domain
            )
            return {'arrival_station': arrival_station_name}

    def _validate_single_arrival_station(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Any:
        dispatcher.utter_message('Ich überprüfe schnell die von dir gewählte Zielstation.')

        (validation_result, matched_station_name) = validate_station_name(value)
        if validation_result == StationNameValidationResult.EXACT_MATCH:
            return matched_station_name
        elif validation_result == StationNameValidationResult.LIST_OF_CANDIDATES:
            dispatcher.utter_message('Für die von dir gewählte Zielstation habe ich direkten Treffer, aber mehrere mögliche gefunden. Du musst die Abfrage leider noch einmal eingeben, da ich mir nicht sicher sein kann, welche Station gemeint ist. Die möglichen Treffer lauten: ' + (', '.join(matched_station_name)))
            return None
        elif validation_result == StationNameValidationResult.NO_MATCH:
            dispatcher.utter_message('Leider konnte ich für die von dir gewählte Zielstation keinen Treffer finden.')
            return None

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ):
        dispatcher.utter_template('utter_lookup_single_connection_form', tracker)
        return []


class ActionLookupSingleConnection(Action):
    def name(self) -> Text:
        return 'action_lookup_single_connection'

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        departure_date_time = datetime.strptime(
            tracker.get_slot('departure_date_time'),
            '%Y-%m-%dT%H:%M:%S.%f%z'
        )
        routes = lookup_routes(
            tracker.get_slot('departure_station'),
            tracker.get_slot('arrival_station'),
            departure_date_time
        )
        if len(routes) > 0:
            dispatcher.utter_message(f'Ich habe die folgenden Verbindungen von {routes[0].departure_station} nach {routes[0].arrival_station} gefunden:')
            # see https://github.com/RasaHQ/rasa/issues/4461
            dispatcher.utter_message(json_message={
                'text': _convert_routes_to_markdown(routes),
                'parse_mode': 'MarkdownV2'
            })
        else:
            dispatcher.utter_message('Leider konnte ich keine Routen zwischen den von dir genannten Stationen finden. Versuche es bitte mit einer neuen Anfrage.')
        return [
            SlotSet('departure_station', None),
            SlotSet('arrival_station', None),
            SlotSet('departure_date_time', None),
        ]


def _convert_routes_to_markdown(routes: List[Route]) -> Text:
    markdown_representation = ''
    for route_index, route in enumerate(routes):
        markdown_representation += f'*Verbindung {str(route_index + 1)}:*\n'
        for partial_route_index, partial_route in enumerate(route.partial_routes):
            if partial_route.means_of_transport.means_of_transport_type != MeansOfTransportType.WALK:
                markdown_representation += f'{str(partial_route_index + 1)}. {partial_route.means_of_transport.product_name} __{partial_route.means_of_transport.short_name}__ '
                markdown_representation += f'von __{partial_route.departure_station}__ (Abfahrtszeit __{_format_time(partial_route.departure_time)}__)'
                markdown_representation += f' nach __{partial_route.arrival_station}__ (Ankunftszeit __{_format_time(partial_route.arrival_time)}__)'
                markdown_representation += f' Richtung {partial_route.means_of_transport.destination}\n'
            else:
                markdown_representation += f'{str(partial_route_index + 1)}. Fußweg nach {partial_route.arrival_station}, '
                markdown_representation += f'Losgehzeit __{_format_time(partial_route.departure_time)}__, '
                markdown_representation += f'Ankunftszeit __{_format_time(partial_route.arrival_time)}__'
        markdown_representation += '\n'

    return _normalize_markdown(markdown_representation)


def _normalize_markdown(markdown_representation: Text) -> Text:
    return re.sub(
        r'(\[|\]|\(|\)|~|`|>|#|\+|-|=|\||\{|\}|\.|!)',
        _replace_special_character,
        markdown_representation
    )


def _replace_special_character(match_object):
    return '\\' + match_object.group(0)


def _format_time(date_time: datetime) -> Text:
    return date_time.strftime('%H:%M')
